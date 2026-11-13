# 🔐 CipherVault AI
### Your Files. Your Password. Your Control.

**A secure, password-based file protection platform powered by modern cryptography, with a vision for AI-assisted cybersecurity.**

<p align="center">

**AES-256-GCM · Argon2id · Python · Streamlit**

</p>

---

## 🚀 About the Project

Digital files contain personal information, confidential documents and sensitive data. Yet protecting individual files is often either unnecessarily complicated or dependent on tools that users don't fully understand.

**CipherVault AI** aims to make file protection simple, accessible and transparent.

It is a Python-based file encryption application that allows users to protect files using password-derived cryptographic keys and recover them when needed.

Instead of relying on a password alone as an encryption key, CipherVault uses **Argon2id for key derivation and AES-256-GCM for authenticated encryption**.

The result is a practical cybersecurity application built around three principles:

- **Confidentiality:** Keep file contents protected.
- **Integrity:** Detect unauthorized modification of encrypted data.
- **Usability:** Make secure file operations accessible through a simple interface.

---

## ✨ What Makes CipherVault Different?

CipherVault focuses on combining a straightforward user experience with meaningful cryptographic engineering.

| Capability | Implementation |
|---|---|
| Secure file encryption | AES-256-GCM |
| Password-based key derivation | Argon2id |
| Randomized encryption | Unique salt and nonce per operation |
| Data integrity | Authenticated encryption |
| File recovery | Password-based decryption |
| User interface | Streamlit web application |
| AI cybersecurity assistance | Local AI integration planned |

### Core Features

**🔒 1. Password-Protected File Encryption**

Encrypt uploaded files using a password-derived 256-bit key.

**🔑 2. Memory-Hard Key Derivation**

Argon2id derives encryption keys from passwords using configurable computational and memory costs.

**🔓 3. Secure File Recovery**

Decrypt previously encrypted files using the correct password.

**🛡️ 4. Tamper Detection**

AES-GCM authentication detects modified ciphertext or invalid authentication data.

**🖥️ 5. Interactive Web Interface**

A Streamlit-based interface provides separate encryption and decryption workflows.

**🤖 6. AI-Assisted Cybersecurity — Planned**

The project roadmap includes a local AI assistant designed to explain encryption concepts and answer general cybersecurity questions without requiring a paid external API.

---

## ⚙️ How CipherVault Works

<details>
<summary><b>Encryption workflow</b></summary>

1. The user selects a file.
2. The user enters an encryption password.
3. CipherVault generates a cryptographically random salt.
4. Argon2id derives a 256-bit encryption key.
5. A random 96-bit nonce is generated.
6. AES-256-GCM encrypts and authenticates the file.
7. The encrypted output is made available for download.

</details>

<details>
<summary><b>Decryption workflow</b></summary>

1. The user uploads a previously encrypted file.
2. The original password is entered.
3. CipherVault extracts the stored salt and nonce.
4. Argon2id derives the corresponding encryption key.
5. AES-256-GCM verifies the authentication tag.
6. If authentication succeeds, the original file is recovered.
7. If the password is incorrect or the encrypted data has been modified, decryption fails.

</details>

---

## 🧬 Security Architecture

CipherVault is built around established cryptographic primitives rather than custom encryption algorithms.

### 1. AES-256-GCM — Authenticated Encryption

- Uses a 256-bit encryption key.
- Provides confidentiality through authenticated encryption.
- Generates an authentication tag to detect unauthorized changes.
- Uses a 96-bit nonce for each encryption operation.

### 2. Argon2id — Password-Based Key Derivation

- Designed to make password guessing more expensive.
- Uses a random salt to prevent identical passwords from producing identical derived keys.
- Applies configurable memory and computational costs.
- Derives a cryptographic key rather than using the raw password directly.

### 3. Security Design Principles

- Cryptographically secure random generation.
- Separate salt and nonce for each encryption operation.
- Authentication verification during decryption.
- No intentional storage of plaintext passwords.
- Environment files and virtual environments excluded from Git tracking.

**Important:** Encryption protects the contents of a file, but it does not automatically protect filenames, backups, passwords or an already compromised device.

---

## 🏗️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive application interface |
| Cryptography | AES-256-GCM encryption |
| Argon2-CFFI | Argon2id key derivation |
| Git & GitHub | Version control and project hosting |
| Local AI runtime | Planned cybersecurity assistant |

---

## 📂 Project Architecture

```text
CipherVault-AI/
│
├── app.py                 # Streamlit application
│
├── crypto_engine.py       # Encryption and key derivation
├── file_manager.py        # File encryption and recovery
├── ai_assistant.py        # AI assistant integration
│
├── test_crypto.py         # Cryptography tests
├── test_files.py          # File operation tests
│
├── samples/               # Sample test files
│
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🧪 Testing & Reliability

Security-related functionality must be tested, not merely demonstrated.

The current project includes tests covering:

| Test | Expected behaviour |
|---|---|
| Valid encryption | Produces encrypted output |
| Valid decryption | Recovers original content |
| Incorrect password | Rejects decryption |
| Modified ciphertext | Authentication fails |
| File round-trip | Recovered file matches original |

### Run the tests

```bash
python test_crypto.py
python test_files.py
```

These tests cover core functionality; they are not a substitute for an independent security audit.

---

## 💻 Getting Started

### Requirements

- Python 3.10 or newer
- Git
- Windows, macOS or Linux

### 1. Clone the repository

```bash
git clone https://github.com/Soumili-codes/CipherVault-AI.git
```

### 2. Navigate to the project

```bash
cd CipherVault-AI
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate it

**Windows PowerShell
