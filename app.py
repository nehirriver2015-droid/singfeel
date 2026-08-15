import streamlit as st
from textblob import TextBlob

# Sayfa Konfigürasyonu
st.set_page_config(
    page_title="SignFeel AI",
    page_icon="🎭",
    layout="centered"
)

# Başlıklar
st.title("🎭 SignFeel")
st.caption("Next-Gen Emotion-Driven Accessible Communication Platform")
st.write("Duygularını seç veya metnini yaz; yapay zeka duyguyu analiz edip konuşma tonunu ayarlasın.")

st.divider()

# 1. DUYGU SEÇİMİ
st.subheader("1. Duygu Durumu Seçin")
mood = st.radio(
    "Hangi duygu tonuyla konuşmak istersiniz?",
    ["😄 Mutlu (Happy)", "🚀 Heyecanlı (Excited)", "🌿 Sakin (Calm)", "🎯 Ciddi (Serious)"],
    horizontal=True
)

# 2. METİN GİRİŞİ
st.subheader("2. Mesajınızı Yazın")
user_text = st.text_area("Aklınızdan geçenleri yazın:", placeholder="Hello! I am excited to share this project with you...")

# Hızlı Cümle Butonları
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("👋 Merhaba"):
        user_text = "Hello! How are you today?"
with col2:
    if st.button("🙏 Teşekkürler"):
        user_text = "Thank you so much for your support!"
with col3:
    if st.button("🆘 Yardım"):
        user_text = "I need a quick moment of assistance, please."

# 3. ANALİZ VE SESLENDİRME
if st.button("🔊 Duygu Tonuyla Seslendir", type="primary", use_container_width=True):
    if user_text.strip() != "":
        # Duygu Analizi (TextBlob)
        blob = TextBlob(user_text)
        polarity = round(blob.sentiment.polarity, 2)
        
        st.success(f"Analiz Tamamlandı! Duygu Skoru: {polarity}")
        
        # Tarayıcı Seslendirme Motoru
        html_code = f"""
            <script>
                var msg = new SpeechSynthesisUtterance("{user_text}");
                msg.lang = 'en-US';
                window.speechSynthesis.speak(msg);
            </script>
        """
        st.components.v1.html(html_code, height=0)
    else:
        st.warning("Lütfen önce bir metin girin.")

st.divider()
st.caption("Developed by an 11-Year-Old Visionary Developer • SignFeel AI")
