from datetime import datetime


class Product:
    def __init__(self, product_code, product_name, selling_price, buying_price, quantity, manufacture_date,
                 expiration_date):
        self.product_code = product_code
        self.product_name = product_name
        self.selling_price = selling_price
        self.buying_price = buying_price
        self.quantity = quantity
        self.manufacture_date = manufacture_date
        self.expiration_date = expiration_date
