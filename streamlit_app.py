import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Aura AI", page_icon="🤖")

st.title("🤖 Aura AI")
st.caption("Your friendly AI assistant with voice input & file upload.")

# Logo
if os.path.exists("logo.png"):
    st.image("logo.png", width=200)

# Input
query = st.text_input("Ask anything...")
if st.button("Submit"):
    st.write("✨ Aura says:", query[::-1])  # Placeholder response

# File upload
file = st.file_uploader("Upload a file (PDF or image)")
if file:
    st.success(f"{file.name} uploaded!")

# Voice input (simulated)
st.text("🎙️ Click mic to use voice (feature coming soon)")
