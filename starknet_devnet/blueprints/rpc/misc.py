"""
RPC miscellaneous endpoints
"""

from __future__ import annotations

from typing import Union

from starkware.starknet.services.api.feeder_gateway.response_objects import (
    PENDING_BLOCK_ID,
)

from starknet_devnet.blueprints.rpc.schema import validate_schema
from starknet_devnet.blueprints.rpc.structures.responses import (
    EmittedEvent,
    RpcEventsResult,
)
from starknet_devnet.blueprints.rpc.structures.types import (
    Address,
    BlockId,
    Felt,
    PredefinedRpcErrorCode,
    RpcError,
)
from starknet_devnet.blueprints.rpc.utils import (
    assert_block_id_is_latest_or_pending,
    get_block_by_block_id,
    rpc_felt,
)
from starknet_devnet.state import state


def check_address(address, event):
    """
    Check address.
    """
    return event.from_address == int(address, 0)


def check_keys(keys, event):
    """
    Check keys.
    """
    return bool(set(event.keys) & set(keys))


def get_events_from_block(block, address, keys):
    """
    Return filtered events.
    """
    events = []
    for receipt, event in [
        (r, e) for r in block.transaction_receipts for e in r.events
    ]:
        if check_keys(keys, event) and check_address(address, event):
            _event: EmittedEvent = {
                "from_address": rpc_felt(event.from_address),
                "keys": [rpc_felt(e) for e in event.keys],
                "data": [rpc_felt(d) for d in event.data],
                "block_hash": rpc_felt(block.block_hash),
                "block_number": block.block_number,
                "transaction_hash": rpc_felt(receipt.transaction_hash),
            }
            events.append(_event)

    return events


@validate_schema("chainId")
async def chain_id() -> str:
    """
    Return the currently configured StarkNet chain id
    """
    devnet_state = state.starknet_wrapper.get_state()
    config = devnet_state.general_config
    chain: int = config.chain_id.value
    return hex(chain)


@validate_schema("syncing")
async def syncing() -> Union[dict, bool]:
    """
    Returns an object about the sync status, or false if the node is not synching
    """
    return False


# pylint: disable=redefined-builtin
# filter name is determined by current RPC implementation and starknet specification
@validate_schema("getEvents")
async def get_events(filter) -> RpcEventsResult:
    """
    Returns all events matching the given filters.

    In our implementation continuation_token is just a number.

    In state.starknet_wrapper.get_state().events there is no relation between blocks.
    This is why we need to iterate block by block, take all events,
    and chunk it later which is not an optimal solution.
    """
    # Required parameters
    from_block = await get_block_by_block_id(filter.get("from_block"))
    to_block = await get_block_by_block_id(filter.get("to_block"))

    try:
        chunk_size = int(filter.get("chunk_size"))
    except ValueError as ex:
        raise RpcError(
            code=PredefinedRpcErrorCode.INVALID_PARAMS.value,
            message=f"invalid chunk_size: '{filter.get('chunk_size')}'",
        ) from ex

    address = filter.get("address")
    keys = [int(k, 0) for k in filter.get("keys")]
    # Optional parameter
    continuation_token = filter.get("continuation_token", "0")

    events = []

    include_pending = to_block == PENDING_BLOCK_ID
    block_range = list(range(from_block.block_number, to_block.block_number + 1))

    if include_pending:
        # pending needs to be included separately as it is not reachable through a number
        block_range.append(PENDING_BLOCK_ID)

    for block_number in block_range:
        block = await state.starknet_wrapper.blocks.get_by_number(block_number)
        if block.transaction_receipts:
            events.extend(get_events_from_block(block, address, keys))

    # Chunking
    continuation_token = int(continuation_token)
    start_index = continuation_token * chunk_size
    events = events[start_index : start_index + chunk_size]

    # Continuation_token should be increased only if events are not empty
    if events:
        continuation_token = continuation_token + 1

    return RpcEventsResult(events=events, continuation_token=str(continuation_token))


@validate_schema("getNonce")
async def get_nonce(block_id: BlockId, contract_address: Address) -> Felt:
    """
    Get the nonce associated with the given address in the given block
    """
    await assert_block_id_is_latest_or_pending(block_id)

    if not await state.starknet_wrapper.is_deployed(int(contract_address, 16)):
        raise RpcError(code=20, message="Contract not found")

    result = await state.starknet_wrapper.get_nonce(
        contract_address=int(contract_address, 16), block_id=block_id
    )

    return rpc_felt(result)
