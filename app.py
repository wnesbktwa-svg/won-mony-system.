from flask import Flask, render_template_string
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_ly_dollar():
    try:
        # الاتصال بموقع عين ليبيا لجلب السعر
        url = "https://www.eanlibya.com/أسعار-العملات-مقابل-الدينار-الليبي/"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # البحث عن أول رقم يظهر في جدول العملات (عادة يكون الدولار)
        # ملاحظة: قد نحتاج لضبط هذا الجزء بناءً على تحديثات الموقع
        price_tag = soup.find('td', text='الدولار').find_next_sibling('td')
        return price_tag.text.strip() + " د.ل"
    except:
        return "8.77 د.ل" # سعر احتياطي في حال فشل الاتصال بالموقع

@app.route('/')
def home():
    ly_price = get_ly_dollar()
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Won Mony V10 - Smart Libya</title>
        <style>
            body { background: #000; color: #fff; font-family: sans-serif; text-align: center; padding: 20px; }
            .card { border-radius: 20px; padding: 25px; margin-bottom: 20px; background: #111; border: 2px solid; }
            .btc-card { border-color: #f7931a; box-shadow: 0 0 15px #f7931a; }
            .ly-card { border-color: #00ff00; box-shadow: 0 0 15px #00ff00; }
            .label { font-size: 14px; color: #888; }
            .price { font-size: 38px; font-weight: bold; margin: 15px 0; }
            .btn { background: #00ff00; color: #000; border: none; padding: 15px; border-radius: 12px; width: 100%; font-weight: bold; font-size: 18px; cursor: pointer; }
        </style>
        <script>
            async function fetchBtc() {
                try {
                    const res = await fetch('https://api.coinbase.com/v2/prices/BTC-USD/spot');
                    const data = await res.json();
                    document.getElementById('btc-val').innerText = '$' + parseFloat(data.data.amount).toLocaleString();
                } catch (e) { document.getElementById('btc-val').innerText = 'تحديث...'; }
            }
            setInterval(fetchBtc, 10000);
            window.onload = fetchBtc;
        </script>
    </head>
    <body>
        <h2 style="color:#00ff00;">WON MONY V10</h2>
        <p style="color:#555;">نظام الربط التلقائي بأسعار ليبيا</p>

        <div class="card btc-card">
            <div class="label">سعر البيتكوين (عالمي)</div>
            <div id="btc-val" class="price" style="color:#f7931a;">جاري الجلب...</div>
        </div>

        <div class="card ly-card">
            <div class="label">سعر الدولار (سوق موازي - عين ليبيا)</div>
            <div class="price" style="color:#00ff00;">{{ ly_price }}</div>
        </div>

        <button class="btn" onclick="location.reload()">تحديث البيانات الآن</button>

        <div style="margin-top:30px; font-size:12px; color:#333;">
            مصدر السعر المحلي: eanlibya.com
        </div>
    </body>
    </html>
    ''', ly_price=ly_price)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
