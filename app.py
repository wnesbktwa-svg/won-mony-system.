from flask import Flask, render_template_string, request
import datetime

app = Flask(__name__)

# الإحصائيات والأسعار (مبنية على آخر صور أرفقتها)
visitor_count = 25 
bank_price = 2707.71 # سعر المصرف من صورتك القديمة
black_market_price = 8.79 # السعر الموازي الحالي

@app.route('/', methods=['GET', 'POST'])
def home():
    global visitor_count, bank_price, black_market_price
    visitor_count += 1
    
    result_text = ""
    profit_diff = black_market_price - 4.85 # حساب فارق الربح تقريبياً
    
    # منطق الحاسبة
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
        <title>Won Mony Pro V21</title>
        <style>
            body { background-color: #000; color: #ffca28; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; padding: 15px; }
            .container { max-width: 450px; margin: auto; }
            .card { border: 2px solid #ffca28; border-radius: 15px; padding: 15px; margin-bottom: 15px; background: #111; }
            .price-box { background: #222; border-radius: 10px; padding: 10px; margin: 10px 0; border: 1px solid #333; }
            .label { color: #888; font-size: 14px; }
            .value { font-size: 22px; font-weight: bold; display: block; margin-top: 5px; }
            .bank { color: #4caf50; } /* لون أخضر لسعر المصرف */
            .market { color: #ffca28; } /* لون ذهبي للسوق السوداء */
            input { width: 70%; padding: 10px; border-radius: 8px; border: 1px solid #ffca28; background: #000; color: #fff; }
            button { background: #ffca28; color: #000; border: none; padding: 10px 20px; border-radius: 8px; font-weight: bold; cursor: pointer; margin-top: 10px; }
            .footer-info { font-size: 12px; color: #555; margin-top: 20px; }
            .ads-area { border: 1px dashed #555; padding: 20px; margin-top: 15px; color: #555; font-size: 14px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h2 style="color:#ffca28;">WON MONY PRO <span style="font-size:12px; color:#555;">V21</span></h2>
            
            <div class="card">
                <div class="price-box">
                    <span class="label">سعر المصرف</span>
                    <span class="value bank">{{ bank_p }} د.ل</span>
                </div>
                <div class="price-box">
                    <span class="label">السوق الموازي (الكاش)</span>
                    <span class="value market">{{ market_p }} د.ل</span>
                </div>
                <div class="price-box">
                    <span class="label">فارق الربح التقريبي</span>
                    <span class="value" style="color:#fff;">{{ diff|round(2) }} د.ل</span>
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

            <div class="ads-area">مساحة إعلانية جاهزة للربح الآلي (Adsterra)</div>

            <div class="footer-info">
                إحصائيات الزيارات اليوم: {{ visitors }} <br>
                آخر تحديث للسيرفر: {{ time }}
            </div>
        </div>
    </body>
    </html>
    """
    last_time = datetime.datetime.now().strftime("%H:%M:%S")
    return render_template_string(html_template, bank_p=bank_price, market_p=black_market_price, 
                                 diff=profit_diff, visitors=visitor_count, time=last_time, 
                                 res=result_text, amount=amount)

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
