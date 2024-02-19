from flask import Flask, render_template,request
from sql_queries import CafeDB
import os


app = Flask(__name__) #ств веб-додаток flask
app.config['SECRET_KEY'] = "fndsfdslfjkasnfl"
PATH = os.path.dirname(__file__) + os.sep

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



@app.route("/category/<category_id>")
def products_by_categories(category_id):
    categories = db.get_all_categories()
    products = db.get_products_by_category(int(category_id))
    return render_template("category_product.html",categories=categories,products = products)

@app.route("/neworder/<product_id>",methods = ["POST","GET"])
def order(product_id):
    categories = db.get_all_categories()
    product = db.get_product(product_id)
    if request.method == "POST":
        db.order(product_id,request.form['name'],request.form['addres'],request.form['quantity'],request.form['phone'],request.form['comment'])

    return render_template("order.html",categories=categories,product=product)


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True)#запускаємо веб-сервер з цього файлу