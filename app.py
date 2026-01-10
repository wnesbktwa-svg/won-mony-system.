from flask import Flask, render_template_string, request
import datetime

app = Flask(__name__)
# البيانات الأولية
d = {'m': 8.79, 'b': 2707.71, 'g18': 415.0, 'v': 65}

@app.route('/', methods=['GET', 'POST'])
def index():
    global d
    res = ""
    # لوحة الإدارة المخفية (تحديث الأسعار)
    if request.method == 'POST' and 'up' in request.form:
        if request.form.get('nm'): d['m'] = float(request.form.get('nm'))
        if request.form.get('ng'): d['g18'] = float(request.form.get('ng'))
    
    # الحاسبة
    amt = request.form.get('amt', '')
    if request.method == 'POST' and amt and 'cl' in request.form:
        res = f"الإجمالي: {float(amt) * d['m']:.2f} د.ل"

    html = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>WON MONY V25</title>
        <script type='text/javascript' src='https://pl28441931.effectivegatecpm.com/09/6d/f2/096df26bc56135a70590947b2dd0347d.js'></script>
        <style>
            body { background:#000; color:#ffca28; font-family:sans-serif; text-align:center; margin:0; }
            .nav { display:flex; justify-content:space-around; background:#111; padding:12px; border-bottom:1px solid #ffca28; position:sticky; top:0; }
            .nav a { color:#ffca28; text-decoration:none; font-size:12px; font-weight:bold; }
            .card { background:#111; border:1px solid #ffca28; border-radius:12px; padding:15px; margin:10px; }
            .row { display:flex; justify-content:space-between; margin:8px 0; font-size:18px; }
            input { width:80%; padding:10px; border-radius:8px; border:1px solid #ffca28; background:#000; color:#fff; }
            button { background:#ffca28; color:#000; border:none; padding:10px 20px; border-radius:8px; font-weight:bold; margin-top:10px; }
        </style>
    </head>
    <body>
        <div class="nav"><a href="#">📉 الأسعار</a><a href="#gold">🟡 الذهب</a><a href="#calc">🧮 الحاسبة</a></div>
        <div class="card">
            <h2>WON MONY PRO <span style="color:#fff">V25</span></h2>
            <div class="row"><span>الموازي</span><span>{{d.m}} د.ل</span></div>
            <div class="row"><span>المصرف</span><span style="color:#4caf50;">{{d.b}}</span></div>
        </div>
        <div class="card" id="gold">
            <h3>الذهب (جرام 18)</h3>
            <div class="row"><span>السعر</span><span>{{d.g18}} د.ل</span></div>
        </div>
        <div class="card" id="calc">
            <form method="POST"><input type="number" name="amt" placeholder="المبلغ بالدولار" value="{{a}}">
            <button type="submit" name="cl">إحسب القيمة</button></form>
            {% if r %}<p style="color:#4caf50;">{{r}}</p>{% endif %}
        </div>
        <div style="font-size:10px; color:#444; margin-top:20px; border:1px dashed #333; padding:10px;">
            لوحة الإدارة: <form method="POST">
            <input type="number" name="nm" placeholder="تحديث الدولار" style="width:30%">
            <input type="number" name="ng" placeholder="تحديث الذهب" style="width:30%">
            <button type="submit" name="up" style="font-size:10px; padding:5px;">تحديث</button></form>
            الزيارات: {{d.v}}
        </div>
    </body></html>
    """
    return render_template_string(html, d=d, r=res, a=amt)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
