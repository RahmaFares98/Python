from product import Product
from store import Store

# Create some products
product1 = Product("Phone", 500, "Electronics", 1)
product2 = Product("Shirt", 20, "Clothing", 2)
product3 = Product("Book", 15, "Books", 3)

# Create a store
my_store = Store("My Store")

# Add products to the store
my_store.add_product(product1)
my_store.add_product(product2)
my_store.add_product(product3)

# Test sell_product method
my_store.sell_product(3)

# Test inflation method
my_store.inflation(5)

# Test set_clearance method
my_store.set_clearance("Clothing", 20)

# Print remaining products
for product in my_store.products:
    product.print_info()
