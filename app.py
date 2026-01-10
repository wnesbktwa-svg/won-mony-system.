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
        <title>Won Mony - Libya Market</title>
        <style>
            body { background: #000; color: #fff; font-family: sans-serif; text-align: center; padding: 15px; }
            .header { color: #00ff00; margin-bottom: 20px; }
            .box {
                background: #0a0a0a; border: 2px solid #00ff00; border-radius: 20px;
                padding: 20px; max-width: 400px; margin: 0 auto 20px;
            }
            input {
                width: 85%; padding: 12px; border-radius: 10px; border: 1px solid #333;
                background: #111; color: #fff; font-size: 22px; text-align: center;
            }
            .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; max-width: 400px; margin: auto; }
            .result-card { background: #111; padding: 15px; border-radius: 15px; border: 1px solid #222; }
            .official { color: #00ff00; font-size: 20px; font-weight: bold; }
            .black-market { color: #f7931a; font-size: 20px; font-weight: bold; }
            .label { font-size: 12px; color: #666; margin-bottom: 5px; }
            .footer { margin-top: 30px; font-size: 11px; color: #444; }
        </style>
        <script>
            let officialRate = 0;
            const blackMarketRate = 8.77; // السعر الذي جلبناه من عين ليبيا

            async function loadRates() {
                try {
                    const res = await fetch('https://open.er-api.com/v6/latest/USD');
                    const data = await res.json();
                    officialRate = data.rates.LYD;
                    updateValues(100); // القيمة الافتراضية
                } catch (e) { console.log("Error loading rates"); }
            }

            function updateValues(usd) {
                if(!usd) usd = 0;
                // الحساب الرسمي
                document.getElementById('off-val').innerText = (usd * officialRate).toLocaleString() + ' د.ل';
                // حساب السوق الموازي
                document.getElementById('bm-val').innerText = (usd * blackMarketRate).toLocaleString() + ' د.ل';
                // حساب الفرق (مكسب التاجر)
                const diff = (usd * blackMarketRate) - (usd * officialRate);
                document.getElementById('diff-val').innerText = diff.toLocaleString() + ' د.ل';
            }

            window.onload = loadRates;
        </script>
    </head>
    <body>
        <h2 class="header">WON MONY - حاسبة السوق</h2>
        
        <div class="box">
            <div class="label">أدخل المبلغ بالدولار (USD)</div>
            <input type="number" id="input" placeholder="100" oninput="updateValues(this.value)">
        </div>

        <div class="grid">
            <div class="result-card">
                <div class="label">السعر الرسمي (البنك)</div>
                <div id="off-val" class="official">...</div>
            </div>
            <div class="result-card">
                <div class="label">السوق الموازي (كاش)</div>
                <div id="bm-val" class="black-market">...</div>
            </div>
        </div>

        <div class="box" style="margin-top:20px; border-color: #555;">
            <div class="label">فارق السعر (الربح التقريبي)</div>
            <div id="diff-val" style="font-size: 24px; color: white;">...</div>
        </div>

        <div class="footer">
            تم الربط آلياً بأسعار الصرف العالمية<br>
            تحديث السوق المحلي: عين ليبيا
        </div>
    </body>
    </html>
    ''')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
