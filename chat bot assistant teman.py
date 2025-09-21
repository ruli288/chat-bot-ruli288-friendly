import streamlit as st
from openai import OpenAI

# Inisialisasi client OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Fungsi chatbot dengan persona "teman ngobrol santai"
def chatbot_response(user_input):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # bisa pakai gpt-4 kalau punya akses
        messages=[
            {"role": "system", "content": "Kamu adalah teman ngobrol santai yang ramah, suka bercanda ringan, dan tidak terlalu formal."},
            {"role": "user", "content": user_input}
        ],
        temperature=0.9,  # lebih tinggi biar jawabannya kreatif & cair
        max_tokens=300
    )
    return response.choices[0].message.content

# Konfigurasi Streamlit
st.set_page_config(page_title="Teman Ngobrol Santai 🤗", page_icon="💬")

st.title("💬 Chatbot: Teman Ngobrol Santai")
st.write("Halo! Aku siap nemenin kamu ngobrol santai. Cerita apa aja bebas 😉")

# Simpan riwayat chat
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
st.subheader("💬 Obrolan")
for sender, message in st.session_state.chat_history:
    if sender == "Kamu":
        st.markdown(f"**🧑 {sender}:** {message}")
    else:
        st.markdown(f"**🤖 {sender}:** {message}")
