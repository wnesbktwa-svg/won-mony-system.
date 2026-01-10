from flask import Flask, render_template_string, request
import datetime

app = Flask(__name__)

# الإحصائيات الحالية (سنستمر من حيث توقفت في الصورة الأخيرة)
visitor_count = 25 
exchange_rate = 8.79 # السعر الذي ظهر في صورتك الأخيرة

@app.route('/', methods=['GET', 'POST'])
def home():
    global visitor_count, exchange_rate
    visitor_count += 1
    
    result = ""
    amount = ""
    
    # منطق الحاسبة
    if request.method == 'POST':
        try:
            amount = request.form.get('amount')
            if amount:
                converted = float(amount) * exchange_rate
                result = f"{amount} دولار = {converted:.2f} دينار"
        except:
            result = "خطأ في الإدخال!"

    html_template = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Won Mony Pro V20 - الحاسبة</title>
        <style>
            body { background-color: #000; color: #ffca28; font-family: sans-serif; text-align: center; padding: 20px; }
            .card { border: 2px solid #ffca28; border-radius: 20px; padding: 20px; margin: 10px auto; max-width: 400px; box-shadow: 0 0 15px #ffca28; }
            input { width: 80%; padding: 10px; border-radius: 10px; border: 1px solid #ffca28; background: #222; color: #fff; margin: 10px 0; }
            button { background: #ffca28; color: #000; border: none; padding: 10px 20px; border-radius: 10px; font-weight: bold; cursor: pointer; }
            .result { font-size: 20px; margin-top: 15px; color: #fff; background: #333; padding: 10px; border-radius: 10px; }
        </style>
    </head>
    <body>
        <h1>WON MONY PRO V20</h1>
        
        <div class="card">
            <h3>سعر السوق الحالي: {{ price }} د.ل</h3>
            <form method="POST">
                <p>حاسبة التحويل السريع:</p>
                <input type="number" name="amount" step="any" placeholder="أدخل القيمة بالدولار" value="{{ amount }}">
                <button type="submit">تحويل</button>
            </form>
            {% if result %}
            <div class="result">{{ result }}</div>
            {% endif %}
        </div>

        <div style="margin-top: 20px;">
            <small>إحصائيات الزيارات: {{ visitors }}</small><br>
            <small>آخر تحديث للسيرفر: 15:04:00</small>
        </div>

        </body>
    </html>
    """
    return render_template_string(html_template, price=exchange_rate, visitors=visitor_count, result=result, amount=amount)

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
