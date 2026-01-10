import requests
from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

# بيانات تليجرام الخاصة بك
TOKEN = "8542169427:AAHv1JELHFp0Lreea9nhZMN2hY1pBfKC1rA"
CHAT_ID = "8319449101"

def get_real_price():
    try:
        # مصدر بيانات مفتوح للسيرفرات المجانية
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        response = requests.get(url, timeout=10)
        data = response.json()
        return data['bpi']['USD']['rate_float']
    except:
        return 0.0

def send_alert(msg):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}"
        requests.get(url, timeout=5)
    except:
        pass

@app.route('/')
def index():
    raw_price = get_real_price()
    # تحويل الرقم إلى تنسيق مالي جميل
    display_price = "{:,.2f}".format(raw_price)
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    
    # إرسال إشعار لهاتفك عند دخول أي زائر
    send_alert(f"🚀 زائر جديد! سعر البيتكوين الآن: ${display_price}")

    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Won Mony Global</title>
        <style>
            body { background-color: #000; color: #0f0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; margin: 0; padding: 20px; }
            .container { border: 2px solid #0f0; border-radius: 20px; padding: 30px; background: #0a0a0a; box-shadow: 0 0 30px #0f0; max-width: 450px; margin: auto; }
            .price-box { font-size: 45px; color: #fff; margin: 25px 0; font-weight: bold; text-shadow: 0 0 10px #0f0; }
            .btn { background: #0f0; color: #000; border: none; padding: 18px 30px; border-radius: 12px; font-size: 18px; font-weight: bold; cursor: pointer; width: 100%; transition: 0.3s; }
            .btn:hover { background: #fff; box-shadow: 0 0 20px #fff; }
            .footer { margin-top: 20px; font-size: 12px; color: #555; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1 style="color:#0f0; letter-spacing: 2px;">WON MONY GLOBAL V8</h1>
            <p style="color:#888;">سعر البيتكوين (BTC) مباشر الآن:</p>
            <div class="price-box">$''' + display_price + '''</div>
            <p>توقيت التحديث: <span style="color:#fff;">''' + current_time + '''</span></p>
            <button class="btn" onclick="location.reload()">تحديث السعر الحقيقي</button>
            <div class="footer">نظام مراقبة الأسعار العالمي - برمجتك الخاصة</div>
        </div>
    </body>
    </html>
    ''')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
