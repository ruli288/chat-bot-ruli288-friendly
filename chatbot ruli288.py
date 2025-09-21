import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from streamlit_option_menu import option_menu

from google import genai  # For interacting with the Google Gemini API
# Inisialisasi ChatBot (hanya sekali, tidak setiap rerun)
@st.cache_resource

# --- 1. API Key and Client Initialization ---

# Check if the user has provided an API key.
# If not, display an informational message and stop the app from running further.
if not google_api_key:
    st.info("Please add your Google AI API key in the sidebar to start chatting.", icon="🗝️")
    st.stop()

# This block of code handles the creation of the Gemini API client.
# It's designed to be efficient: it only creates a new client if one doesn't exist
# or if the user has changed the API key in the sidebar.

# We use `st.session_state` which is Streamlit's way of "remembering" variables
# between user interactions (like sending a message or clicking a button).

# Condition 1: "genai_client" not in st.session_state
# Checks if we have *never* created the client before.
#
# Condition 2: getattr(st.session_state, "_last_key", None) != google_api_key
# This is a safe way to check if the current API key is different from the last one we used.
# `getattr(object, 'attribute_name', default_value)` tries to get an attribute from an object.
# If the attribute doesn't exist, it returns the default value (in this case, `None`).
# So, it checks: "Is the key stored in memory different from the one in the input box?"
if ("genai_client" not in st.session_state) or (getattr(st.session_state, "_last_key", None) != google_api_key):
    try:
        # If the conditions are met, create a new client.
        st.session_state.genai_client = genai.Client(api_key=google_api_key)
        # Store the new key in session state to compare against later.
        st.session_state._last_key = google_api_key
        # Since the key changed, we must clear the old chat and message history.
        # .pop() safely removes an item from session_state.
        st.session_state.pop("chat", None)
        st.session_state.pop("messages", None)
    except Exception as e:
        # If the key is invalid, show an error and stop.
        st.error(f"Invalid API Key: {e}")
        st.stop()


# --- 2. Chat History Management ---

# Initialize the chat session if it doesn't already exist in memory.
if "chat" not in st.session_state:
    # Create a new chat instance using the 'gemini-2.5-flash' model.
    st.session_state.chat = st.session_state.genai_client.chats.create(model="gemini-2.5-flash")

# Initialize the message history (as a list) if it doesn't exist.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Handle the reset button click.
if reset_button:
    # If the reset button is clicked, clear the chat object and message history from memory.
    st.session_state.pop("chat", None)
    st.session_state.pop("messages", None)
    # st.rerun() tells Streamlit to refresh the page from the top.
    st.rerun()

# --- 3. Display Past Messages ---

# Loop through every message currently stored in the session state.
for msg in st.session_state.messages:
    # For each message, create a chat message bubble with the appropriate role ("user" or "assistant").
    with st.chat_message(msg["role"]):
        # Display the content of the message using Markdown for nice formatting.
        st.markdown(msg["content"])

# --- 4. Handle User Input and API Communication ---

# Create a chat input box at the bottom of the page.
# The user's typed message will be stored in the 'prompt' variable.
prompt = st.chat_input("Type your message here...")

# Check if the user has entered a message.
if prompt:
    # 1. Add the user's message to our message history list.
    st.session_state.messages.append({"role": "user", "content": prompt})
    # 2. Display the user's message on the screen immediately for a responsive feel.
    with st.chat_message("user"):
        st.markdown(prompt)

    # 3. Get the assistant's response.
    # Use a 'try...except' block to gracefully handle potential errors (e.g., network issues, API errors).
    try:
        # Send the user's prompt to the Gemini API.
        response = st.session_state.chat.send_message(prompt)
        
        # Safely get the text from the response object.
        # `hasattr(object, 'attribute_name')` checks if an object has a specific property.
        # This prevents an error if the API response object doesn't have a '.text' attribute.
        if hasattr(response, "text"):
            answer = response.text
        else:
            # If there's no '.text', convert the whole response to a string as a fallback.
            answer = str(response)

    except Exception as e:
        # If any error occurs, create an error message to display to the user.
        answer = f"An error occurred: {e}"

    # 4. Display the assistant's response.
    with st.chat_message("assistant"):
        st.markdown(answer)
    # 5. Add the assistant's response to the message history list.
    st.session_state.messages.append({"role": "assistant", "content": answer})
def load_bot():
    bot = ChatBot('ChatBot Ruli288')
    trainer = ChatterBotCorpusTrainer(bot)
    try:
        trainer.train("chatterbot.corpus.indonesian")
    except Exception:
        pass  # Agar tidak duplikasi training
    return bot

bot = load_bot()

# Custom CSS untuk memperindah UI
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #b3ffab 0%, #12fff7 100%);
    }
    .chat-bubble {
        padding: 10px 15px; margin: 10px 0; border-radius: 15px; max-width: 70%;
        display: inline-block; font-size: 16px;
    }
    .user {background: #fff; color: #222; align-self: flex-end;}
    .bot {background: #0f2027; color: #fff; align-self: flex-start;}
    .chat-container {display: flex; flex-direction: column;}
    </style>
""", unsafe_allow_html=True)

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        "Menu", ["Chat", "Tentang"], 
        icons=["chat-dots", "info-circle"], 
        menu_icon="robot", default_index=0
    )

st.title("🤖 ChatBot Ruli288")
st.caption("Chatbot sederhana dengan antarmuka cantik menggunakan Streamlit")

if selected == "Chat":
    if "history" not in st.session_state:
        st.session_state.history = []

    user_input = st.text_input("Ketik pesan Anda...", key="input")

    if st.button("Kirim") and user_input:
        response = bot.get_response(user_input)
        st.session_state.history.append(("Anda", user_input))
        st.session_state.history.append(("ChatBot Ruli288", str(response)))
        st.experimental_rerun()

    # Tampilkan riwayat chat
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for speaker, message in st.session_state.history:
        role = "user" if speaker == "Anda" else "bot"
        st.markdown(
            f'<div class="chat-bubble {role}"><b>{speaker}:</b> {message}</div>',
            unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Tentang":
    st.subheader("Tentang ChatBot Ruli288")
    st.write("""
    ChatBot Ruli288 adalah chatbot sederhana yang dibangun dengan Python, Streamlit, dan ChatterBot.
    Dikembangkan oleh **ruli288**.
    """)

    st.write("Source code: [GitHub](https://github.com/ruli288/chat-bot-ruli288-friendly)")
