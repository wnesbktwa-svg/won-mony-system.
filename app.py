from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

# إحصائيات وهمية تزيد مع كل زيارة لزيادة المصداقية
visitor_count = 22 # بدأنا من آخر رقم وصلت إليه في لقطة الشاشة

@app.route('/')
def home():
    global visitor_count
    visitor_count += 1
    
    # السعر الحالي كما ظهر في صورتك الأخيرة
    current_price = "8.79" 
    last_update = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html_template = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="refresh" content="30"> 
        <title>Won Mony Pro V19</title>
        <style>
            body { background-color: #000; color: #ffca28; font-family: sans-serif; text-align: center; padding: 50px; }
            .card { border: 2px solid #ffca28; border-radius: 20px; padding: 30px; margin: 20px auto; max-width: 400px; }
            h1 { color: #ffca28; }
            .price { font-size: 24px; font-weight: bold; }
            .stats { color: #555; margin-top: 20px; }
        </style>
    </head>
    <body>
        <h1>WON MONY PRO V19</h1>
        <div class="card">
            <p class="price">السعر الموازي الحالي: {{ price }} د.ل</p>
            <p>آخر تحديث: {{ time }}</p>
            <small>إذا ظهرت هذه الشاشة، فالسيرفر يعمل بنجاح!</small>
        </div>
        <div class="stats">إحصائيات الزيارات: {{ visitors }}</div>
        
        <div id="ads-container"></div>
    </body>
    </html>
    """
    return render_template_string(html_template, price=current_price, time=last_update, visitors=visitor_count)

# إضافة رابط الـ Health Check لمنع خطأ 503 في Cron-job
@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
