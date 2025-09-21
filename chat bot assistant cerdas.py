import streamlit as st
from openai import OpenAI

# Inisialisasi client OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Fungsi chatbot dengan OpenAI
def chatbot_response(user_input):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # bisa diganti ke gpt-4 jika punya akses
        messages=[
            {"role": "system", "content": "Kamu adalah asisten AI yang ramah dan membantu."},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7,
        max_tokens=300
    )
    return response.choices[0].message.content

# Konfigurasi Streamlit
st.set_page_config(page_title="AI Assistant Chatbot", page_icon="🤖")

st.title("🤖 Chatbot AI Assistant")
st.write("Selamat datang! Silakan ngobrol dengan asisten AI ini.")

# Simpan riwayat chat di session_state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input user
user_input = st.text_input("Ketik pesanmu:")

if st.button("Kirim") and user_input:
    response = chatbot_response(user_input)

    # Simpan ke riwayat chat
    st.session_state.chat_history.append(("Kamu", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Tampilkan riwayat chat
st.subheader("💬 Riwayat Chat")
for sender, message in st.session_state.chat_history:
    if sender == "Kamu":
        st.markdown(f"**🧑 {sender}:** {message}")
    else:
        st.markdown(f"**🤖 {sender}:** {message}")
