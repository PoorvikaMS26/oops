# Parent Class
class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def display_product(self):
        print("Product Name:", self.product_name)
        print("Price:", self.price)


# Child Class (Inherits from Product)
class ElectronicProduct(Product):
    def __init__(self, product_name, price, brand, warranty):
        super().__init__(product_name, price)
        self.brand = brand
        self.warranty = warranty

    def display_electronic_product(self):
        self.display_product()
        print("Brand:", self.brand)
        print("Warranty:", self.warranty)


# Grandchild Class (Inherits from ElectronicProduct)
class MobilePhone(ElectronicProduct):
    def __init__(self, product_name, price, brand, warranty, ram, storage):
        super().__init__(product_name, price, brand, warranty)
        self.ram = ram
        self.storage = storage

    def display_mobile_details(self):
        self.display_electronic_product()
        print("RAM:", self.ram)
        print("Storage:", self.storage)


# Create one object of MobilePhone
mobile1 = MobilePhone("iPhone 15", 80000, "Apple", "2 Year", "8GB", "256GB")

# Display all details
mobile1.display_mobile_details()