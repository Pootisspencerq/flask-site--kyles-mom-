from flask import Flask, render_template
from db import DatabaseManager

app = Flask(__name__)  # Створюємо веб–додаток Flask
db = DatabaseManager("data.db")

@app.route("/")  # Вказуємо url-адресу для виклику функції
def index():
    articles = db.get_all_articles()
    
    return render_template("index.html", articles=articles)  # html-сторінка, що повертається у браузер


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True)  # Запускаємо веб-сервер з цього файлу в режимі налагодження