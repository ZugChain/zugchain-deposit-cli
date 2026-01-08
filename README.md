# ZugChain Staking Deposit CLI

A command-line tool for generating [EIP-2335 format](https://eips.ethereum.org/EIPS/eip-2335) BLS12-381 keystores and `deposit_data*.json` files for ZugChain validator staking.

Based on the [ethereum/staking-deposit-cli](https://github.com/ethereum/staking-deposit-cli) which was audited by [Trail of Bits](https://github.com/trailofbits/publications/blob/master/reviews/ETH2DepositCLI.pdf).

> ⚠️ **Warning: Please generate your keystores on your own safe, completely offline device.**
>
> ⚠️ **Warning: Please backup your mnemonic, keystores, and password securely.**

---

## Quick Start

### Download Binary (Recommended)

Download the latest release for your operating system from the [Releases](https://github.com/ZugChain/deposit-cli/releases) page.

| Platform | File |
|----------|------|
| Windows | `zugchain-deposit-cli-windows-amd64.exe` |
| Linux | `zugchain-deposit-cli-linux-amd64` |
| macOS | `zugchain-deposit-cli-darwin-amd64` |

### Create New Validator Keys

```bash
# Windows
./deposit.exe new-mnemonic --num_validators=1

# Linux/macOS
./deposit new-mnemonic --num_validators=1
```

### Recover Keys from Existing Mnemonic

```bash
./zugchain-deposit-cli existing-mnemonic --num_validators=1 --validator_start_index=0
```

---

## Commands

| Command | Description |
|---------|-------------|
| `new-mnemonic` | Generate new validator keys with a fresh mnemonic |
| `existing-mnemonic` | Recover or generate additional keys from an existing mnemonic |
| `generate-bls-to-execution-change` | Create BLS to execution layer withdrawal credential change message |

---

## Arguments

### `new-mnemonic` Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `--num_validators` | Integer | Number of validators to create |
| `--mnemonic_language` | String | Language for mnemonic (default: English) |
| `--folder` | String | Output folder (default: ./validator_keys) |
| `--execution_address` | String | ETH1 withdrawal address (0x...) |

### `existing-mnemonic` Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `--num_validators` | Integer | Number of validators to create |
| `--validator_start_index` | Integer | Starting index for key derivation |
| `--folder` | String | Output folder (default: ./validator_keys) |
| `--execution_address` | String | ETH1 withdrawal address (0x...) |

---

## Build from Source

### Requirements
- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/ZugChain/deposit-cli.git
cd deposit-cli

# Install dependencies
pip install -r requirements.txt
python setup.py install
```

### Run from Source

```bash
python ./staking_deposit/deposit.py new-mnemonic
```

### Build Binary

```bash
# Install PyInstaller
pip install pyinstaller

# Windows
pyinstaller ./build_configs/windows/build.spec

# Linux
pyinstaller ./build_configs/linux/build.spec

# macOS
pyinstaller ./build_configs/macos/build.spec
```

Output will be in the `dist/` folder.

---

## Output Files

After running the tool, you'll find these files in `./validator_keys/`:

| File | Description |
|------|-------------|
| `keystore-m_*.json` | Encrypted validator signing keys (for beacon node) |
| `deposit_data-*.json` | Deposit data (for launchpad/smart contract) |

---

## Security Recommendations

1. **Run Offline**: Generate keys on an air-gapped machine
2. **Backup Mnemonic**: Write down your 24-word mnemonic on paper
3. **Secure Storage**: Store keystores and mnemonic in separate secure locations
4. **Verify Checksums**: Always verify downloaded binary checksums

---

## License

This project is licensed under the Creative Commons Zero v1.0 Universal License - see the [LICENSE](LICENSE) file for details.

---

## Support

- Website: [https://zugchain.io](https://zugchain.io)
- Discord: [ZugChain Discord](https://discord.gg/zugchain)
- Documentation: [https://docs.zugchain.io](https://docs.zugchain.io)
