from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    # كود الواجهة المزدوجة (بيتكوين + دولار ليبيا)
    html_template = '''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Won Mony - ليبيا</title>
        <style>
            body { background: #000; color: #fff; font-family: sans-serif; text-align: center; padding: 20px; }
            .container { max-width: 450px; margin: auto; }
            .card { border-radius: 20px; padding: 20px; margin-bottom: 20px; position: relative; overflow: hidden; border: 2px solid; }
            
            /* تصميم كرت البيتكوين */
            .btc-card { border-color: #f7931a; box-shadow: 0 0 15px #f7931a; background: #111; }
            /* تصميم كرت الدولار ليبيا */
            .ly-card { border-color: #00ff00; box-shadow: 0 0 15px #00ff00; background: #111; }
            
            .label { font-size: 14px; color: #888; margin-bottom: 5px; }
            .price { font-size: 35px; font-weight: bold; margin: 10px 0; }
            .btc-price { color: #f7931a; }
            .ly-price { color: #00ff00; }
            
            .update-btn { background: #333; color: #fff; border: 1px solid #555; padding: 12px; border-radius: 10px; width: 100%; cursor: pointer; font-weight: bold; }
            .footer { margin-top: 30px; font-size: 12px; color: #444; }
        </style>
        <script>
            async function fetchGlobalPrices() {
                try {
                    // جلب سعر البيتكوين
                    const resBtc = await fetch('https://api.coinbase.com/v2/prices/BTC-USD/spot');
                    const dataBtc = await resBtc.json();
                    const btcPrice = parseFloat(dataBtc.data.amount).toLocaleString(undefined, {minimumFractionDigits: 2});
                    document.getElementById('btc-val').innerText = '$' + btcPrice;
                } catch (e) {
                    document.getElementById('btc-val').innerText = 'خطأ في الاتصال';
                }
            }
            setInterval(fetchGlobalPrices, 10000);
            window.onload = fetchGlobalPrices;
        </script>
    </head>
    <body>
        <div class="container">
            <h2 style="color:#0f0;">WON MONY GLOBAL V9</h2>
            <p style="color:#666; font-size:12px;">تحديث مباشر للأسعار</p>

            <div class="card btc-card">
                <div class="label">سعر البيتكوين العالمي (BTC)</div>
                <div id="btc-val" class="price btc-price">جاري التحميل...</div>
            </div>

            <div class="card ly-card">
                <div class="label">سعر الدولار في ليبيا (كاش)</div>
                <div class="price ly-price">7.25 د.ل</div> 
                <div style="font-size:11px; color:#555;">* يمكنك تعديل هذا السعر من الكود يدوياً</div>
            </div>

            <button class="update-btn" onclick="location.reload()">تحديث يدوي للبيانات</button>

            <div class="footer">
                برمج بواسطة: مبرمج ليبي طموح <br>
                System Status: Active & Secured
            </div>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
