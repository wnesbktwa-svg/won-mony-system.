from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    # كود HTML احترافي يجلب السعر من المتصفح مباشرة لتفادي قيود السيرفر
    html_template = '''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Won Mony Global V8</title>
        <style>
            body { background: #000; color: #0f0; font-family: sans-serif; text-align: center; padding: 50px 20px; }
            .card { border: 2px solid #0f0; border-radius: 20px; padding: 30px; background: #050505; box-shadow: 0 0 25px #0f0; max-width: 400px; margin: auto; }
            .price { font-size: 48px; color: #fff; margin: 25px 0; font-weight: bold; text-shadow: 0 0 10px #0f0; }
            .status-dot { height: 10px; width: 10px; background-color: #0f0; border-radius: 50%; display: inline-block; margin-left: 5px; }
            .btn { background: #0f0; border: none; padding: 15px; border-radius: 12px; font-weight: bold; width: 100%; cursor: pointer; color: #000; font-size: 18px; transition: 0.3s; }
            .btn:active { transform: scale(0.95); background: #fff; }
        </style>
        <script>
            async function fetchPrice() {
                try {
                    const res = await fetch('https://api.coinbase.com/v2/prices/BTC-USD/spot');
                    const data = await res.json();
                    const price = parseFloat(data.data.amount).toLocaleString(undefined, {minimumFractionDigits: 2});
                    document.getElementById('btc-price').innerText = '$' + price;
                    document.getElementById('status-text').innerText = 'متصل ومباشر';
                } catch (e) {
                    document.getElementById('btc-price').innerText = 'جاري المحاولة...';
                }
            }
            setInterval(fetchPrice, 5000); // تحديث كل 5 ثواني
            window.onload = fetchPrice;
        </script>
    </head>
    <body>
        <div class="card">
            <h1 style="font-size: 24px; letter-spacing: 1px;">WON MONY GLOBAL V8</h1>
            <p style="color: #888;">سعر البيتكوين مباشر (BTC/USD)</p>
            <div id="btc-price" class="price">جاري التحميل...</div>
            <button class="btn" onclick="fetchPrice()">تحديث السعر الآن</button>
            <div style="margin-top: 25px; font-size: 13px; color: #555;">
                <span id="status-text">جاري الاتصال</span> <span class="status-dot"></span>
            </div>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
