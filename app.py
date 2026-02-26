import streamlit as st
import streamlit.components.v1 as components

# Set halaman full width
st.set_page_config(
    page_title="Dashboard DB Distribusi",
    layout="wide"
)

# Baca file HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render HTML ke Streamlit
components.html(
    html_content,
    height=1200,
    scrolling=True
)
