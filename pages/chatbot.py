import streamlit as st
import ollama

## Ensure session state is initialized
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Khamma Ghani! I am JT, your Jaipur guide. Ask me anything about the Pink City!"}
    ]

## Generator for Streaming Responses
def generate_response():
    response = ollama.chat(model='llama2', stream=True, messages=st.session_state.messages)
    for partial_resp in response:
        token = partial_resp["message"]["content"]
        st.session_state["full_message"] += token
        yield token

def app():
    st.title("Khamma Ghani! I am JT 👋")
    
    # Display Chat History
    for msg in st.session_state.messages:
        role = "user" if msg["role"] == "user" else "assistant"
        avatar = "🧑‍💻" if msg["role"] == "user" else "🤖"
        st.chat_message(role, avatar=avatar).write(msg["content"])
    
    # User Input Handling
    if prompt := st.chat_input("Ask me about Jaipur..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user", avatar="🧑‍💻").write(prompt)

        st.session_state["full_message"] = ""
        st.chat_message("assistant", avatar="🤖").write_stream(generate_response)

        st.session_state.messages.append({"role": "assistant", "content": st.session_state["full_message"]})   

    # Sidebar About Section
    with st.sidebar:
        st.header("About JT")
        st.markdown("JT is an intelligent chatbot that understands commands. It can help with your queries about Jaipur!")

