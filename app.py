from flask import Flask, render_template_string, request

app = Flask(__name__)

# متغير عالمي لحفظ سعر السوق الموازي (يمكن تغييره من لوحة التحكم)
market_data = {"usd_to_lyd": 8.77}

@app.route('/', methods=['GET', 'POST'])
def home():
    # لوحة تحكم بسيطة لتحديث السعر يدوياً إذا أردت
    if request.method == 'POST' and request.form.get('new_rate'):
        market_data["usd_to_lyd"] = float(request.form.get('new_rate'))

    return render_template_string('''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Won Mony V15 - Libya Gold</title>
        <style>
            :root { --main-gold: #d4af37; --main-green: #00ff00; }
            body { 
                background: #000 url('https://www.transparenttextures.com/patterns/dark-matter.png'); 
                color: #fff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                margin: 0; padding: 20px; overflow-x: hidden;
            }
            /* خلفية خريطة ليبيا الباهتة */
            .bg-map {
                position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
                width: 90%; opacity: 0.1; z-index: -1; pointer-events: none;
            }
            .header { color: var(--main-gold); text-shadow: 0 0 15px var(--main-gold); margin-bottom: 5px; }
            .sub-header { color: #666; font-size: 12px; margin-bottom: 25px; }
            
            .main-box {
                background: rgba(10, 10, 10, 0.9); border: 1px solid var(--main-gold);
                border-radius: 25px; padding: 25px; max-width: 450px; margin: auto;
                box-shadow: 0 0 30px rgba(212, 175, 55, 0.2);
            }
            
            input[type="number"] {
                width: 90%; padding: 15px; border-radius: 15px; border: 1px solid #333;
                background: #1a1a1a; color: #fff; font-size: 24px; text-align: center; outline: none;
            }
            
            .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 25px; }
            .card { 
                background: rgba(255, 255, 255, 0.03); padding: 15px; border-radius: 20px; 
                border: 1px solid #222; transition: 0.3s;
            }
            .card:hover { border-color: var(--main-gold); }
            
            .val { font-size: 22px; font-weight: bold; margin-top: 5px; }
            .green { color: var(--main-green); }
            .gold { color: var(--main-gold); }
            
            .share-btn {
                background: linear-gradient(45deg, #25D366, #128C7E); color: white;
                border: none; padding: 18px; border-radius: 15px; width: 100%;
                font-weight: bold; font-size: 18px; cursor: pointer; margin-top: 20px;
            }

            /* لوحة التحكم المخفية بالأسفل */
            .admin-panel { margin-top: 50px; padding: 10px; border-top: 1px dashed #222; font-size: 10px; }
            .admin-panel input { width: 60px; font-size: 10px; padding: 2px; }
        </style>
        <script>
            let officialRate = 0;
            const blackMarketRate = {{ current_market_rate }}; 

            async function loadRates() {
                try {
                    const res = await fetch('https://open.er-api.com/v6/latest/USD');
                    const data = await res.json();
                    officialRate = data.rates.LYD;
                    updateValues(100); 
                } catch (e) { document.body.innerHTML += "خطأ في الشبكة"; }
            }

            function updateValues(usd) {
                if(!usd) usd = 0;
                let offVal = (usd * officialRate).toFixed(2);
                let bmVal = (usd * blackMarketRate).toFixed(2);
                let diff = (bmVal - offVal).toFixed(2);

                document.getElementById('off-val').innerText = offVal + ' د.ل';
                document.getElementById('bm-val').innerText = bmVal + ' د.ل';
                document.getElementById('diff-val').innerText = diff + ' د.ل';
                
                let msg = `*تقرير Won Mony V15*%0Aالمبلغ: ${usd}$%0Aالسعر الموازي: ${bmVal} د.ل%0Aالفارق المالي: ${diff} د.ل`;
                document.getElementById('whatsapp-link').onclick = () => {
                    window.open(`https://wa.me/?text=${msg}`, '_blank');
                };
            }
            window.onload = loadRates;
        </script>
    </head>
    <body>
        <img class="bg-map" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Flag_map_of_Libya.svg/1200px-Flag_map_of_Libya.svg.png">
        
        <h1 class="header">WON MONY GOLD</h1>
        <div class="sub-header">نظام التاجر الليبي الذكي - الإصدار V15</div>

        <div class="main-box">
            <div style="color: #888; margin-bottom: 10px;">أدخل القيمة بالدولار</div>
            <input type="number" id="input" placeholder="100" oninput="updateValues(this.value)">
            
            <div class="grid">
                <div class="card">
                    <div style="font-size: 10px; color: #666;">سعر المصرف</div>
                    <div id="off-val" class="val green">...</div>
                </div>
                <div class="card">
                    <div style="font-size: 10px; color: #666;">سعر الكاش</div>
                    <div id="bm-val" class="val gold">...</div>
                </div>
            </div>

            <div class="card" style="margin-top: 15px; border-style: dashed;">
                <div style="font-size: 11px; color: #666;">الفارق المالي (الربح)</div>
                <div id="diff-val" style="font-size: 28px; font-weight: bold;">...</div>
            </div>

            <button id="whatsapp-link" class="share-btn">مشاركة التقرير عبر واتساب ✅</button>
        </div>

        <div class="admin-panel">
            <form method="POST">
                لوحة التحكم: تحديث سعر السوق الحالي <input type="number" step="0.01" name="new_rate" placeholder="{{ current_market_rate }}">
                <button type="submit" style="font-size: 10px;">تحديث</button>
            </form>
            <p>Powered by Won Mony Labs | System Live</p>
        </div>
    </body>
    </html>
    ''', current_market_rate=market_data["usd_to_lyd"])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
