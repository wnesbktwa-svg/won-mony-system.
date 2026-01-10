from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

# السعر الحالي للسوق الموازي
market_data = {"usd_to_lyd": 8.77}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST' and request.form.get('new_rate'):
        try:
            market_data["usd_to_lyd"] = float(request.form.get('new_rate'))
        except:
            pass

    return render_template_string('''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Won Mony Gold V15</title>
        <style>
            body { 
                background: #000; color: #fff; font-family: sans-serif; 
                text-align: center; padding: 20px;
                background-image: radial-gradient(circle, #1a1a1a 10%, #000 90%);
            }
            .main-box {
                border: 2px solid #d4af37; border-radius: 25px;
                padding: 25px; max-width: 400px; margin: auto;
                background: rgba(0,0,0,0.8); box-shadow: 0 0 20px rgba(212,175,55,0.3);
            }
            .header { color: #d4af37; text-shadow: 0 0 10px #d4af37; }
            input {
                width: 80%; padding: 15px; border-radius: 12px; border: 1px solid #333;
                background: #111; color: #fff; font-size: 22px; text-align: center;
            }
            .card { background: #111; padding: 15px; border-radius: 15px; margin-top: 15px; border: 1px solid #222; }
            .gold { color: #d4af37; font-weight: bold; font-size: 24px; }
            .green { color: #00ff00; font-weight: bold; font-size: 24px; }
            .share-btn {
                background: #25D366; color: white; border: none; padding: 15px;
                border-radius: 12px; width: 100%; font-weight: bold; margin-top: 20px; cursor: pointer;
            }
        </style>
        <script>
            let officialRate = 4.85; // قيمة افتراضية في حال فشل الـ API
            const blackMarketRate = {{ current_market_rate }};

            async function loadRates() {
                try {
                    const res = await fetch('https://open.er-api.com/v6/latest/USD');
                    const data = await res.json();
                    officialRate = data.rates.LYD;
                    updateValues(100);
                } catch (e) { updateValues(100); }
            }

            function updateValues(usd) {
                if(!usd) usd = 0;
                let offVal = (usd * officialRate).toFixed(2);
                let bmVal = (usd * blackMarketRate).toFixed(2);
                let diff = (bmVal - offVal).toFixed(2);

                document.getElementById('off-val').innerText = offVal + ' د.ل';
                document.getElementById('bm-val').innerText = bmVal + ' د.ل';
                document.getElementById('diff-val').innerText = diff + ' د.ل';
                
                let msg = `*تقرير Won Mony*%0Aالمبلغ: ${usd}$%0Aالسعر الموازي: ${bmVal} د.ل%0Aالفارق: ${diff} د.ل`;
                document.getElementById('whatsapp-link').onclick = () => {
                    window.open(`https://wa.me/?text=${msg}`, '_blank');
                };
            }
            window.onload = loadRates;
        </script>
    </head>
    <body>
        <h1 class="header">WON MONY GOLD</h1>
        <div class="main-box">
            <p style="color:#888;">أدخل القيمة بالدولار</p>
            <input type="number" id="input" placeholder="100" oninput="updateValues(this.value)">
            
            <div class="card">
                <div style="font-size:12px; color:#666;">سعر المصرف</div>
                <div id="off-val" class="green">...</div>
            </div>
            <div class="card">
                <div style="font-size:12px; color:#666;">سعر السوق الموازي</div>
                <div id="bm-val" class="gold">...</div>
            </div>
            <div class="card">
                <div style="font-size:12px; color:#666;">الفارق المالي</div>
                <div id="diff-val" style="font-size:24px;">...</div>
            </div>

            <button id="whatsapp-link" class="share-btn">إرسال التقرير عبر واتساب</button>
        </div>
        <div style="margin-top:40px; font-size:10px; color:#333;">
            <form method="POST">
                تحديث السعر يدوياً: <input type="number" step="0.01" name="new_rate" style="width:60px; font-size:10px; padding:2px;">
                <button type="submit" style="font-size:10px;">حفظ</button>
            </form>
        </div>
    </body>
    </html>
    ''', current_market_rate=market_data["usd_to_lyd"])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
