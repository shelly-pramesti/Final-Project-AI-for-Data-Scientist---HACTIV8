import streamlit as st
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyDP5uvxNy6j8wmeUBWE8-ecrMr8NsNRYQ8")  # Replace with your actual Gemini API key

# Set up the model
model = genai.GenerativeModel('gemini-2.5-flash')

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Page title and styling
st.title("Chatbot Lite")
st.markdown("<style>h1 {color: #2e86c1; text-align: center;} .stChatMessage {margin-bottom: 10px;}</style>", unsafe_allow_html=True)
st.markdown("Welcome to Chatbot Lite! Ask me anything, and I'll respond using Gemini AI.")

# Clear chat history button
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Generate and display assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(prompt)
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Oops, something went wrong: {str(e)}")
                response_text = f"Error: {str(e)}"
            else:
                response_text = response.text
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": response_text})
    # Refresh to update chat history
    st.rerun()