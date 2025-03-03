---
sidebar_position: 17
---
# Devnet speed-up troubleshooting

If you are not satisfied with Devnet's performance, consider the following:

- Make sure you are using the latest version of Devnet because new improvements are added regularly.
- Try using [lite-mode](lite-mode.md).
- If minting tokens, set the [lite parameter](mint-token.md#mint-lite).
- Using an [installed Devnet](./../intro.md#install) should be faster than [running it with Docker](run.md#run-with-docker).
- If you are [running Devnet with Docker](run.md#run-with-docker) on an ARM machine (e.g. M1), make sure you are using [the appropriate image tag](run.md#versions-and-tags)
- If Devnet has been running for some time, try restarting it (either by killing it or by using the [restart functionality](restart.md)).
- Keep in mind that:
  - The first transaction is always a bit slower due to lazy loading.
  - Tools you use for testing (e.g. [the Hardhat plugin](https://github.com/Shard-Labs/starknet-hardhat-plugin)) add their own overhead.
  - Bigger contracts are more time consuming.