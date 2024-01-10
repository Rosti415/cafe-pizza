from flask import Flask, render_template

app = Flask(__name__) #ств веб-додаток flask

@app.route("/")#вказуєм url для виклику функції
def main_page():
    return render_template("index.html")#результат який відображається






if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True)#запускаємо веб-сервер з цього файлу