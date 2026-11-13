
import streamlit as st
from crypto_engine import encrypt_data, decrypt_data

st.set_page_config(
    page_title="CipherVault AI",
    page_icon="🔐"
)

st.markdown("""
<div style="padding: 22px 0 15px 0;">
    <h1 style="font-size: 38px; margin-bottom: 5px;">
        🔐 CipherVault AI
    </h1>
    <p style="font-size: 16px; color: #8db8ed;">
        Intelligent File Protection • Secure Encryption • Cybersecurity
    </p>
</div>
""", unsafe_allow_html=True)
st.markdown("### 🛡️ Security Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Encryption", "AES-256-GCM")

with col2:
    st.metric("Key Derivation", "Argon2id")

with col3:
    st.metric("Protection", "Enabled")
    st.divider()

st.markdown("""
### 📁 Secure File Workspace
Upload your file, protect it with encryption,
or recover it using your password.
""")
st.subheader("AI-Powered Encrypted File Locker")

st.write("Secure your files using AES-256-GCM encryption.")

encrypt_tab, decrypt_tab = st.tabs(
    ["Encrypt File", "Decrypt File"]
)

# ENCRYPTION SECTION

with encrypt_tab:
    st.header("Encrypt Your File")

    uploaded_file = st.file_uploader(
        "Choose a file",
        key="encrypt_file"
    )

    password = st.text_input(
        "Create password",
        type="password",
        key="encrypt_password"
    )

    if st.button("Encrypt File"):

        if uploaded_file is None:
            st.error("Please upload a file.")

        elif not password:
            st.error("Please enter a password.")

        elif len(uploaded_file.getvalue()) > 10 * 1024 * 1024:
            st.error("Maximum file size is 10 MB.")

        else:
            try:
                encrypted = encrypt_data(
                    uploaded_file.getvalue(),
                    password
                )

                st.success("Encryption successful!")

                st.download_button(
                    "Download Encrypted File",
                    data=encrypted,
                    file_name=uploaded_file.name + ".cvault",
                    mime="application/octet-stream"
                )

            except Exception:
                st.error("Encryption failed.")

# DECRYPTION SECTION

with decrypt_tab:
    st.header("Decrypt Your File")

    encrypted_file = st.file_uploader(
        "Upload encrypted file",
        type=["cvault"],
        key="decrypt_file"
    )

    decrypt_password = st.text_input(
        "Enter password",
        type="password",
        key="decrypt_password"
    )

    if st.button("Decrypt File"):

        if encrypted_file is None:
            st.error("Please upload an encrypted file.")

        elif not decrypt_password:
            st.error("Please enter your password.")

        else:
            try:
                decrypted = decrypt_data(
                    encrypted_file.getvalue(),
                    decrypt_password
                )

                st.success("Decryption successful!")

                original_name = encrypted_file.name.removesuffix(
                    ".cvault"
                )

                st.download_button(
                    "Download Decrypted File",
                    data=decrypted,
                    file_name=original_name,
                    mime="application/octet-stream"
                )

            except Exception:
                st.error(
                    "Wrong password or invalid encrypted file."
                )

from ai_assistant import ask_ai

st.divider()
st.header("🤖 CipherVault AI Assistant")
st.write("Ask questions about encryption and cybersecurity.")

question = st.text_input(
    "Enter your cybersecurity question:"
)

if st.button("Ask AI"):
    if question.strip():
        with st.spinner("Thinking..."):
            try:
                answer = ask_ai(question)
                st.write(answer)
            except Exception as e:
                st.error(f"AI Error: {e}")
    else:
        st.warning("Please enter a question.")

# ---------- PROFESSIONAL UI THEME ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #07111f, #101d33);
    color: #eaf2ff;
}

h1, h2, h3 {
    color: #eaf2ff !important;
}

p, label {
    color: #c5d5eb;
}

.stButton > button {
    background: linear-gradient(90deg, #1769ff, #00b8d9);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 22px;
    font-weight: 600;
}

.stButton > button:hover {
    background: #0057d9;
    color: white;
    border: none;
}

.stTextInput input, .stTextArea textarea {
    background-color: #17263d;
    color: white;
    border: 1px solid #345071;
    border-radius: 9px;
}

[data-testid="stFileUploader"] {
    background: #14243a;
    border: 1px dashed #3984ff;
    border-radius: 12px;
    padding: 12px;
}

[data-testid="stMetric"] {
    background: #14243a;
    border: 1px solid #29415f;
    padding: 16px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)
