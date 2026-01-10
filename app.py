import requests
from flask import Flask, render_template_string

app = Flask(__name__)

# دالة جلب السعر من مصدر موثوق لا يحظر السيرفرات المجانية
def get_btc_price():
    try:
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        response = requests.get(url, timeout=10)
        data = response.json()
        return data['bpi']['USD']['rate_float']
    except:
        return 0.0

@app.route('/')
def index():
    price = get_btc_price()
    # تنسيق الرقم بفاصلة آلاف وعلامة عشرية
    formatted_price = "{:,.2f}".format(price)
    
    # واجهة الموقع (HTML) مدمجة لضمان عدم حدوث خطأ 500
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Won Mony V8</title>
        <style>
            body {{ background: #000; color: #0f0; font-family: sans-serif; text-align: center; padding: 40px 20px; }}
            .card {{ border: 2px solid #0f0; border-radius: 20px; padding: 30px; background: #050505; box-shadow: 0 0 20px #0f0; max-width: 400px; margin: auto; }}
            .price {{ font-size: 40px; color: white; margin: 20px 0; font-weight: bold; }}
            .btn {{ background: #0f0; border: none; padding: 15px; border-radius: 10px; font-weight: bold; width: 100%; cursor: pointer; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1 style="font-size: 22px;">WON MONY GLOBAL V8</h1>
            <p style="color: #888;">سعر البيتكوين مباشر (USD):</p>
            <div class="price">${formatted_price}</div>
            <button class="btn" onclick="location.reload()">تحديث الآن</button>
            <p style="font-size: 10px; margin-top: 20px; color: #333;">System Status: Live</p>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
