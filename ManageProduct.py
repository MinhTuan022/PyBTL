from datetime import datetime

from Invoice import Invoice
from Product import Product


class ManageProduct:
    def __init__(self):
        self.products = []
        self.invoices = []

    def add_product(self, product):
        self.products.append(product)

    def find_product(self, product_code):
        for product in self.products:
            if product.product_code == product_code:
                return product
        return None

    def display_products(self):
        print("\nProduct List:")
        print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(
            "Code", "Name", "Selling Price", "Purchase Price", "Quantity", "Production Date", "Expiration Date"))
        print("-" * 130)
        for product in self.products:
            print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(
                product.product_code, product.product_name, product.selling_price, product.buying_price,
                product.quantity, product.manufacture_date, product.expiration_date))

    def edit_product(self, product_code, new_product_info):
        product = self.find_product(product_code)
        if product:
            for key, value in new_product_info.items():
                setattr(product, key, value)
            print("Thông tin sản phẩm đã được cập nhật.")
        else:
            print("Không tìm thấy sản phẩm.")

    def delete_product(self, product_code):
        product = self.find_product(product_code)
        if product:
            self.products.remove(product)
            print("Sản phẩm đã được xoá khỏi danh sách.")
        else:
            print("Không tìm thấy sản phẩm.")

    def add_invoice(self, invoice):
        self.invoices.append(invoice)

    # def calculate_daily_revenue(self, date):
    #     total_revenue = {}
    #     for invoice in self.invoices:
    #         if invoice.invoice_date.date() == date.date():
    #             for item in invoice.items:
    #                 if item.product_code not in total_revenue:
    #                     total_revenue[item.product_code] = 0
    #                 total_revenue[item.product_code] += item.total_price
    #     return total_revenue

    def sort_product_revenue(self, reverse=False):
        product_revenue = {}
        for invoice in self.invoices:
            for item in invoice.items:
                if item.product_code not in product_revenue:
                    product_revenue[item.product_code] = 0
                product_revenue[item.product_code] += item.total_price
        sorted_products = sorted(product_revenue.items(), key=lambda x: x[1], reverse=reverse)
        return sorted_products

    def display_top_products(self, n, reverse=False):
        sorted_products = self.sort_product_revenue(reverse)
        print(f"Top {n} Products by Revenue:")
        for i in range(min(n, len(sorted_products))):
            product_code, revenue = sorted_products[i]
            print(f"Product Code: {product_code}, Revenue: {revenue}")

    def display_near_expiry(self, weeks_remaining):
        today = datetime.now()
        near_expiry_products = [product for product in self.products if
                                (product.expiration_date - today).days // 7 == weeks_remaining]
        if near_expiry_products:
            print(f"Hàng hết hạn trong {weeks_remaining} tuần:")
            for product in near_expiry_products:
                print(
                    f"Product Code: {product.product_code}, Product Name: {product.product_name}, Expiry Date: {product.expiration_date}")
        else:
            print("Không có sản phẩm nào sắp hết hạn.")

    def calculate_daily_revenue(self, date):
        total_revenue = 0
        for invoice in self.invoices:
            if datetime.strptime(invoice.invoice_date, '%Y-%m-%d') == date:
                total_revenue += invoice.calculate_total()
        return total_revenue

    def display_expired_products(self):
        today = datetime.now()
        soon_to_expire = []
        for product in self.products:
            days_to_expire = (datetime.strptime(product.expiration_date, '%Y-%m-%d') - today).days
            if days_to_expire <= 42 and days_to_expire > 0:
                if days_to_expire <= 21:
                    product_price = product.selling_price * 0.431
                else:
                    product_price = product.selling_price * 0.725
                soon_to_expire.append((product.product_code, product.product_name, product_price))
        if soon_to_expire:
            print("Products soon to expire:")
            for product in soon_to_expire:
                print(f"Product Code: {product[0]}, Product Name: {product[1]}, New Price: {product[2]}")
