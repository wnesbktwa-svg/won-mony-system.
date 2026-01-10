from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Won Mony V10</title>
        <style>
            body { background: #000; color: #fff; font-family: sans-serif; text-align: center; padding: 20px; }
            .card { border-radius: 20px; padding: 25px; margin-bottom: 20px; background: #0a0a0a; border: 2px solid; transition: 0.3s; }
            .btc-card { border-color: #f7931a; box-shadow: 0 0 15px #f7931a; }
            .ly-card { border-color: #00ff00; box-shadow: 0 0 15px #00ff00; }
            .label { font-size: 14px; color: #888; margin-bottom: 10px; }
            .price { font-size: 38px; font-weight: bold; }
            .btn { background: #00ff00; color: #000; border: none; padding: 15px; border-radius: 12px; width: 100%; font-weight: bold; font-size: 18px; cursor: pointer; }
        </style>
        <script>
            async function updatePrices() {
                try {
                    // جلب البيتكوين
                    const resBtc = await fetch('https://api.coinbase.com/v2/prices/BTC-USD/spot');
                    const dataBtc = await resBtc.json();
                    document.getElementById('btc-val').innerText = '$' + parseFloat(dataBtc.data.amount).toLocaleString();
                    
                    // تحديث حالة النظام
                    document.getElementById('status').innerText = 'متصل ومباشر ●';
                } catch (e) {
                    document.getElementById('btc-val').innerText = 'تحديث...';
                }
            }
            setInterval(updatePrices, 10000);
            window.onload = updatePrices;
        </script>
    </head>
    <body>
        <h2 style="color:#00ff00; letter-spacing: 2px;">WON MONY V10</h2>
        <div id="status" style="font-size: 12px; color: #0f0; margin-bottom: 20px;">جاري الاتصال...</div>

        <div class="card btc-card">
            <div class="label">البيتكوين مقابل الدولار (عالمي)</div>
            <div id="btc-val" class="price" style="color:#f7931a;">...</div>
        </div>

        <div class="card ly-card">
            <div class="label">الدولار مقابل الدينار (سوق موازي)</div>
            <div class="price" style="color:#00ff00;">8.77 د.ل</div>
            <div style="font-size: 11px; color: #444; margin-top: 10px;">المصدر: عين ليبيا (تحديث يدوي مستقر)</div>
        </div>

        <button class="btn" onclick="location.reload()">تحديث البيانات</button>
        
        <p style="margin-top: 30px; color: #222; font-size: 10px;">Built by: Won Mony System</p>
    </body>
    </html>
    ''')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
