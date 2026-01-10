from flask import Flask, render_template_string, request

app = Flask(__name__)

# إحصائيات النظام وسعر السوق الحالي
app_stats = {"total_visits": 0, "market_rate": 8.79}

@app.route('/', methods=['GET', 'POST'])
def home():
    app_stats["total_visits"] += 1
    if request.method == 'POST' and request.form.get('new_rate'):
        try: 
            app_stats["market_rate"] = float(request.form.get('new_rate'))
        except: 
            pass

    return render_template_string('''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Won Mony V18 - Profit Active</title>
        
        <script type='text/javascript' src='https://pl28441931.effectiveratecpm.com/7d/5d/7c/7d5d7c80528441931.js'></script>
        
        <style>
            body { background: #000; color: #fff; font-family: sans-serif; text-align: center; padding: 10px; }
            .main-box { border: 2px solid #d4af37; border-radius: 20px; padding: 20px; max-width: 400px; margin: auto; background: #0a0a0a; box-shadow: 0 0 20px rgba(212,175,55,0.2); }
            .header { color: #d4af37; text-shadow: 0 0 10px #d4af37; margin-bottom: 20px; }
            .price-card { background: #111; padding: 15px; border-radius: 15px; margin-top: 10px; border: 1px solid #222; }
            .val { font-size: 26px; font-weight: bold; }
            .gold { color: #d4af37; } .green { color: #0f0; }
            .admin-stats { background: #050505; margin-top: 50px; padding: 20px; font-size: 11px; border-top: 1px solid #222; color: #444; }
            input { width: 85%; padding: 15px; background: #111; color: #fff; border: 1px solid #333; border-radius: 12px; text-align: center; font-size: 24px; }
        </style>
        <script>
            let offRate = 4.85;
            const bmRate = {{ current_rate }};
            async function load() {
                try {
                    const res = await fetch('https://open.er-api.com/v6/latest/USD');
                    const data = await res.json();
                    offRate = data.rates.LYD;
                    calc(100);
                } catch(e) { calc(100); }
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
        <h2 class="header">WON MONY PRO <span style="font-size:10px;">V18</span></h2>
        
        <div class="main-box">
            <p style="color:#666; font-size: 14px;">أدخل القيمة بالدولار (USD)</p>
            <input type="number" id="in" placeholder="100" oninput="calc(this.value)">
            
            <div class="price-card">
                <div style="font-size:11px; color:#555;">سعر المصرف الرسمي</div>
                <div id="o-v" class="val green">...</div>
            </div>

            <div class="price-card">
                <div style="font-size:11px; color:#555;">سعر السوق الموازي</div>
                <div id="b-v" class="val gold">...</div>
            </div>

            <div class="price-card" style="border-style: dashed; border-color: #d4af37;">
                <div style="font-size:11px; color:#555;">صافي فارق السعر</div>
                <div id="d-v" class="val">...</div>
            </div>
        </div>

        <div class="admin-stats">
            📊 لوحة إدارة النظام:<br>
            إجمالي الزيارات المحتسبة: <b>{{ total_visits }}</b><br>
            حالة الإعلانات: <span style="color: #0f0;">نشطة ✅</span>
            <form method="POST" style="margin-top:10px;">
                تعديل السعر اليدوي: <input type="number" step="0.01" name="new_rate" value="{{ current_rate }}" style="width:60px; font-size: 12px; padding: 5px;">
                <button type="submit" style="font-size: 10px; background: #d4af37; border: none; padding: 5px 10px; border-radius: 5px;">تحديث</button>
            </form>
        </div>
    </body>
    </html>
    ''', current_rate=app_stats["market_rate"], total_visits=app_stats["total_visits"])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
