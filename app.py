import streamlit as st
from translator import translate_text
from googletrans import LANGUAGES

# Set page config for dark theme and title
st.set_page_config(page_title="Language Translator", page_icon="🌍", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for attractive and colorful design
st.markdown("""
<style>
    .main {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    .stTextArea textarea {
        background-color: #2d2d2d;
        color: #ffffff;
        border: 2px solid #4CAF50;
        border-radius: 10px;
    }
    .stSelectbox select {
        background-color: #2d2d2d;
        color: #ffffff;
        border: 2px solid #2196F3;
        border-radius: 10px;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stSuccess {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 10px;
    }
    .stError {
        background-color: #f44336;
        color: white;
        border-radius: 10px;
        padding: 10px;
    }
    .title {
        color: #FFD700;
        text-align: center;
        font-size: 3em;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .subtitle {
        color: #FFA500;
        text-align: center;
        font-size: 1.2em;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown('<h1 class="title">🌍 Language Translator</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Translate English text to any language instantly!</p>', unsafe_allow_html=True)

# Create two columns for layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📝 Enter Text")
    input_text = st.text_area("Enter English text to translate:", height=150, key="input")

with col2:
    st.markdown("### 🌐 Select Language")
    languages = {code: name.title() for code, name in LANGUAGES.items()}
    target_lang = st.selectbox("Choose target language:", options=list(languages.keys()), format_func=lambda x: languages[x], key="lang")

# Translate button
st.markdown("### 🚀 Translate")
if st.button("Translate Now!", key="translate"):
    if input_text.strip():
        with st.spinner("Translating..."):
            translated = translate_text(input_text, target_lang)
        st.success("✅ Translation Complete!")
        st.markdown("### 📋 Translated Text:")
        st.info(translated)
    else:
        st.error("❌ Please enter some text to translate.")
