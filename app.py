from flask import Flask, render_template_string, request
import datetime

app = Flask(__name__)

# الإحصائيات (مستمرة من آخر رقم حققته 31 زيارة)
visitor_count = 31 
bank_price = 2707.71 
black_market_price = 8.79 

@app.route('/', methods=['GET', 'POST'])
def home():
    global visitor_count, bank_price, black_market_price
    visitor_count += 1
    
    result_text = ""
    profit_diff = black_market_price - 4.85 # حسب بياناتك السابقة
    
    amount = request.form.get('amount', '')
    if request.method == 'POST' and amount:
        try:
            total = float(amount) * black_market_price
            result_text = f"القيمة الإجمالية: {total:.2f} د.ل"
        except:
            result_text = "خطأ في الإدخال!"

    html_template = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Won Mony Pro V22 - فعال للربح</title>
        
        <script type='text/javascript' src='https://pl28441931.effectivegatecpm.com/09/6d/f2/096df26bc56135a70590947b2dd0347d.js'></script>
        
        <style>
            body { background-color: #000; color: #ffca28; font-family: sans-serif; text-align: center; padding: 15px; }
            .container { max-width: 450px; margin: auto; }
            .card { border: 2px solid #ffca28; border-radius: 15px; padding: 15px; margin-bottom: 15px; background: #111; }
            .price-box { background: #222; border-radius: 10px; padding: 10px; margin: 10px 0; border: 1px solid #333; }
            .label { color: #888; font-size: 14px; }
            .value { font-size: 22px; font-weight: bold; display: block; margin-top: 5px; }
            input { width: 70%; padding: 10px; border-radius: 8px; border: 1px solid #ffca28; background: #000; color: #fff; }
            button { background: #ffca28; color: #000; border: none; padding: 10px 20px; border-radius: 8px; font-weight: bold; cursor: pointer; margin-top: 10px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h2 style="color:#ffca28;">WON MONY PRO <span style="font-size:12px; color:#555;">V22</span></h2>
            
            <div class="card">
                <div class="price-box">
                    <span class="label">سعر المصرف</span>
                    <span class="value" style="color:#4caf50;">{{ bank_p }} د.ل</span>
                </div>
                <div class="price-box">
                    <span class="label">السوق الموازي (الكاش)</span>
                    <span class="value" style="color:#ffca28;">{{ market_p }} د.ل</span>
                </div>
            </div>

            <div class="card">
                <form method="POST">
                    <input type="number" name="amount" placeholder="أدخل المبلغ بالدولار" value="{{ amount }}">
                    <button type="submit">إحسب القيمة</button>
                </form>
                {% if res %}
                <div style="margin-top:15px; font-size:18px; color:#4caf50;">{{ res }}</div>
                {% endif %}
            </div>

            <div style="font-size: 12px; color: #555; margin-top: 20px;">
                إحصائيات الزيارات اليوم: {{ visitors }} <br>
                آخر تحديث للسيرفر: {{ time }}
            </div>
        </div>
    </body>
    </html>
    """
    last_time = datetime.datetime.now().strftime("%H:%M:%S")
    return render_template_string(html_template, bank_p=bank_price, market_p=black_market_price, 
                                 visitors=visitor_count, time=last_time, res=result_text, amount=amount)

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
