class User:
    def __init__(self, name, age, email):  
        self.name = name
        self.age = age
        self.email = email

    def get_info(self):
        return {
            'name': self.name,
            'age': self.age + "years",  
            'email': self.email
        }

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity