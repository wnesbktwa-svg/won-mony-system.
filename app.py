from flask import Flask, render_template_string, request
import datetime

app = Flask(__name__)

# قاعدة بيانات التطبيق (الأسعار الحالية)
data = {
    'visitor_count': 31,
    'bank_price': 2707.71,
    'market_price': 8.79,
    'gold_18': 415.00,
    'gold_24': 485.00,
    'last_update': datetime.datetime.now().strftime("%H:%M:%S")
}

@app.route('/', methods=['GET', 'POST'])
def home():
    global data
    # 1. منطق تحديث الأسعار (لوحة الإدارة)
    if request.method == 'POST' and 'update_price' in request.form:
        new_p = request.form.get('new_market_price')
        new_g = request.form.get('new_gold_price')
        if new_p: data['market_price'] = float(new_p)
        if new_g: data['gold_18'] = float(new_g)
        data['last_update'] = datetime.datetime.now().strftime("%H:%M:%S")

    # 2. منطق الحاسبة
    result_text = ""
    amount = request.form.get('amount', '')
    if request.method == 'POST' and amount and 'calc' in request.form:
        try:
            total = float(amount) * data['market_price']
            result_text = f"القيمة الإجمالية: {total:.2f} د.ل"
        except: result_text = "خطأ في الإدخال!"

    # 3. واجهة المستخدم HTML + CSS + JS
    html_template = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Won Mony Pro V23.5 - السكربت الشامل</title>
        
        <script type='text/javascript' src='https://pl28441931.effectivegatecpm.com/09/6d/f2/096df26bc56135a70590947b2dd0347d.js'></script>
        
        <style>
            body { background-color: #000; color: #ffca28; font-family: 'Arial', sans-serif; text-align: center; margin: 0; padding-bottom: 50px; }
            .navbar { display: flex; justify-content: space-around; background: #111; padding: 15px; border-bottom: 2px solid #ffca28; position: sticky; top: 0; z-index: 1000; }
            .nav-link { color: #ffca28; text-decoration: none; font-weight: bold; font-size: 14px; }
            .container { max-width: 480px; margin: auto; padding: 15px; }
            .card { border: 2px solid #ffca28; border-radius: 20px; padding: 20px; margin-bottom: 20px; background: #111; box-shadow: 0 0 10px rgba(255, 202, 40, 0.2); }
            .price-row { display: flex; justify-content: space-between; background: #222; padding: 10px; border-radius: 10px; margin: 5px 0; border: 1px solid #333; }
            .val { font-weight: bold; color: #fff; }
            input { width: 70%; padding: 12px; border-radius: 10px; border: 1px solid #ffca28; background: #000; color: #fff; margin: 10px 0; }
            button { background: #ffca28; color: #000; border: none; padding: 12px 25px; border-radius: 10px; font-weight: bold; cursor: pointer; width: 80%; }
            .admin-section { border: 1px dashed #444; padding: 15px; margin-top: 40px; font-size: 12px; border-radius: 10px; }
        </style>
    </head>
    <body>
        <nav class="navbar">
            <a href="#" class="nav-link">📈 العملات</a>
            <a href="#calc" class="nav-link">🧮 الحاسبة</a>
            <a href="#gold" class="nav-link">🟡 الذهب</a>
        </nav>

        <div class="container">
            <h1 style="font-size: 22px;">WON MONY PRO <span style="color:#fff">V23.5</span></h1>
            
            <div class="card">
                <div class="price-row">
                    <span>السوق الموازي (كاش)</span>
                    <span class="val">{{ d.market_price }} د.ل</span>
                </div>
                <div class="price-row">
                    <span>سعر المصرف المركزي</span>
                    <span class="val" style="color: #4caf50;">{{ d.bank_price }} د.ل</span>
                </div>
                <small style="color:#666">آخر تحديث للسعر: {{ d.last_update }}</small>
            </div>

            <div class="card" id="gold">
                <h3 style="margin-top:0">🟡 أسعار الذهب (جرام)</h3>
                <div class="price-row">
                    <span>عيار 18 (كسر)</span>
                    <span class="val">{{ d.gold_18 }} د.ل</span>
                </div>
                <div class="price-row">
                    <span>عيار 24 (جديد)</span>
                    <span class="val">{{ d.gold_24 }} د.ل</span>
                </div>
            </div>

            <div class="card" id="calc">
                <h3>🧮 حاسبة الدولار</h3>
                <form method="POST">
                    <input type="number" name="amount" step="any" placeholder="المبلغ بالدولار" value="{{ amount }}">
                    <button type="submit" name="calc">تحويل للدينار</button>
                </form>
                {% if res %}<p style="color:#4caf50; font-weight:bold; margin-top:15px;">{{ res }}</p>{% endif %}
            </div>

            <div class="admin-section">
                <p>⚙️ لوحة الإدارة (تحديث الأسعار)</p>
                <form method="POST">
                    <input type="number" name="new_market_price" step="0.01" placeholder="سعر الدولار الجديد" style="width: 40%; font-size:10px;">
                    <input type="number" name="new_gold_price" step="0.1" placeholder="سعر الذهب الجديد" style="width: 40%; font-size:10px;">
                    <button type="submit" name="update_price" style="width: 90%; background:#333; color:#fff; padding:5px;">حفظ التغييرات</button>
                </form>
                <p style="margin-top:10px">إجمالي الزيارات: {{ d.visitor_count + 1 }}</p>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template, d=data, res=result_text, amount=amount)

@app.route('/health')
def health(): return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
