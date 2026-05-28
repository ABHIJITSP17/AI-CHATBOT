import streamlit as st
from chatbot import get_response
from memory import Memory
from config import APP_TITLE, APP_ICON

# ── Page Setup ────────────────────────────────────
st.set_page_config(page_title=APP_TITLE, page_icon=APP_ICON)
st.title(f"{APP_ICON} {APP_TITLE}")

# ── Initialize Memory ─────────────────────────────
if "memory" not in st.session_state:
    st.session_state.memory = Memory()

# ── Display Chat History ──────────────────────────
for msg in st.session_state.memory.get():
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ── Chat Input Box ────────────────────────────────
user_input = st.chat_input("Ask me anything...")

if user_input:
    # Show user message
    with st.chat_message("user"):
        st.write(user_input)

    # Add to memory
    st.session_state.memory.add("user", user_input)

    # Get bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply = get_response(st.session_state.memory.get())
            st.write(reply)

    # Add bot reply to memory
    st.session_state.memory.add("assistant", reply)