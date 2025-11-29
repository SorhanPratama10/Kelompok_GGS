# ==============================================================
# 🌊 CHATBOT EDUKASI SAMPAH LAUT - KELOMPOK 8 🌊
# Bidang AI   : Natural Language Processing (NLP)
# Algoritma   : Rule-Based NLP / Intent Recognition
# ==============================================================
# Dibuat untuk membantu edukasi masyarakat mengenai bahaya
# dan solusi dari pencemaran laut akibat sampah plastik 🌍
# ==============================================================

from colorama import Fore, Style, init
import random
import time

init(autoreset=True)

# -------------------------------
# Fungsi identifikasi intent
# -------------------------------
def identifikasi_intent(teks):
    teks = teks.lower()

    if any(k in teks for k in ["halo", "hai", "hi", "selamat pagi", "selamat siang", "selamat malam"]):
        return "salam"
    elif any(k in teks for k in ["apa itu sampah laut", "sampah laut", "laut kotor", "apa itu sampah", "sampah di laut"]):
        return "tanya_sampah_laut"
    elif any(k in teks for k in ["bahaya", "berbahaya", "dampak", "efek", "akibat sampah laut"]):
        return "bahaya_sampah"
    elif any(k in teks for k in ["cara menjaga", "mengurangi", "mencegah", "membersihkan", "menjaga laut"]):
        return "cara_menjaga"
    elif any(k in teks for k in ["daur ulang", "recycle", "olah sampah", "pengolahan sampah"]):
        return "daur_ulang"
    elif any(k in teks for k in ["fakta", "data", "berapa banyak", "statistik", "jumlah sampah"]):
        return "data_fakta"
    elif any(k in teks for k in ["terima kasih", "makasih", "thanks"]):
        return "ucapan_terima_kasih"
    else:
        return "tidak_dikenal"

# -------------------------------
# Fungsi jawaban chatbot
# -------------------------------
def chatbot(teks):
    intent = identifikasi_intent(teks)

    if intent == "salam":
        return (
            "Hai! 👋 Saya Chatbot *Edukasi Sampah Laut* 🌊\n"
            "Saya bisa membantu kamu memahami apa itu sampah laut, bahayanya, dan bagaimana cara kita menjaga laut agar tetap bersih dan sehat 🌴\n"
            "Silakan ajukan pertanyaan seperti:\n"
            f"{Fore.YELLOW}- Apa itu sampah laut?\n- Bahaya sampah laut?\n- Cara menjaga laut?\n- Daur ulang sampah?\n- Fakta sampah laut?"
        )

    elif intent == "tanya_sampah_laut":
        return (
            "📘 **Penjelasan:**\n"
            "Sampah laut adalah segala jenis limbah yang masuk ke laut — baik dari daratan maupun dari aktivitas di laut sendiri.\n"
            "Sebagian besar berasal dari plastik sekali pakai, botol minuman, jaring ikan, dan limbah rumah tangga yang terbawa arus sungai.\n"
            "Sampah ini dapat mengapung di permukaan, tenggelam ke dasar laut, atau menumpuk di pesisir pantai sehingga merusak ekosistem laut 🌍."
        )

    elif intent == "bahaya_sampah":
        return (
            "⚠️ **Bahaya Sampah Laut:**\n"
            "Sampah laut menimbulkan dampak serius bagi makhluk hidup dan manusia:\n"
            f"{Fore.YELLOW}1️⃣ Hewan laut seperti penyu, ikan, dan burung laut sering menelan plastik yang dikira makanan.\n"
            "2️⃣ Plastik yang terurai menjadi mikroplastik bisa masuk ke rantai makanan dan akhirnya dikonsumsi manusia.\n"
            "3️⃣ Terumbu karang dan ekosistem laut rusak akibat tertutup limbah padat.\n"
            f"{Fore.CYAN}Dampak ini bukan hanya untuk lingkungan, tapi juga untuk kesehatan kita sebagai manusia."
        )

    elif intent == "cara_menjaga":
        return (
            "🌿 **Cara Menjaga Laut Agar Tetap Bersih:**\n"
            f"{Fore.YELLOW}1️⃣ Kurangi penggunaan plastik sekali pakai seperti sedotan dan kantong plastik.\n"
            "2️⃣ Pisahkan dan buang sampah sesuai jenisnya (organik dan anorganik).\n"
            "3️⃣ Ikuti kegiatan bersih pantai dan edukasi lingkungan.\n"
            "4️⃣ Dukung program daur ulang dan gunakan produk ramah lingkungan.\n"
            f"{Fore.CYAN}Dengan langkah kecil dari kita semua, laut akan tetap bersih dan indah untuk generasi selanjutnya 🌊."
        )

    elif intent == "daur_ulang":
        return (
            "♻️ **Tentang Daur Ulang:**\n"
            "Sampah plastik yang terkumpul bisa diolah kembali menjadi bahan yang bermanfaat.\n"
            f"{Fore.YELLOW}- Contohnya: tas, paving block, bahan bangunan, atau karya seni.\n"
            "Namun tidak semua plastik bisa didaur ulang — karena itu penting untuk memilah sejak dari rumah.\n"
            f"{Fore.CYAN}Daur ulang membantu mengurangi jumlah sampah yang berakhir di laut dan menjaga ekosistem laut tetap lestari."
        )

    elif intent == "data_fakta":
        return (
            "📊 **Fakta dan Data tentang Sampah Laut:**\n"
            f"{Fore.YELLOW}- Setiap tahun sekitar 8 juta ton plastik masuk ke laut (data PBB).\n"
            "- 80% sampah laut berasal dari aktivitas manusia di daratan.\n"
            "- Mikroplastik kini ditemukan di hampir seluruh lautan di dunia.\n"
            "- Jika tidak ditangani, pada tahun 2050 jumlah plastik di laut bisa lebih banyak dari ikan! 🐠\n"
            f"{Fore.CYAN}Fakta ini menunjukkan pentingnya perubahan perilaku kita terhadap sampah."
        )

    elif intent == "ucapan_terima_kasih":
        return (
            "💙 Sama-sama! Terima kasih sudah peduli dengan laut kita 🌊\n"
            "Semoga informasi yang saya berikan bisa membantu kamu memahami pentingnya menjaga kebersihan laut.\n"
            f"{Fore.CYAN}Mari bersama wujudkan laut yang bersih, sehat, dan bebas dari sampah plastik!"
        )

    else:
        return (
            "❓ Maaf, saya hanya bisa menjawab pertanyaan seputar edukasi dan kebersihan laut 🌊\n"
            f"{Fore.YELLOW}Coba tanya hal seperti:\n- Apa itu sampah laut?\n- Bahaya sampah laut?\n- Cara menjaga laut?\n- Daur ulang sampah?"
        )

# -------------------------------
# Tampilan pembuka (intro)
# -------------------------------
print(Fore.CYAN + Style.BRIGHT + "\n🌊==========================================================🌊")
print(Fore.BLUE + Style.BRIGHT + "        CHATBOT EDUKASI SAMPAH LAUT - KELOMPOK 8")
print(Fore.CYAN + "   Bidang AI : Natural Language Processing (NLP)")
print(Fore.CYAN + "   Algoritma : Rule-Based NLP / Intent Recognition")
print(Fore.CYAN + "🌊==========================================================🌊\n")

time.sleep(0.5)
print(Fore.YELLOW + "Ketik 'keluar' untuk mengakhiri percakapan.\n")

# -------------------------------
# Loop utama percakapan
# -------------------------------
while True:
    user = input(Fore.WHITE + Style.BRIGHT + "👤 Kamu : ").strip()
    if user.lower() in ["keluar", "exit", "quit"]:
        print(Fore.GREEN + "\n🤖 Bot  : Terima kasih! Jaga laut kita tetap bersih dan lestari 🌴\n")
        break

    time.sleep(0.6)
    print(Fore.CYAN + Style.BRIGHT + "\n🤖 Bot  :" + Style.NORMAL, chatbot(user))
    print()
