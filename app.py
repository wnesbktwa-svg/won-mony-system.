from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Won Mony - Currency Converter</title>
        <style>
            body { background: #000; color: #fff; font-family: sans-serif; text-align: center; padding: 15px; }
            .header { color: #00ff00; margin-bottom: 20px; text-shadow: 0 0 10px #00ff00; }
            
            .converter-box {
                background: #0a0a0a; border: 2px solid #00ff00; border-radius: 20px;
                padding: 25px; max-width: 400px; margin: 0 auto 30px; box-shadow: 0 0 20px rgba(0,255,0,0.2);
            }
            
            input {
                width: 90%; padding: 15px; border-radius: 12px; border: 1px solid #333;
                background: #111; color: #fff; font-size: 20px; text-align: center; margin-top: 10px;
            }
            
            .currency-list { 
                display: grid; grid-template-columns: repeat(auto-fill, minmax(130px, 1fr)); 
                gap: 15px; max-width: 900px; margin: auto; 
            }
            
            .currency-item { 
                background: #111; border: 1px solid #222; padding: 15px; 
                border-radius: 15px; transition: 0.3s;
            }
            
            .code { color: #00ff00; font-weight: bold; font-size: 16px; margin-bottom: 5px; }
            .result { font-size: 20px; font-weight: bold; color: #fff; }
            .label { font-size: 12px; color: #666; }
        </style>
        <script>
            let rates = {};

            async function loadData() {
                try {
                    const res = await fetch('https://open.er-api.com/v6/latest/USD');
                    const data = await res.json();
                    rates = data.rates;
                    convert(1); // البدء بـ 1 دولار كافتراضي
                } catch (e) {
                    document.getElementById('list').innerHTML = 'خطأ في الاتصال بالسوق العالمي';
                }
            }

            function convert(amount) {
                if(!amount || amount < 0) amount = 0;
                const listDiv = document.getElementById('list');
                listDiv.innerHTML = '';
                
                // قائمة العملات التي تهمنا أولاً
                const priority = ['LYD', 'EUR', 'GBP', 'SAR', 'EGP', 'TRY', 'AED', 'KWD'];
                
                // عرض العملات المفضلة أولاً
                priority.forEach(code => {
                    if(rates[code]) createCard(code, rates[code] * amount);
                });

                // عرض باقي العملات
                for (let code in rates) {
                    if(!priority.includes(code)) createCard(code, rates[code] * amount);
                }
            }

            function createCard(code, value) {
                const item = document.createElement('div');
                item.className = 'currency-item';
                item.innerHTML = `
                    <div class="code">${code}</div>
                    <div class="result">${value.toLocaleString(undefined, {maximumFractionDigits: 2})}</div>
                    <div class="label">القيمة المحولة</div>
                `;
                document.getElementById('list').appendChild(item);
            }

            window.onload = loadData;
        </script>
    </head>
    <body>
        <h2 class="header">WON MONY CONVERTER</h2>
        
        <div class="converter-box">
            <div class="label">أدخل المبلغ بالدولار الأمريكي (USD)</div>
            <input type="number" id="usd-input" placeholder="100" oninput="convert(this.value)">
        </div>

        <div id="list" class="currency-list">
            <p style="color:#f7931a;">جاري تجهيز بيانات البنك المركزي...</p>
        </div>

        <div style="margin-top: 50px; color: #333; font-size: 10px; line-height: 1.6;">
            نظام Won Mony V12 السحابي<br>
            يتم تحديث أسعار الصرف العالمية كل ساعة تلقائياً
        </div>
    </body>
    </html>
    ''')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
