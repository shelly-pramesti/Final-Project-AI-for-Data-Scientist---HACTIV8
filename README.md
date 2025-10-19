# Gemini AI Chatbot
## Bootcamp Final Project

### Overview
This is a web-based chatbot built with Streamlit and Google's Gemini 2.5 Flash AI model. Users can type questions or prompts in a clean chat interface, view conversation history, and clear the chat with a button. The chatbot uses the Gemini API to generate smart, fast responses, making it a fun and interactive tool for learning and exploration.

### How to Run
Follow these steps to set up and run the chatbot locally:

1. **Install Miniconda**:
   - Download and install Miniconda from [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html).
   - Create a new environment: `conda create -n gemini-chatbot python=3.11`
   - Activate the environment: `conda activate gemini-chatbot`

2. **Install Dependencies**:
   - Run: `pip install streamlit google-generativeai`

3. **Set Up the API Key**:
   - Get a Gemini API key from [https://aistudio.google.com/](https://aistudio.google.com/).
   - Open `app.py` and replace `"YOUR_API_KEY_HERE"` with your actual key.

4. **Run the App**:
   - In your project folder (e.g., `C:\gemini-chatbot`), run: `streamlit run app.py`
   - Open your browser to `http://localhost:8501`.

### Features
- **Interactive Chat Interface**: Users can type messages and get responses from Gemini AI.
- **Conversation History**: Displays all messages without duplicates.
- **Clear Chat Button**: Resets the conversation for a fresh start.
- **Error Handling**: Shows user-friendly messages if the API fails (e.g., rate limits).
- **Styling**: Blue, centered title and clean layout for a professional look.

### Screenshot
![Chatbot Interface](chatbot_screenshot.png)

### Challenges Overcome
- Fixed duplicate user messages by streamlining the Streamlit display logic.
- Updated from the deprecated `gemini-1.5-flash` model to `gemini-2.5-flash`.
- Resolved a Streamlit error by replacing `st.experimental_rerun` with `st.rerun` for newer versions.
- Learned to use Miniconda, Streamlit, and the Gemini API as a beginner in Python.

### Technologies Used
- Python 3.11
- Streamlit
- Google Gemini 2.5 Flash API
- Miniconda
- Visual Studio Code

### Author
[Shelly Pramesti] – Created for [AI for Data Scientist - HACTIV8] Final Project, October 2025.

### Notes
- The API key in `app.py` has been removed for security (`"YOUR_API_KEY_HERE"` placeholder).
- For live demo, contact me to run locally, or deploy via Streamlit Cloud using the GitHub repo: [https://github.com/yourusername/gemini-chatbot-project](https://github.com/yourusername/gemini-chatbot-project).
