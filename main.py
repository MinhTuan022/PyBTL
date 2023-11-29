from datetime import datetime

from Invoice import Invoice
from ManageProduct import ManageProduct
from Product import Product


def main():
    manager = ManageProduct()
    # Chuẩn bị dữ liệu
    new_product1 = Product("P1", "Sữa", 5000, 2000, 50, "2023-1-1", "2025-1-1")
    new_product2 = Product("P2", "Cà phê", 4000, 1000, 30, "2023-2-15", "2024-2-15")
    new_product3 = Product("P3", "Bánh quy", 2000, 1000, 40, "2023-10-25", "2023-10-25")
    new_product4 = Product("P4", "Cháo hạt sen", 4000, 2500, 25, "2023-4-20", "2023-12-31")
    new_product5 = Product("P5", "Nước ngọt", 1500, 800, 60, "2023-5-5", "2024-5-5")
    new_product6 = Product("P6", "Kẹo", 1000, 200, 70, "2023-6-30", "2023-12-20")
    new_product7 = Product("P7", "Mì tôm", 3000, 500, 45, "2023-5-12", "2024-1-1")
    new_product8 = Product("P8", "Bánh mì", 1500, 600, 55, "2023-8-18", "2023-9-18")
    new_product9 = Product("P9", "Trà", 2500, 1000, 35, "2023-9-2", "2024-9-2")
    new_product10 = Product("P10", "Sữa chua", 2000, 900, 40, "2023-10-5", "2023-12-22")
    manager.add_product(new_product1)
    manager.add_product(new_product2)
    manager.add_product(new_product3)
    manager.add_product(new_product4)
    manager.add_product(new_product5)
    manager.add_product(new_product6)
    manager.add_product(new_product7)
    manager.add_product(new_product8)
    manager.add_product(new_product9)
    manager.add_product(new_product10)

    invoice1 = Invoice("I1", "2023-10-01")
    invoice1.add_item("P1", "Sữa", 10, 5000, 50000)
    invoice1.add_item("P3", "Bánh quy", 5, 2000, 1000)

    invoice2 = Invoice("I2", "2023-10-05")
    invoice2.add_item("P1", "Sữa", 20, 5000, 100000)

    invoice3 = Invoice("I3", "2023-10-10")
    invoice3.add_item("P3", "Bánh quy", 10, 2000, 20000)

    # Thêm các hoá đơn vào danh sách hoá đơn trong quản lý hàng hoá
    manager.invoices.extend([invoice1, invoice2, invoice3])

    while True:
        print("\n------ MENU ------")
        print("1. Thêm sản phẩm")
        print("2. Tìm kiếm sản phẩm")
        print("3. Sửa thông tin sản phẩm")
        print("4. Xóa sản phẩm")
        print("5. Hiển thị danh sách sản phẩm")
        print("6. Bán Hàng")
        print("7. Sắp xếp tổng doanh thu từng mặt hàng")
        print("8. Tính tổng doanh thu theo ngày của cửa hàng")
        print("9. Hiển thị 5 mặt hàng có tổng doanh thu cao nhất và thấp nhất")
        print("10. Tổng hợp những hàng hoá sắp hết hạn sử dụng")
        print("11. Thoát chương trình")

        choice = input("Nhập lựa chọn của bạn: ")

        if choice == "1":
            while True:
                try:
                    product_code = input("Nhập mã sản phẩm: ")
                    product_name = input("Nhập tên sản phẩm: ")
                    selling_price = float(input("Nhập giá bán: "))
                    buying_price = float(input("Nhập giá nhập: "))
                    quantity = int(input("Nhập số lượng: "))
                    manufacture_date = input("Nhập ngày sản xuất (YYYY-MM-DD): ")
                    manager.validate_date_format(manufacture_date)
                    expiration_date = input("Nhập hạn sử dụng (YYYY-MM-DD): ")
                    manager.validate_date_format(expiration_date)

                    break
                except ValueError:
                    print("Giá trị nhập vào không hợp lệ, vui lòng nhập lại")

            new_product = Product(product_code, product_name, selling_price, buying_price, quantity, manufacture_date,
                                  expiration_date)
            manager.add_product(new_product)
            print("Sản phẩm đã thêm thành công")

        elif choice == "2":
            while True:
                try:
                    search_code = input("Nhập mã sản phẩm cần tìm kiếm: ")
                    break
                except ValueError:
                    print("Giá trị nhập vào không hợp lệ, vui lòng nhập lại")
            found_product = manager.find_product(search_code)
            if found_product:
                print(f"Thông tin sản phẩm: {found_product.__dict__}")
            else:
                print("Không tìm thấy sản phẩm.")

        elif choice == "3":
            product_code = input("Nhập mã sản phẩm cần sửa: ")
            product = manager.find_product(product_code)
            if product:
                while True:
                    try:
                        new_info = {
                            "product_name": input("Nhập tên sản phẩm mới: "),
                            "selling_price": float(input("Nhập giá bán mới: ")),
                            "buying_price": float(input("Nhập giá mua mới: ")),
                            "quantity": int(input("Nhập số lượng sản phẩm mới: ")),
                            "manufacture_date": datetime.strptime(input("Nhập vào ngày sản xuất (YYYY-MM-DD): "), '%Y-%m-%d'),
                            "expiration_date": datetime.strptime(input("Nhập vào ngày hết hạn(YYYY-MM-DD): "), '%Y-%m-%d')
                        }
                        break
                    except ValueError:
                        print("Giá trị nhập vào không hợp lệ, vui lòng nhập lại")
                manager.edit_product(product_code, new_info)
            else:
                print("Không tìm thấy sản phẩm.")

        elif choice == "4":
            product_code = input("Nhập mã sản phẩm cần xoá: ")
            product = manager.find_product(product_code)
            if product:
                manager.delete_product(product_code)
            else:
                print("Không tìm thấy sản phẩm.")

        elif choice == "5":
            manager.display_products()

        elif choice == "6":
            # Bán hàng
            # Tạo hoá đơn mới tại đây, tương tự như chức năng thêm sản phẩm ở trên
            while True:
                try:
                    invoice_code = input("Nhập mã hoá đơn: ")
                    invoice_date = datetime.strptime(input("Nhập ngày xuất hoá đơn (YYYY-MM-DD): "), '%Y-%m-%d')
                    break
                except ValueError:
                    print("Giá trị nhập vào không hợp lệ, vui lòng nhập lại")

            invoice = Invoice(invoice_code, invoice_date)

            while True:
                while True:
                    try:
                        product_code = input("Nhập mã sản phẩm: ")
                        quantity = int(input("Nhập số lượng: "))
                        break
                    except ValueError:
                        print("Giá trị nhập vào không hợp lệ, vui lòng nhập lại")

                product = manager.find_product(product_code)
                if product:
                    if product.quantity >= quantity:
                        # Thêm sản phẩm vào hoá đơn
                        invoice.add_item(product.product_code, product.product_name, quantity, product.selling_price,
                                         product.selling_price * quantity)
                        product.quantity -= quantity  # Giảm số lượng sản phẩm trong kho
                        print(f"Đã thêm sản phẩm {product.product_name} vào hoá đơn.")
                    else:
                        print("Số lượng sản phẩm không đủ.")
                else:
                    print("Không tìm thấy sản phẩm.")

                add_another = input("Thêm sản phẩm khác vào hoá đơn? (Y/N): ")
                if add_another.lower() != 'y':
                    break

            manager.add_invoice(invoice)  # Thêm hoá đơn vào danh sách quản lý
            invoice.display_invoice_info()

        elif choice == "7":
            # date_input = input("Nhập ngày (YYYY-MM-DD): ")
            # date = datetime.strptime(date_input, '%Y-%m-%d')
            # revenue_by_product = manager.calculate_daily_revenue(date)
            # print("Tổng doanh thu theo ngày của từng mặt hàng:")
            # for product_code, revenue in revenue_by_product.items():
            #     print(f"Mã hàng hoá: {product_code}, Doanh thu: {revenue}")

            reverse_sort = input("Sắp xếp từ cao đến thấp (Y) hoặc từ thấp đến cao (N): ").lower()
            reverse = True if reverse_sort == 'y' else False
            sorted_products = manager.sort_product_revenue(reverse)
            print("Sắp xếp tổng doanh thu từng mặt hàng:")
            for product_code, revenue in sorted_products:
                print(f"Mã hàng hoá: {product_code}, Doanh thu: {revenue}")

        elif choice == "8":
            while True:
                try:
                    date_input = input("Nhập ngày (YYYY-MM-DD) muốn thông kê doanh thu: ")
                    date = datetime.strptime(date_input, '%Y-%m-%d')
                    break
                except ValueError:
                    print("Giá trị nhập vào không hợp lệ")
            total_revenue = manager.calculate_daily_revenue(date)
            print(f"Tổng doanh thu của cửa hàng trong ngày {date.date()}: {total_revenue}")

        elif choice == "9":
            # hiển thị 5 mặt hàng có doanh thu cao nhất, thấp nhât
            manager.display_top_products(5)
            manager.display_top_products(5, True)

        elif choice == "10":
            # Tổng hợp sản phẩm hết hạn, fix giá
            manager.display_expired_products()

        elif choice == "11":
            print("Đã thoát chương trình.")

        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")


if __name__ == "__main__":
    main()
