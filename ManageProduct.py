from datetime import datetime


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
        if not self.products:
            print("\033[33mKhông có sản phẩm nào\033[0m")
        else:
            print("\n\033[34mDanh Sách Sản Phẩm Hiện Có:\033[0m")
            print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(
                "Mã Sản Phẩm", "Tên Sản Phẩm", "Giá Bán", "Giá Nhập", "Số Lượng", "Ngày Sản Xuất", "Ngày Hết Hạn"))
            print("-" * 130)
            for product in self.products:
                selling_price = f"{product.selling_price} VNĐ"
                buying_price = f"{product.buying_price} VNĐ"
                print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(
                    product.product_code, product.product_name, selling_price, buying_price,
                    product.quantity, product.manufacture_date.strftime('%Y-%m-%d'), product.expiration_date.strftime('%Y-%m-%d')))

    def edit_product(self, product_code, new_product_info):
        product = self.find_product(product_code)
        if product:
            for key, value in new_product_info.items():
                setattr(product, key, value)
            print("\033[32mThông tin sản phẩm đã được cập nhật.\033[0m")
        else:
            print("\033[33mKhông tìm thấy sản phẩm.\033[0m")

    def delete_product(self, product_code):
        product = self.find_product(product_code)
        if product:
            self.products.remove(product)
            print("\033[32mSản phẩm đã được xoá khỏi danh sách.\033[0m")
        else:
            print("\033[33mKhông tìm thấy sản phẩm.\033[0m")

    def add_invoice(self, invoice):
        if self.invoice_exists(invoice.invoice_code):
            print(f"\033[31mHóa đơn có mã {invoice.invoice_code} đã tồn tại trong hệ thống.\033[0m")
        else:
            self.invoices.append(invoice)
            return True
    def invoice_exists(self, invoice_code):
        for inv in self.invoices:
            if inv.invoice_code == invoice_code:
                return True
        return False

    def display_invoices(self):
        if not self.invoices:
            print("\033[33mKhông có hóa đơn nào.\033[0m")
        else:
            print("\033[92m==>Danh sách hóa đơn:\033[0m")
            for invoice in self.invoices:
                invoice.display_invoice_info()
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

        print("{:<20} {:<20} {:<20}".format("Mã Sản Phẩm", "Tên Sản Phẩm", "Doanh Thu"))
        print("-" * 40)
        for i in range(min(n, len(sorted_products))):
            product_code, revenue = sorted_products[i]
            product = self.find_product(product_code)
            print("{:<20} {:<20} {:<20}".format(product_code,product.product_name, revenue))

    def calculate_daily_revenue(self, date):
        total_revenue = 0
        for invoice in self.invoices:
            if invoice.invoice_date.date() == date.date():
                total_revenue += invoice.calculate_total()
        return total_revenue

    def display_expired_products(self):
        today = datetime.now()
        soon_to_expire = []
        for product in self.products:
            days_to_expire = (product.expiration_date - today).days
            if days_to_expire <= 42 and days_to_expire > 0:
                if days_to_expire <= 21:
                    product_price = product.selling_price * 0.431
                else:
                    product_price = product.selling_price * 0.725
                soon_to_expire.append((product.product_code, product.product_name, product_price))
        if soon_to_expire:
            print("\033[34mDanh sách sản phẩm sắp hết hạn:\033[0m")
            print("{:<10} {:<20} {:<20}".format("Mã Sản Phẩm", "Tên Sản Phẩm", "Giá Mới"))
            print("-" * 50)
            for product in soon_to_expire:
                print("{:<10} {:<23} {:<20} VNĐ".format(product[0], product[1], int(product[2])))

    def validate_date_format(self, date_str):
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            raise ValueError("\033[31mSai định dạng ngày. Vui lòng nhập theo định dạng YYYY-MM-DD.\033[0m")

