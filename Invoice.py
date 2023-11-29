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
        self.invoice_date = datetime.strptime(invoice_date, '%Y-%m-%d')
        self.items = []

    def add_item(self, product_code, product_name, quantity, unit_price, total_price):
        item = InvoiceItem(product_code, product_name, quantity, unit_price, total_price)
        self.items.append(item)

    def calculate_total(self):
        return sum(item.total_price for item in self.items)

    def display_invoice_info(self):
        print("\033[94m***Mã Hóa Đơn: {}***\033[0m".format(self.invoice_code))
        print("Ngày xuất hóa đơn: {}".format(self.invoice_date.strftime('%Y-%m-%d')))
        print("Danh sách sản phẩm:")
        print("{:<15} {:<20} {:<15} {:<15} {:<15}".format(
            "Mã Sản Phẩm", "Tên Sản Phẩm", "Số lượng bán", "Giá Bán", "Tổng Tiền"))
        print("-" * 80)
        for item in self.items:
            unit_price = f"{item.unit_price} VNĐ"
            total_price = f"{item.total_price} VNĐ"
            print("{:<15} {:<20} {:<15} {:<15} {:<15}".format(
                item.product_code, item.product_name, item.quantity,
                unit_price, total_price))
        print("\t\t\t\t\t\t\tTổng tiền hóa đơn: {} VNĐ\n".format(self.calculate_total()))