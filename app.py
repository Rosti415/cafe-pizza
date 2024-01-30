from flask import Flask, render_template
from sql_queries import CafeDB

app = Flask(__name__) #ств веб-додаток flask
db = CafeDB("shop.db")

@app.route("/")#вказуєм url для виклику функції
def main_page():
    return render_template("index.html")#результат який відображається

@app.route("/dish")
def dish():
    products = db.get_all_products()
    print(products)
    return render_template("dishes.html")

@app.route("/drink")
def drink():
    return render_template("drink.html")

@app.route("/order")
def order():
    return render_template("order.html")

@app.route("/help")
def support():
    return render_template("support.html")




if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True)#запускаємо веб-сервер з цього файлу