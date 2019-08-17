# 3. Write a Python class that represents a Shoe.  Add all attribtues you can think of.

class Shoe():

    def __init__(self, brand, color, size, price):
        self.brand = brand
        self.color = color
        self.size = size
        self.price = price


my_shoe = Shoe('Nike', 'Red', 5, 29.95)
print(my_shoe.brand)
print(my_shoe.color)
print(my_shoe.size)
print(my_shoe.price)
