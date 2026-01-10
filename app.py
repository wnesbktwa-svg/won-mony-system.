from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="ar">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Won Mony Global V8</title>
        <style>
            body { background: #000; color: #0f0; font-family: sans-serif; text-align: center; padding: 40px 20px; }
            .card { border: 2px solid #0f0; border-radius: 20px; padding: 30px; background: #050505; box-shadow: 0 0 20px #0f0; max-width: 400px; margin: auto; }
            .price { font-size: 45px; color: white; margin: 25px 0; font-weight: bold; text-shadow: 0 0 10px #0f0; }
            .btn { background: #0f0; border: none; padding: 15px; border-radius: 12px; font-weight: bold; width: 100%; cursor: pointer; color: #000; font-size: 18px; }
        </style>
        <script>
            async function updatePrice() {
                try {
                    const response = await fetch('https://api.coindesk.com/v1/bpi/currentprice.json');
                    const data = await response.json();
                    const btcPrice = data.bpi.USD.rate_float;
                    document.getElementById('btc-val').innerText = '$' + btcPrice.toLocaleString(undefined, {minimumFractionDigits: 2});
                } catch (e) {
                    document.getElementById('btc-val').innerText = 'جاري التحديث...';
                }
            }
            setInterval(updatePrice, 10000); // تحديث تلقائي كل 10 ثوانٍ
            window.onload = updatePrice;
        </script>
    </head>
    <body>
        <div class="card">
            <h1 style="font-size: 24px;">WON MONY GLOBAL V8</h1>
            <p style="color: #888;">(BTC) سعر البيتكوين مباشر الآن:</p>
            <div id="btc-val" class="price">جاري التحميل...</div>
            <button class="btn" onclick="location.reload()">تحديث السعر الآن</button>
            <p style="font-size: 12px; margin-top: 25px; color: #444;">نظام سحابي عالمي - الإصدار الثامن</p>
        </div>
    </body>
    </html>
    ''')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
