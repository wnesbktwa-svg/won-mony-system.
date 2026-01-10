from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

# بيانات السعر والزيارات
app_stats = {"total_visits": 0, "market_rate": 8.79}

@app.route('/', methods=['GET', 'POST'])
def home():
    app_stats["total_visits"] += 1
    if request.method == 'POST' and request.form.get('new_rate'):
        try: app_stats["market_rate"] = float(request.form.get('new_rate'))
        except: pass

    return render_template_string('''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Won Mony V18 - Fixed</title>
        
        <script type='text/javascript' src='https://pl28441931.effectiveratecpm.com/7d/5d/7c/7d5d7c80528441931.js'></script>
        
        <style>
            body { background: #000; color: #fff; font-family: sans-serif; text-align: center; padding: 10px; }
            .main-box { border: 2px solid #d4af37; border-radius: 20px; padding: 20px; max-width: 400px; margin: auto; background: #0a0a0a; }
            .val { font-size: 26px; font-weight: bold; }
            .gold { color: #d4af37; } .green { color: #0f0; }
        </style>
    </head>
    <body>
        <h2 class="gold">WON MONY PRO V18</h2>
        <div class="main-box">
            <p>السعر الموازي الحالي: <span class="gold">{{ market_rate }} د.ل</span></p>
            <div style="font-size: 12px; color: #555;">إذا ظهرت هذه الشاشة، فالسيرفر يعمل بنجاح!</div>
        </div>
        <div style="margin-top: 30px; font-size: 10px; color: #222;">
            إحصائيات الزيارات: {{ total_visits }}
        </div>
    </body>
    </html>
    ''', market_rate=app_stats["market_rate"], total_visits=app_stats["total_visits"])

if __name__ == "__main__":
    # هذا السطر مهم جداً لبيئة Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
