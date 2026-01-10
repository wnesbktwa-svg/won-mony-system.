from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Won Mony Global V8</title>
        <style>
            body { background: #000; color: #0f0; font-family: sans-serif; text-align: center; padding: 20px; }
            .card { border: 2px solid #0f0; border-radius: 20px; padding: 30px; background: #050505; box-shadow: 0 0 30px #0f0; max-width: 400px; margin: auto; }
            .price { font-size: 45px; color: #fff; margin: 20px 0; font-weight: bold; text-shadow: 0 0 10px #0f0; }
            .status { color: #888; font-size: 14px; }
        </style>
        <script>
            // كود جلب السعر مباشرة من المتصفح (يضمن العمل 100%)
            async function getPrice() {
                try {
                    const response = await fetch('https://api.coindesk.com/v1/bpi/currentprice.json');
                    const data = await response.json();
                    const price = data.bpi.USD.rate_float;
                    document.getElementById('btc-price').innerText = '$' + price.toLocaleString(undefined, {minimumFractionDigits: 2});
                    document.getElementById('status').innerText = '● السوق نشط الآن';
                } catch (error) {
                    document.getElementById('btc-price').innerText = 'جاري الاتصال...';
                }
            }
            setInterval(getPrice, 5000); // تحديث كل 5 ثوانٍ تلقائياً
            window.onload = getPrice;
        </script>
    </head>
    <body>
        <div class="card">
            <h1 style="font-size: 24px;">WON MONY GLOBAL V8</h1>
            <p>سعر البيتكوين (BTC) المباشر:</p>
            <div id="btc-price" class="price">جاري التحميل...</div>
            <p id="status" class="status">جاري تحديث البيانات...</p>
            <hr style="border: 0.5px solid #222; margin: 20px 0;">
            <p style="font-size: 12px; color: #444;">نظام مراقبة سحابي - تحديث تلقائي</p>
        </div>
    </body>
    </html>
    ''')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
