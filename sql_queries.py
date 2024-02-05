import sqlite3


class CafeDB():
    def __init__(self,dbname):
        self.dbname = dbname
        self.conn = None
        self.cursor = None

    def open(self):
        self.conn = sqlite3.connect(self.dbname) # підключаємося до бази данних
        self.cursor = self.conn.cursor()#створюємо курсор

    def close(self):
        self.cursor.close()
        self.conn.close()# закриваємо все в кінці коду

    def get_all_products(self):
        self.open()
        self.cursor.execute("SELECT * FROM products")
        data = self.cursor.fetchall()
        self.close()
        return data
    
    def get_products_by_category(self,category_id):
        self.open()
        self.cursor.execute("SELECT * FROM products WHERE category_id=(?)",[category_id])
        data = self.cursor.fetchall()
        self.close()
        return data
    
    def get_all_categories(self):
        self.open()
        self.cursor.execute("SELECT * FROM categories")
        data = self.cursor.fetchall()
        self.close()
        return data
