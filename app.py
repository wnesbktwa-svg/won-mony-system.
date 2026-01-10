from flask import Flask, render_template_string, request

app = Flask(__name__)

# قاعدة بيانات مؤقتة (تصفر عند إعادة تشغيل السيرفر في النسخة المجانية)
app_stats = {
    "total_visits": 0,
    "market_rate": 8.77,
    "last_update": "2026-01-10"
}

@app.route('/', methods=['GET', 'POST'])
def home():
    # زيادة عداد الزوار آلياً عند كل دخول
    app_stats["total_visits"] += 1
    
    if request.method == 'POST' and request.form.get('new_rate'):
        try:
            app_stats["market_rate"] = float(request.form.get('new_rate'))
        except: pass

    return render_template_string('''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Won Mony V17 - Admin Analytics</title>
        <style>
            body { background: #000; color: #fff; font-family: sans-serif; text-align: center; padding: 10px; }
            .main-box { border: 2px solid #d4af37; border-radius: 20px; padding: 20px; max-width: 400px; margin: auto; background: #0a0a0a; }
            .price-card { background: #111; padding: 15px; border-radius: 15px; margin-top: 10px; border: 1px solid #222; }
            .val { font-size: 24px; font-weight: bold; }
            .ad-space { background: #111; border: 1px dashed #d4af37; padding: 15px; margin: 20px auto; border-radius: 15px; color: #d4af37; }
            
            /* تصميم لوحة الإحصائيات */
            .admin-stats {
                background: #050505; border-top: 1px solid #222; 
                margin-top: 50px; padding: 20px; font-size: 12px; color: #555;
            }
            .stat-badge { color: #d4af37; font-weight: bold; font-size: 16px; }
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
        <h2 style="color:#d4af37;">WON MONY PRO <span style="font-size:10px; color:#444;">V17</span></h2>
        
        <div class="main-box">
            <input type="number" id="in" placeholder="100" oninput="calc(this.value)" 
                   style="width:80%; padding:10px; background:#111; color:#fff; border:1px solid #333; border-radius:10px; text-align:center; font-size:20px;">
            
            <div class="price-card">
                <div style="color:#666; font-size:11px;">سعر المصرف</div>
                <div id="o-v" class="val" style="color:#0f0;">...</div>
            </div>

            <div class="price-card">
                <div style="color:#666; font-size:11px;">السوق السوداء</div>
                <div id="b-v" class="val" style="color:#d4af37;">...</div>
            </div>

            <div class="price-card" style="border-color: #333;">
                <div style="color:#666; font-size:11px;">فارق الربح</div>
                <div id="d-v" class="val">...</div>
            </div>
        </div>

        <div class="ad-space">مساحة إعلانية جاهزة للربح الآلي</div>

        <div class="admin-stats">
            <p>📊 إحصائيات الإدارة (خاصة بك):</p>
            <p>إجمالي الزيارات اليوم: <span class="stat-badge">{{ total_visits }}</span></p>
            <form method="POST">
                تعديل سعر السوق: <input type="number" step="0.01" name="new_rate" value="{{ current_rate }}" style="width:60px; background:#000; color:#d4af37; border:1px solid #333;">
                <button type="submit" style="background:#d4af37; color:#000; border:none; border-radius:5px; padding:2px 10px;">تحديث</button>
            </form>
        </div>
    </body>
    </html>
    ''', current_rate=app_stats["market_rate"], total_visits=app_stats["total_visits"])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
