
from flask import Flask, request, render_template_string, send_from_directory
import os
import requests

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="ru">
<head>
<meta name="google-site-verification" content="rIUQ1QwMR59d48ntAC2r2hSV7q-2hL7mAIfC_tr9Kcc" />
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CAR POINT — Выкуп автомобилей</title>
    <meta name="description" content="CAR POINT — быстрый и выгодный выкуп автомобилей в Москве и Московской области. Оценка автомобиля, оформление сделки и выплата денег в день обращения.">

<meta name="keywords" content="выкуп автомобилей, срочный выкуп авто, продать автомобиль, выкуп машин Москва, выкуп авто Московская область">
    <style>
        * { box-sizing: border-box; }
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #101010;
            color: white;
        }
        header {
            padding: 25px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #292929;
        }
        .logo { color: #d6a33b; font-size: 28px; font-weight: bold; }
        header span { color: #aaa; font-size: 13px; }
        .hero {
            padding: 100px 8%;
            min-height: 480px;
            background:
              linear-gradient(90deg, #101010 5%, rgba(16,16,16,.7)),
              url("https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?auto=format&fit=crop&w=1800&q=85");
            background-size: cover;
            background-position: center;
        }
        h1 { font-size: 50px; }
        h1 span { color: #d6a33b; }
        .hero p { color: #ccc; font-size: 19px; line-height: 1.6; }
        .button {
            display: inline-block;
            padding: 16px 28px;
            background: #d6a33b;
            color: #111;
            border: 0;
            border-radius: 4px;
            font-weight: bold;
            cursor: pointer;
            text-decoration: none;
        }
        .advantages, .request { padding: 55px 8%; text-align: center; }
        .items {
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
        }
        .item {
            background: #1c1c1c;
            padding: 25px;
            width: 240px;
            border: 1px solid #333;
            border-radius: 8px;
        }
        .item h3 { color: #d6a33b; }
        .request { background: #191919; }
        input {
            display: block;
            width: 100%;
            max-width: 400px;
            margin: 12px auto;
            padding: 15px;
            background: #252525;
            color: white;
            border: 1px solid #444;
            border-radius: 4px;
        }
        .success { color: #d6a33b; font-weight: bold; }
        footer { padding: 25px; text-align: center; color: #888; }
        @media (max-width: 600px) {
            h1 { font-size: 36px; }
            .hero { padding: 70px 6%; }
            header { padding: 20px 6%; }
        }
    </style>
</head>
<body>
<header>
    <div class="logo">CAR POINT</div>
    <span>МОСКВА И МО</span>
</header>

<section class="hero">
    <h1>ВЫКУП <span>АВТОМОБИЛЕЙ</span></h1>
    <p>Продадим ваш автомобиль быстро, удобно и без лишних хлопот.</p>
    <p>Бесплатная предварительная оценка автомобиля.</p>
    <a href="#request" class="button">ОСТАВИТЬ ЗАЯВКУ</a>
</section>


<section style="padding: 60px 20px; background: #0b0b0b; color: white; text-align: center;">
    <h2 style="color: #d4af37; margin-bottom: 35px;">
        Почему выбирают CAR POINT
    </h2>

    <div style="max-width: 900px; margin: auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;">

        <div style="border: 1px solid #d4af37; padding: 25px; border-radius: 12px;">
            <h3 style="color: #d4af37;">Быстрая оценка</h3>
            <p>Оценим ваш автомобиль и обсудим стоимость.</p>
        </div>

        <div style="border: 1px solid #d4af37; padding: 25px; border-radius: 12px;">
            <h3 style="color: #d4af37;">Быстрая сделка</h3>
            <p>Поможем организовать выкуп в удобное время.</p>
        </div>

        <div style="border: 1px solid #d4af37; padding: 25px; border-radius: 12px;">
            <h3 style="color: #d4af37;">Бесплатная оценка</h3>
            <p>Предварительная оценка автомобиля бесплатна.</p>
        </div>

        <div style="border: 1px solid #d4af37; padding: 25px; border-radius: 12px;">
            <h3 style="color: #d4af37;">Москва и область</h3>
            <p>Работаем с автомобилями в Москве и Московской области.</p>
        </div>

    </div>
</section><section class="steps" style="padding: 60px 20px; text-align: center; background: #111; color: white;">
    <h2 style="color: #d4af37;">Как проходит выкуп автомобиля</h2>

    <div style="max-width: 900px; margin: 30px auto; line-height: 1.8;">
        <p><strong style="color: #d4af37;">01. Оставляете заявку</strong><br>Указываете имя, телефон и информацию об автомобиле.</p>
        <p><strong style="color: #d4af37;">02. Получаете оценку</strong><br>Мы связываемся с вами и обсуждаем стоимость автомобиля.</p>
        <p><strong style="color: #d4af37;">03. Проводим осмотр</strong><br>Согласуем удобное время и место осмотра.</p>
        <p><strong style="color: #d4af37;">04. Получаете деньги</strong><br>После согласования оформляем сделку и производим выплату.</p>
    </div>
</section><section class="request" id="request">
    <h2>ОСТАВИТЬ ЗАЯВКУ</h2>
    <p>Расскажите нам о своём автомобиле</p>

    {% if success %}
        <p class="success">Заявка успешно отправлена! Мы скоро с вами свяжемся.</p>
    {% elif error %}
        <p style="color:#ff7777;">Не удалось отправить заявку. Попробуйте позже.</p>
    {% endif %}

    <form action="/send" method="POST">
        <input name="name" type="text" placeholder="Ваше имя" required>
        <input name="phone" type="tel" placeholder="Ваш номер телефона" required>
        <input name="car" type="text" placeholder="Марка и модель автомобиля" required>
        <button class="button" type="submit">ОТПРАВИТЬ ЗАЯВКУ</button>
    </form>
</section>

<footer>CAR POINT © 2026 | Москва и Московская область</footer>
</body>
</html>
"""
@app.route("/yandex_a2f950e3c2880a5b.html")
def yandex_verification():
    return send_from_directory(".", "yandex_a2f950e3c2880a5b.html")
@app.route("/")
def home():
    return render_template_string(HTML, success=False, error=False)

@app.route("/send", methods=["POST"])
def send():
    name = request.form.get("name", "").strip()
    phone = request.form.get("phone", "").strip()
    car = request.form.get("car", "").strip()

    if not name or not phone or not car:
        return render_template_string(HTML, success=False, error=True)

    token = os.environ.get("BOT_TOKEN")
    chat_id = os.environ.get("CHAT_ID")

    if not token or not chat_id:
        return render_template_string(HTML, success=False, error=True)

    message = (
        "🚗 НОВАЯ ЗАЯВКА — CAR POINT\n\n"
        f"Имя: {name}\n"
        f"Телефон: {phone}\n"
        f"Автомобиль: {car}"
    )

    try:
        response = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data={"chat_id": chat_id, "text": message},
            timeout=10
        )
        response.raise_for_status()

        if not response.json().get("ok"):
            raise RuntimeError("Telegram did not accept the message")

        return render_template_string(HTML, success=True, error=False)

    except (requests.RequestException, RuntimeError):
        return render_template_string(HTML, success=False, error=True)

if __name__ == "__main__":
    app.run(debug=True)
