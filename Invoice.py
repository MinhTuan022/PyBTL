from datetime import datetime


class InvoiceItem:
    def __init__(self, product_code, product_name, quantity, unit_price, total_price):
        self.product_code = product_code
        self.product_name = product_name
        self.quantity = quantity
        self.unit_price = unit_price
        self.total_price = total_price


class Invoice:
    def __init__(self, invoice_code, invoice_date):
        self.invoice_code = invoice_code
        self.invoice_date = invoice_date
        self.items = []

    def add_item(self, product_code, product_name, quantity, unit_price, total_price):
        item = InvoiceItem(product_code, product_name, quantity, unit_price, total_price)
        self.items.append(item)

    def calculate_total(self):
        return sum(item.total_price for item in self.items)

    def display_invoice_info(self):
        print("Invoice Code: {}".format(self.invoice_code))
        print("Invoice Date: {}".format(self.invoice_date.strftime('%Y-%m-%d')))
        print("\nProduct List:")
        print("{:<15} {:<20} {:<15} {:<15} {:<15}".format(
            "Product Code", "Product Name", "Quantity Sold", "Selling Price", "Total Price"))
        print("-" * 80)
        for item in self.items:
            print("{:<15} {:<20} {:<15} {:<15} {:<15}".format(
                item.product_code, item.product_name, item.quantity,
                item.unit_price, item.total_price))
        print("\nTotal Amount: {}".format(self.calculate_total()))