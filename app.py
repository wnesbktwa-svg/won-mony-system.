from flask import Flask, render_template_string, request
import datetime

app = Flask(__name__)

# قاعدة البيانات الحالية
data = {
    'bank': 2707.71,
    'market': 8.79,
    'gold_18': 415.00,
    'gold_24': 485.00,
    'visitors': 65, # تحديث بناءً على صورتك الأخيرة
    'time': datetime.datetime.now().strftime("%H:%M:%S")
}

@app.route('/', methods=['GET', 'POST'])
def home():
    global data
    res = ""
    # تحديث الأسعار من لوحة الإدارة
    if request.method == 'POST' and 'upd' in request.form:
        if request.form.get('m'): data['market'] = float(request.form.get('m'))
        if request.form.get('g'): data['gold_18'] = float(request.form.get('g'))
    
    # حساب الدولار
    amount = request.form.get('amt', '')
    if request.method == 'POST' and amount and 'calc' in request.form:
        res = f"الإجمالي: {float(amount) * data['market']:.2f} د.ل"

    html = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>WON MONY PRO V24</title>
        <script type='text/javascript' src='https://pl28441931.effectivegatecpm.com/09/6d/f2/096df26bc56135a70590947b2dd0347d.js'></script>
        <style>
            body { background:#000; color:#ffca28; font-family:sans-serif; margin:0; text-align:center; }
            .nav { display:flex; justify-content:space-around; background:#111; padding:15px; border-bottom:2px solid #ffca28; position:sticky; top:0; }
            .nav a { color:#ffca28; text-decoration:none; font-weight:bold; font-size:13px; }
            .container { padding:15px; max-width:450px; margin:auto; }
            .card { background:#111; border:2px solid #ffca28; border-radius:15px; padding:15px; margin-bottom:15px; }
            .row { display:flex; justify-content:space-between; background:#222; padding:10px; border-radius:8px; margin:5px 0; }
            input { width:70%; padding:10px; border-radius:8px; border:1px solid #ffca28; background:#000; color:#fff; margin:10px 0; }
            button { background:#ffca28; color:#000; border:none; padding:10px 20px; border-radius:8px; font-weight:bold; cursor:pointer; }
            .admin { border:1px dashed #444; padding:10px; margin-top:30px; font-size:11px; }
        </style>
    </head>
    <body>
        <div class="nav">
            <a href="#prices">📈 الأسعار</a>
            <a href="#gold">🟡 الذهب</a>
            <a href="#calc">🧮 الحاسبة</a>
        </div>
        <div class="container">
            <h2 id="prices">WON MONY PRO <span style="color:#fff">V24</span></h2>
            <div class="card">
                <div class="row"><span>السوق الموازي</span><span style="color:#fff; font-weight:bold;">{{d.market}} د.ل</span></div>
                <div class="row"><span>سعر المصرف</span><span style="color:#4caf50;">{{d.bank}} د.ل</span></div>
            </div>
            <div class="card" id="gold">
                <h3>أسعار الذهب (جرام)</h3>
                <div class="row"><span>عيار 18 (كسر)</span><span style="color:#fff;">{{d.gold_18}} د.ل</span></div>
                <div class="row"><span>عيار 24 (جديد)</span><span style="color:#fff;">{{d.gold_24}} د.ل</span></div>
            </div>
            <div class="card" id="calc">
                <h3>حاسبة العملات</h3>
                <form method="POST"><input type="number" name="amt" step="any" placeholder="المبلغ بالدولار" value="{{a}}">
                <button type="submit" name="calc">تحويل</button></form>
                {% if r %}<p style="color:#4caf50;">{{r}}</p>{% endif %}
            </div>
            <div class="admin">
                <p>⚙️ لوحة الإدارة</p>
                <form method="POST">
                    <input type="number" name="m" step="0.01" placeholder="سعر دولار جديد" style="width:40%">
                    <input type="number" name="g" step="0.1" placeholder="سعر ذهب جديد" style="width:40%">
                    <button type="submit" name="upd" style="width:90%; background:#333; color:#fff;">تحديث الكل</button>
                </form>
                <p>الزيارات: {{d.visitors}} | الوقت: {{d.time}}</p>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, d=data, r=res, a=amount)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
