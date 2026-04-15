from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Adını ve öğrenci numaranı HTML formatında döndürüyoruz
    return "<h1>Merhaba, ben Müge!</h1><p>Öğrenci Numaram: 123456789</p>"

if __name__ == '__main__':
    # Uygulamayı yerel sunucuda başlatıyoruz
    app.run(debug=True)
