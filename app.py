import requests
from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

TOKEN = "8542169427:AAHv1JELHFp0Lreea9nhZMN2hY1pBfKC1rA"
CHAT_ID = "8319449101"

def get_prices():
    try:
        btc_url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        data = requests.get(btc_url, timeout=5).json()
        return data['price']
    except:
        return "0.00"

@app.route('/')
def home():
    btc_price = get_prices()
    now = datetime.datetime.now().strftime("%H:%M:%S")
    return f'''
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{ background: #000; color: #0f0; font-family: sans-serif; text-align: center; padding: 20px; }}
            .card {{ border: 2px solid #0f0; border-radius: 15px; padding: 20px; background: #050505; box-shadow: 0 0 20px #0f0; }}
            .price {{ font-size: 35px; color: white; margin: 15px 0; }}
            button {{ background: #0f0; border: none; padding: 15px; border-radius: 5px; font-weight: bold; cursor: pointer; width: 100%; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>Won Mony Global V8</h2>
            <p>سعر البيتكوين الآن (BTC):</p>
            <div class="price">${float(btc_price):,.2f}</div>
            <p>توقيت التحديث: {now}</p>
            <button onclick="location.reload()">تحديث السعر المباشر</button>
        </div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
