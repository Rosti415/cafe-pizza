from flask import Flask, render_template
from sql_queries import CafeDB

app = Flask(__name__) #ств веб-додаток flask
db = CafeDB("shop.db")

@app.route("/")#вказуєм url для виклику функції
def main_page():
    categories = db.get_all_categories()
    return render_template("index.html",categories=categories)#результат який відображається

@app.route("/dish")
def dish():
    categories = db.get_all_categories()
    products = db.get_all_products()
    print(products)
    return render_template("dishes.html",products=products,categories=categories)

@app.route("/drink")
def drink():
    categories = db.get_all_categories()
    products = db.get_all_products()
    print(products)
    return render_template("drink.html", products=products,categories=categories)

@app.route("/order")
def order():
    categories = db.get_all_categories()
    return render_template("order.html",categories=categories)

@app.route("/help")
def support():
    categories = db.get_all_categories()
    return render_template("support.html",categories=categories)




if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True)#запускаємо веб-сервер з цього файлу