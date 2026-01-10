import requests
from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

TOKEN = "8542169427:AAHv1JELHFp0Lreea9nhZMN2hY1pBfKC1rA"
CHAT_ID = "8319449101"

def get_prices():
    try:
        btc_url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        data = requests.get(btc_url, timeout=10).json()
        return data['bpi']['USD']['rate_float']
    except:
        return 0.0

def send_to_telegram(text):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}"
        requests.get(url, timeout=5)
    except:
        pass

@app.route('/')
def home():
    price_val = get_prices()
    now = datetime.datetime.now().strftime("%H:%M:%S")
    formatted_price = "{:,.2f}".format(price_val)
    send_to_telegram(f"💹 Won Mony: BTC Price is ${formatted_price}")
    
    html_template = '''
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { background: #000; color: #0f0; font-family: sans-serif; text-align: center; padding: 20px; }
            .card { border: 2px solid #0f0; border-radius: 15px; padding: 20px; background: #050505; box-shadow: 0 0 20px #0f0; max-width: 400px; margin: auto; }
            .price { font-size: 35px; color: white; margin: 20px 0; font-weight: bold; }
            button { background: #0f0; border: none; padding: 15px; border-radius: 10px; font-weight: bold; cursor: pointer; width: 100%; color: black; }
        </style>
    </head>
    <body>
        <div class="card">
            <h2 style="color:#0f0;">Won Mony Global V8</h2>
            <p>(BTC) سعر البيتكوين الآن مباشر:</p>
            <div class="price">$''' + formatted_price + '''</div>
            <p>توقيت التحديث: ''' + now + '''</p>
            <button onclick="location.reload()">تحديث السعر الحقيقي</button>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
