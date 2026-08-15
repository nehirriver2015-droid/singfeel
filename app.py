from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/analyze-emotion', methods=['POST'])
def analyze_emotion():
    """
    Kullanıcının girdiği metnin duygusunu ve tonunu analiz eden API servisi.
    """
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({"error": "Lütfen analiz edilecek bir metin gönderin."}), 400
        
    text = data['text']
    
    # TextBlob kütüphanesi ile duygu analizi yapılıyor
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity  # -1.0 (Olumsuz) ile +1.0 (Olumlu) arası
    
    # Duygu durumunu ve yapay ses ayarlarını belirleme
    if polarity > 0.5:
        detected_mood = "excited"
        pitch = 1.5
        rate = 1.3
        message = "Yüksek olumlu duygu tespit edildi."
    elif polarity > 0.1:
        detected_mood = "happy"
        pitch = 1.3
        rate = 1.1
        message = "Olumlu duygu tespit edildi."
    elif polarity < -0.1:
        detected_mood = "serious"
        pitch = 0.7
        rate = 0.9
        message = "Ciddi / Olumsuz duygu tespit edildi."
    else:
        detected_mood = "calm"
        pitch = 0.9
        rate = 0.9
        message = "Nötr / Sakin duygu tespit edildi."

    # Yanıt oluşturma
    response_data = {
        "text": text,
        "sentiment_score": round(polarity, 2),
        "mood": detected_mood,
        "voice_settings": {
            "pitch": pitch,
            "rate": rate
        },
        "status_message": message
    }

    return jsonify(response_data), 200

if __name__ == '__main__':
    print("🚀 SignFeel AI Backend Sunucusu Çalışıyor...")
    app.run(debug=True, port=5000)
