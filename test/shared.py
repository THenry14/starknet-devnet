"""Shared values between tests"""

ARTIFACTS_PATH = "test/artifacts/contracts/cairo"
CONTRACT_PATH = f"{ARTIFACTS_PATH}/contract.cairo/contract.json"
ABI_PATH = f"{ARTIFACTS_PATH}/contract.cairo/contract_abi.json"
STORAGE_CONTRACT_PATH = f"{ARTIFACTS_PATH}/storage.cairo/storage.json"
STORAGE_ABI_PATH = f"{ARTIFACTS_PATH}/storage.cairo/storage_abi.json"
EVENTS_CONTRACT_PATH = f"{ARTIFACTS_PATH}/events.cairo/events.json"
EVENTS_ABI_PATH = f"{ARTIFACTS_PATH}/events.cairo/events_abi.json"
FAILING_CONTRACT_PATH = f"{ARTIFACTS_PATH}/always_fail.cairo/always_fail.json"
DEPLOYER_CONTRACT_PATH = f"{ARTIFACTS_PATH}/deployer.cairo/deployer.json"
DEPLOYER_ABI_PATH = f"{ARTIFACTS_PATH}/deployer.cairo/deployer_abi.json"

BALANCE_KEY = (
    "916907772491729262376534102982219947830828984996257231353398618781993312401"
)

SIGNATURE = [
    "1225578735933442828068102633747590437426782890965066746429241472187377583468",
    "3568809569741913715045370357918125425757114920266578211811626257903121825123",
]

EXPECTED_SALTY_DEPLOY_ADDRESS = (
    "0x0273078f19eae2ad8aae94d1c0745fd3e7b758828c704e130cff0658a281f004"
)
EXPECTED_SALTY_DEPLOY_HASH = (
    "0x342d5cd9a280b81112518dc7afd9ae10e0ce484389aa0c2f626727498a51594"
)

EXPECTED_CLASS_HASH = (
    "0x18272236f94c858935851a7024eff968eea3af2b8ed2ad02c16917068f23866"
)

# This is temporary change.
EXPECTED_SALTY_DEPLOY_HASH_LITE_MODE = (
    "0x342d5cd9a280b81112518dc7afd9ae10e0ce484389aa0c2f626727498a51594"
)
EXPECTED_SALTY_DEPLOY_BLOCK_HASH_LITE_MODE = "0x1"

NONEXISTENT_TX_HASH = "0x1"
GENESIS_BLOCK_NUMBER = 0
GENESIS_BLOCK_HASH = "0x0"
INCORRECT_GENESIS_BLOCK_HASH = "0x1"
DEFAULT_GAS_PRICE = int(1e11)

SUPPORTED_TX_VERSION = 0

PREDEPLOYED_ACCOUNT_ADDRESS = (
    "0x347be35996a21f6bf0623e75dbce52baba918ad5ae8d83b6f416045ab22961a"
)
PREDEPLOYED_ACCOUNT_PRIVATE_KEY = 0xBDD640FB06671AD11C80317FA3B1799D

EXPECTED_FEE_TOKEN_ADDRESS = (
    "0x62230ea046a9a5fbc261ac77d03c8d41e5d442db2284587570ab46455fd2488"
)
EXPECTED_WALLET_ADDRESS = (
    "0x51743c6e5fd8c620107061292ebcad8becebc3ae57dda3c3064ece886216491"
)
