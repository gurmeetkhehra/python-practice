# 5. Write a Python class Car and all attributes private. Write method to return all individual attributes

class Car():

    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def get_car_details(self):
        print(self.brand)
        print(self.model)
        print(self.color)
        print(self.year)

Toyota = Car('Toyota', 'Camry', 2018, 'white')
print(Toyota.get_car_details())


class ElectricCar(Car):
    def __init__(self, brand, model, year, color, battery, charged_capacity):
        super().__init__(brand, model, year, color)
        self.battery=battery
        self.charged_capacity=charged_capacity

    def get_car_details(self):
        super().get_car_details()
        print(self.battery)
        print(self.charged_capacity)


tesla = ElectricCar('Tesla', 'X', 2019, 'Red', 5000, 100)
print(tesla.get_car_details())