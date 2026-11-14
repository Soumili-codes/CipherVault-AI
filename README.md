# 🔐 CipherVault AI

<h3 align="center">SECURE YOUR FILES. PROTECT YOUR PRIVACY.</h3>

<p align="center">
  <strong>A modern password-based file encryption platform powered by strong cryptographic techniques.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-Framework-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/AES--256--GCM-Encryption-00A86B?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Argon2id-Key%20Derivation-7B42BC?style=for-the-badge" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Working%20Prototype-success?style=flat-square" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" />
  <img src="https://img.shields.io/badge/Focus-Cybersecurity-blueviolet?style=flat-square" />
</p>

---

## 🌌 01. About the Project

**CipherVault AI** is a Python-based file encryption application designed to make digital file protection simple and accessible.

It combines authenticated encryption, password-based key derivation, and a user-friendly interface to help users protect sensitive digital information.

Users can encrypt files, download encrypted versions, and recover their original files using the correct password.

### 🎯 The Mission

Make strong file encryption easier to understand and use without requiring advanced cybersecurity knowledge.

---

## 🚨 02. The Problem

Digital files often contain sensitive personal, academic, and professional information.

Without appropriate protection, these files may be exposed to unauthorized access.

Traditional encryption tools can also be difficult for beginners to understand.

### 💡 Our Approach

CipherVault AI provides a straightforward workflow:

- Select a file.
- Enter a password.
- Encrypt the file.
- Download the protected output.
- Decrypt it whenever needed using the correct password.

---

## ✨ 03. Core Features

| Feature | Description |
| --- | --- |
| 🔐 AES-256-GCM | Authenticated file encryption |
| 🛡️ Argon2id | Password-based cryptographic key derivation |
| 🔑 Password Protection | Password required for decryption |
| 🧩 Tampering Detection | Authentication verification |
| 📁 File Management | Upload, encrypt, decrypt and download |
| 🖥️ Streamlit UI | Simple interactive application |

---

## 🏗️ 04. System Architecture

The application follows a modular architecture that separates the user interface, file handling, and cryptographic operations.

``` mermaid
flowchart TD
    A["👤 User"] --> B["🖥️ Streamlit Interface"]
    B --> C["📁 File Manager"]
    C --> D["🔐 Crypto Engine"]
    D --> E["🧂 Random Salt"]
    E --> F["Argon2id Key Derivation"]
    F --> G["🔑 256-bit Encryption Key"]
    G --> H["AES-256-GCM"]
    H --> I["🔒 Encrypted File"]
    I --> J["📥 Download"]
```

### Architecture Components

- **app.py:** Handles the Streamlit user interface.
- **file\_manager.py:** Manages file encryption and decryption operations.
- **crypto\_engine.py:** Implements cryptographic operations.
- **ai\_assistant.py:** Contains the experimental AI assistant integration.

---

## 🔬 05. Cryptographic Architecture

CipherVault AI uses two important cryptographic technologies.

### AES-256-GCM

AES-GCM provides authenticated encryption, protecting both file confidentiality and integrity.

### Argon2id

Argon2id derives a cryptographic key from the user's password using configurable computational and memory costs.

### Encryption Workflow

``` mermaid
flowchart TD
    A["📄 Original File"] --> B["🔑 User Password"]
    B --> C["🧂 Generate Random Salt"]
    C --> D["Argon2id"]
    D --> E["32-byte Encryption Key"]
    E --> F["AES-256-GCM"]
    A --> F
    F --> G["🔒 Encrypted Data"]
    G --> H["📦 Store Salt + Nonce + Ciphertext"]
```

### Decryption Workflow

``` mermaid
flowchart TD
    A["🔒 Encrypted File"] --> B["Extract Salt and Nonce"]
    B --> C["Enter Original Password"]
    C --> D["Argon2id"]
    D --> E["Reconstruct Encryption Key"]
    E --> F["AES-256-GCM Authentication"]
    F --> G{"Authentication Successful?"}
    G -->|Yes| H["📄 Recover Original File"]
    G -->|No| I["❌ Reject Decryption"]
```

**Security considerations:** Random salts and nonces are used. Authentication must succeed before decrypted content is accepted. Users should keep their passwords secure because forgotten passwords cannot be recovered by the application.

---

## 🛠️ 06. Technology Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,vscode,github,git" />
</p>

| Technology | Purpose |
| --- | --- |
| Python | Core application logic |
| Streamlit | Web interface |
| Cryptography | AES-GCM implementation |
| Argon2-cffi | Password-based key derivation |
| Git | Version control |
| GitHub | Source code hosting |

---

## 📂 07. Project Structure

``` text
CipherVault-AI/
│
├── app.py
│
├── crypto_engine.py
│
├── file_manager.py
│
├── ai_assistant.py
│
├── test_crypto.py
│
├── test_files.py
│
├── requirements.txt
│
├── README.md
│
├── .gitignore
│
└── samples/
```

---

## 🚀 08. Installation \& Setup

### Prerequisites

- Python installed
- Git installed
- Visual Studio Code (recommended)

### Step 1 — Clone Repository

``` bash
git clone https://github.com/Soumili-codes/CipherVault-AI.git
```

``` bash
cd CipherVault-AI
```

### Step 2 — Create Virtual Environment

``` bash
python -m venv .venv
```

Activate on Windows:

``` powershell
.venv\Scripts\activate
```

### Step 3 — Install Dependencies

``` bash
pip install streamlit cryptography argon2-cffi
```

### Step 4 — Launch Application

``` bash
streamlit run app.py
```

Open the local URL displayed in the terminal.

---

## 🧪 09. Testing \& Validation

The project has been tested for:

- Successful file encryption.
- Successful file decryption.
- Original file recovery.
- Incorrect password rejection.
- Encrypted data tampering detection.

The encryption and file-handling tests completed successfully during development.

---

## 🤖 10. AI Development Status

An AI cybersecurity assistant was explored as part of the project concept.

Gemini API integration was investigated, but API access and billing limitations prevented completion of a working AI model integration.

The current prototype focuses on tested file encryption and decryption functionality. AI-powered assistance remains a future development objective.

---

## 🔮 11. Future Roadmap

- [ ] Working AI-powered cybersecurity assistant.
- [ ] File integrity and security reporting.
- [ ] Improved file management.
- [ ] Additional file format support.
- [ ] Enhanced user experience.
- [ ] Expanded security testing.

---

## 👩‍💻 12. Developer

<p align="center">
  <strong>SOUMILI SAIN</strong>
  <br/>
  Student Developer | Cybersecurity Enthusiast
  <br/><br/>
  <a href="https://github.com/Soumili-codes">
    <img src="https://img.shields.io/badge/GitHub-Soumili--codes-181717?style=for-the-badge&logo=github" />
  </a>
</p>

---

## 📜 License

This project is licensed under the MIT License.

---

<p align="center">
  <h3 align="center">🔐 CipherVault AI</h3>
  <strong>Privacy is not a luxury. It is a necessity.</strong>
</p>
