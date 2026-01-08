from typing import Dict, NamedTuple
from eth_utils import decode_hex

DEPOSIT_CLI_VERSION = '1.0.0'


class BaseChainSetting(NamedTuple):
    NETWORK_NAME: str
    GENESIS_FORK_VERSION: bytes
    GENESIS_VALIDATORS_ROOT: bytes


# ZugChain Settings
ZUGCHAIN = 'zugchain'

# ZugChain Mainnet Setting
# GENESIS_FORK_VERSION: 0x20000000 (matches beacon chain config)
# GENESIS_VALIDATORS_ROOT: Will be updated after genesis, using zeros for pre-genesis
ZugChainSetting = BaseChainSetting(
    NETWORK_NAME=ZUGCHAIN,
    GENESIS_FORK_VERSION=bytes.fromhex('20000000'),
    GENESIS_VALIDATORS_ROOT=bytes(32),  # Pre-genesis: all zeros
)


ALL_CHAINS: Dict[str, BaseChainSetting] = {
    ZUGCHAIN: ZugChainSetting,
}


def get_chain_setting(chain_name: str = ZUGCHAIN) -> BaseChainSetting:
    return ALL_CHAINS[chain_name]


def get_devnet_chain_setting(network_name: str,
                             genesis_fork_version: str,
                             genesis_validator_root: str) -> BaseChainSetting:
    return BaseChainSetting(
        NETWORK_NAME=network_name,
        GENESIS_FORK_VERSION=decode_hex(genesis_fork_version),
        GENESIS_VALIDATORS_ROOT=decode_hex(genesis_validator_root),
    )

