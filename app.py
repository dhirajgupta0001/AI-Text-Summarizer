import streamlit as st
import requests

st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📝",
    layout="centered"
)

st.title("📝 AI Text Summarizer")
st.write("Summarize long text using AI.")

text = st.text_area(
    "Enter your text",
    height=250,
    placeholder="Paste your text here..."
)

length = st.selectbox(
    "Summary length",
    ["short", "medium", "detailed"]
)

if st.button("Summarize"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Generating summary..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/summarize",
                    json={
                        "text": text,
                        "length": length
                    },
                    timeout=120
                )
                response.raise_for_status()
                summary = response.json()["summary"]

                st.subheader("Summary")
                st.write(summary)

            except requests.RequestException as e:
                st.error(f"API request failed: {e}")
