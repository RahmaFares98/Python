class Product:
    def __init__(self, name, price, category, product_id):
        self.name = name
        self.price = price
        self.category = category
        self.product_id = product_id

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += self.price * percent_change / 100
        else:
            self.price -= self.price * percent_change / 100

    def print_info(self):
        print("Product:", self.name)
        print("Category:", self.category)
        print("Price:", self.price)
