from flask import Flask, render_template_string, request

app = Flask(__name__)

# بيانات السوق (يمكنك تحديثها من لوحة التحكم)
market_data = {"usd_to_lyd": 8.77, "is_alert_on": True}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST' and request.form.get('new_rate'):
        try:
            market_data["usd_to_lyd"] = float(request.form.get('new_rate'))
        except: pass

    return render_template_string('''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Won Mony V16 - Pro Monetized</title>
        <style>
            body { background: #000; color: #fff; font-family: sans-serif; text-align: center; padding: 10px; }
            .main-box { border: 2px solid #d4af37; border-radius: 20px; padding: 20px; max-width: 400px; margin: auto; background: #0a0a0a; }
            
            /* مساحة إعلانية احترافية */
            .ad-space {
                background: linear-gradient(45deg, #1a1a1a, #222);
                border: 1px dashed #d4af37; border-radius: 15px;
                padding: 15px; margin: 20px auto; max-width: 400px;
                color: #d4af37; font-size: 14px; cursor: pointer;
            }
            
            .price-card { background: #111; padding: 15px; border-radius: 15px; margin-top: 10px; border: 1px solid #222; }
            .val { font-size: 24px; font-weight: bold; }
            .share-btn { background: #25D366; color: white; border: none; padding: 15px; border-radius: 12px; width: 100%; font-weight: bold; margin-top: 15px; }
            
            /* تنبيه آلي */
            .alert-box { background: rgba(212, 175, 55, 0.1); color: #d4af37; padding: 10px; border-radius: 10px; font-size: 12px; margin-bottom: 15px; border: 1px solid #d4af37; }
        </style>
        <script>
            let offRate = 4.85;
            const bmRate = {{ current_rate }};

            async function load() {
                const res = await fetch('https://open.er-api.com/v6/latest/USD');
                const data = await res.json();
                offRate = data.rates.LYD;
                calc(100);
            }

            function calc(usd) {
                if(!usd) usd = 0;
                let o = (usd * offRate).toFixed(2);
                let b = (usd * bmRate).toFixed(2);
                document.getElementById('o-v').innerText = o + ' د.ل';
                document.getElementById('b-v').innerText = b + ' د.ل';
                document.getElementById('d-v').innerText = (b - o).toFixed(2) + ' د.ل';
            }
            window.onload = load;
        </script>
    </head>
    <body>
        <h2 style="color:#d4af37;">WON MONY PRO</h2>
        
        <div class="alert-box">⚠️ تنبيه: فرق السعر اليوم يتجاوز 300 دينار لكل 100$! فرصة للتبديل.</div>

        <div class="main-box">
            <input type="number" id="in" placeholder="100" oninput="calc(this.value)" 
                   style="width:80%; padding:10px; background:#111; color:#fff; border:1px solid #333; border-radius:10px; text-align:center; font-size:20px;">
            
            <div class="price-card">
                <div style="color:#666; font-size:12px;">سعر المصرف الرسمي</div>
                <div id="o-v" class="val" style="color:#0f0;">...</div>
            </div>

            <div class="price-card">
                <div style="color:#666; font-size:12px;">سعر السوق السوداء</div>
                <div id="b-v" class="val" style="color:#d4af37;">...</div>
            </div>

            <button class="share-btn">مشاركة التقرير السريع</button>
        </div>

        <div class="ad-space" onclick="alert('هنا يظهر إعلانك التلقائي أو إعلان شركة صرافة')">
            <b>مساحة إعلانية محجوزة</b><br>
            <span style="font-size:10px; color:#555;">للاعلان هنا، تواصل مع إدارة التطبيق آلياً</span>
        </div>

        <div style="font-size:10px; color:#222; margin-top:30px;">
            <form method="POST">
                تعديل السعر: <input type="number" step="0.01" name="new_rate" style="width:50px;">
                <button type="submit">حفظ</button>
            </form>
        </div>
    </body>
    </html>
    ''', current_rate=market_data["usd_to_lyd"])
