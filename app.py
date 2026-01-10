
from flask import Flask, render_template_string, request
import datetime

app = Flask(__name__)

# الأسعار الحالية (يمكنك تعديلها من لوحة الإدارة بالأسفل)
data = {
    'visitor_count': 31,
    'bank_price': 2707.71,
    'market_price': 8.79,
    'last_update': datetime.datetime.now().strftime("%H:%M:%S")
}

@app.route('/', methods=['GET', 'POST'])
def home():
    # تحديث الأسعار من لوحة الإدارة
    if request.method == 'POST' and 'update_price' in request.form:
        new_price = request.form.get('new_market_price')
        if new_price:
            data['market_price'] = float(new_price)
            data['last_update'] = datetime.datetime.now().strftime("%H:%M:%S")

    # منطق الحاسبة
    result_text = ""
    amount = request.form.get('amount', '')
    if request.method == 'POST' and amount and 'calc' in request.form:
        try:
            total = float(amount) * data['market_price']
            result_text = f"القيمة: {total:.2f} د.ل"
        except: result_text = "خطأ!"

    html_template = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Won Mony Pro V23</title>
        
        <script type='text/javascript' src='https://pl28441931.effectivegatecpm.com/09/6d/f2/096df26bc56135a70590947b2dd0347d.js'></script>
        
        <style>
            body { background-color: #000; color: #ffca28; font-family: sans-serif; text-align: center; padding: 10px; margin: 0; }
            .nav-menu { display: flex; justify-content: space-around; background: #111; padding: 10px; border-bottom: 1px solid #ffca28; position: sticky; top: 0; z-index: 100; }
            .nav-item { color: #ffca28; text-decoration: none; font-size: 14px; font-weight: bold; cursor: pointer; }
            .container { max-width: 450px; margin: auto; padding-top: 15px; }
            .card { border: 2px solid #ffca28; border-radius: 15px; padding: 15px; margin-bottom: 15px; background: #111; }
            .price-box { background: #222; border-radius: 10px; padding: 10px; margin: 5px 0; border: 1px solid #333; }
            .bank { color: #4caf50; font-size: 20px; font-weight: bold; }
            input { width: 60%; padding: 10px; border-radius: 8px; border: 1px solid #ffca28; background: #000; color: #fff; }
            button { background: #ffca28; color: #000; border: none; padding: 10px 15px; border-radius: 8px; font-weight: bold; }
            .admin-panel { border: 1px dashed #555; padding: 10px; margin-top: 50px; font-size: 12px; }
        </style>
    </head>
    <body>
        <div class="nav-menu">
            <div class="nav-item" onclick="alert('أنت الآن تشاهد الأسعار مباشرة')">📈 الأسعار</div>
            <div class="nav-item" onclick="document.getElementById('calc-sec').scrollIntoView()">🧮 الحاسبة</div>
            <div class="nav-item" onclick="alert('سيتم إضافة تداول الذهب قريباً!')">🟡 الذهب</div>
        </div>

        <div class="container">
            <h2 style="margin:5px;">WON MONY PRO V23</h2>
            
            <div class="card">
                <div class="price-box">
                    <small>سعر المصرف الرسمي</small><br>
                    <span class="bank">{{ data.bank_price }} د.ل</span>
                </div>
                <div class="price-box">
                    <small>السوق الموازي (الكاش)</small><br>
                    <span style="font-size:24px; font-weight:bold;">{{ data.market_price }} د.ل</span>
                </div>
                <div style="font-size:11px; color:#666; margin-top:5px;">تحديث: {{ data.last_update }}</div>
            </div>

            <div class="card" id="calc-sec">
                <p>حاسبة التحويل السريع</p>
                <form method="POST">
                    <input type="number" name="amount" placeholder="المبلغ بالدولار" value="{{ amount }}">
                    <button type="submit" name="calc">إحسب</button>
                </form>
                {% if res %}<div style="color:#4caf50; margin-top:10px;">{{ res }}</div>{% endif %}
            </div>

            <div class="admin-panel">
                <p>⚙️ إدارة النظام (خاص بك فقط)</p>
                <form method="POST">
                    <input type="number" name="new_market_price" step="0.01" placeholder="تغيير سعر السوق">
                    <button type="submit" name="update_price" style="background:#444; color:#fff;">تحديث</button>
                </form>
                <small>إجمالي الزيارات اليوم: {{ data.visitor_count + 1 }}</small>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template, data=data, res=result_text, amount=amount)

@app.route('/health')
def health(): return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
