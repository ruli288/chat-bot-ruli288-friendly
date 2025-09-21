import streamlit as st
import random
import time

# Judul Aplikasi
st.title("🤖 Chatbot Sederhana")

# Inisialisasi riwayat obrolan
# 'st.session_state' adalah variabel yang persisten antar-rerun
if "messages" not in st.session_state:
    st.session_state.messages = []

# Menampilkan pesan-pesan sebelumnya dari riwayat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Menerima input dari pengguna
if prompt := st.chat_input("Apa kabarmu?"):
    # Tambahkan pesan pengguna ke riwayat
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Tampilkan pesan pengguna
    with st.chat_message("user"):
        st.markdown(prompt)

    # Buat dan tampilkan respons dari asisten (bot)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        # Contoh respons sederhana dari bot
        list_jawaban = [
            "Halo! Ada yang bisa saya bantu?",
            "Hai, senang bertemu denganmu!",
            "Saya adalah chatbot sederhana. Tanyakan sesuatu padaku.",
            "Maaf, saya tidak mengerti. Bisa coba lagi?",
        ]
        assistant_response = random.choice(list_jawaban)
        
        # Efek mengetik untuk respons
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    
    # Tambahkan respons bot ke riwayat
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    Tentu, saya akan bantu jelaskan cara membangun chatbot Streamlit dengan Python, lengkap dengan beberapa ide chatbot yang menarik dan tips untuk mempercantik tampilannya.

Dasar-Dasar Membangun Chatbot dengan Streamlit
Streamlit adalah framework Python yang luar biasa untuk membuat aplikasi web interaktif dengan cepat, termasuk chatbot. Konsep dasarnya sederhana: aplikasi dijalankan dari atas ke bawah setiap kali pengguna berinteraksi. Untuk chatbot, kita perlu cara untuk "mengingat" percakapan sebelumnya. Di sinilah Session State Streamlit berperan.

Berikut adalah kerangka kode dasar untuk chatbot sederhana di Streamlit:

Python

import streamlit as st
import random
import time

# Judul Aplikasi
st.title("🤖 Chatbot Sederhana")

# Inisialisasi riwayat obrolan
# 'st.session_state' adalah variabel yang persisten antar-rerun
if "messages" not in st.session_state:
    st.session_state.messages = []

# Menampilkan pesan-pesan sebelumnya dari riwayat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Menerima input dari pengguna
if prompt := st.chat_input("Apa kabarmu?"):
    # Tambahkan pesan pengguna ke riwayat
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Tampilkan pesan pengguna
    with st.chat_message("user"):
        st.markdown(prompt)

    # Buat dan tampilkan respons dari asisten (bot)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        # Contoh respons sederhana dari bot
        list_jawaban = [
            "Halo! Ada yang bisa saya bantu?",
            "Hai, senang bertemu denganmu!",
            "Saya adalah chatbot sederhana. Tanyakan sesuatu padaku.",
            "Maaf, saya tidak mengerti. Bisa coba lagi?",
        ]
        assistant_response = random.choice(list_jawaban)
        
        # Efek mengetik untuk respons
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    
    # Tambahkan respons bot ke riwayat
    st.session_state.messages.append({"role": "assistant", "content": full_response})

Cara Menjalankannya:

Simpan kode di atas sebagai file Python (misalnya, app.py).

Buka terminal atau command prompt.

Jalankan perintah: streamlit run app.py

Usulan Ide Chatbot yang Menarik dan Kreatif
Untuk membuat chatbot Anda menonjol, pilihlah tema yang unik dan fungsional.

1. 🤖 Asisten Penulis Kreatif
Chatbot yang membantu pengguna mengatasi writer's block atau kebuntuan menulis.

Fitur:

Memberikan ide plot cerita berdasarkan genre yang dipilih (misal: "beri aku ide plot horor tentang rumah kosong").

Menghasilkan dialog antar karakter.

Menyarankan sinonim atau frasa yang lebih menarik.

Membuat deskripsi karakter atau latar tempat.

Tampilan: Gunakan tema gelap (dark mode) yang elegan dengan font serif untuk nuansa literasi. Anda bisa menambahkan gambar-gambar inspiratif yang relevan dengan genre tulisan.

2. 🥗 Perencana Resep & Menu Makanan
Sebuah chatbot yang membantu pengguna merencanakan makanan berdasarkan bahan-bahan yang mereka miliki.

Fitur:

Pengguna memasukkan bahan-bahan yang ada di kulkas.

Bot memberikan beberapa pilihan resep lengkap dengan langkah-langkahnya.

Bisa memberikan estimasi kalori atau informasi gizi.

Filter berdasarkan jenis masakan (Asia, Italia, dll.) atau waktu memasak.

Tampilan: Desain yang cerah dan bersih dengan banyak ruang putih. Gunakan ikon-ikon makanan yang menarik dan tampilkan gambar hasil masakan yang menggugah selera di setiap resep.

3. ✈️ Konsultan Perjalanan Virtual
Chatbot yang berfungsi sebagai agen perjalanan pribadi.

Fitur:

Memberikan rekomendasi tujuan wisata berdasarkan budget, minat (pantai, gunung, kota), dan lama waktu liburan.

Membuat itinerary atau jadwal perjalanan harian.

Memberikan tips lokal (misal: "restoran terbaik di Tokyo untuk ramen").

Informasi cuaca dan budaya setempat.

Tampilan: Gunakan gambar-gambar lanskap yang indah sebagai latar belakang atau di sidebar. Palet warna biru dan hijau untuk memberikan kesan tenang dan petualangan.

4. 🧑‍🏫 Tutor Bahasa Interaktif
Chatbot untuk latihan percakapan dalam bahasa asing.

Fitur:

Simulasi percakapan sehari-hari (misal: memesan kopi, menanyakan arah).

Memberikan koreksi tata bahasa sederhana.

Menyediakan kosakata baru sesuai konteks percakapan.

Mode kuis atau tebak kata.

Tampilan: Desain minimalis agar pengguna fokus pada teks. Gunakan bendera negara sebagai ikon untuk pemilihan bahasa. Anda bisa menambahkan progress bar untuk menunjukkan kemajuan belajar pengguna.

Tips Membuat Tampilan Indah dan Profesional
Tampilan sangat penting untuk pengalaman pengguna. Berikut cara mempercantik chatbot Streamlit Anda.

Gunakan Komponen Streamlit dengan Kreatif
Kolom dan Kontainer: Bagi layout Anda menggunakan st.columns() untuk menempatkan elemen berdampingan (misal: chat di satu sisi, gambar atau info tambahan di sisi lain). Gunakan st.container() untuk mengelompokkan elemen secara visual.

Sidebar (st.sidebar): Letakkan menu, pengaturan, atau profil pengguna di sidebar agar antarmuka utama tetap bersih dan fokus pada percakapan.

Ekspander (st.expander): Sembunyikan informasi tambahan atau riwayat obrolan yang panjang di dalam ekspander agar tidak memakan banyak tempat.

Ikon dan Emoji: Gunakan emoji seperti dalam contoh kode di atas untuk memberikan kepribadian pada bot dan antarmuka Anda.

Kustomisasi Tema
Streamlit memungkinkan Anda mengubah tema bawaan. Buat file bernama .streamlit/config.toml di direktori proyek Anda dan tambahkan konfigurasi seperti ini:

Ini, TOML

[theme]
primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"