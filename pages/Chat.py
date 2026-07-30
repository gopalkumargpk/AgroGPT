import streamlit as st
from src.rag_pipeline import ask_question

st.set_page_config(
    page_title="AgroGPT Chat",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 AgroGPT")
st.subheader("AI Agriculture Assistant")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask anything about agriculture..."):

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = ask_question(prompt)
            st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )