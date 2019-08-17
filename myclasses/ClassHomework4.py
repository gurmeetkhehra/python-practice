# 4. Write a Python class that represent a Laptop. Add all attribtues you can think of.

class Laptop():
    def __init__(self, brand, screen_size, model, OS, RAM, Processor_Type, Processor_Speed, Hard_Drive):
        self.brand = brand
        self.screen_size = screen_size
        self.model = model
        self.OS = OS
        self.RAM = RAM
        self.Processor_Type = Processor_Type
        self.Processor_Speed = Processor_Speed
        self.Hard_Drive = Hard_Drive

my_laptop = Laptop('Apple', 17, 'MD101LL/A', 'High Sierra', 16, 'Intel Core i5',
               2.5, 1)


print(my_laptop.brand)
print(my_laptop.model)
print(my_laptop.OS)
print(my_laptop.RAM)
print(my_laptop.Processor_Type)
print(my_laptop.Processor_Speed)
print(my_laptop.Hard_Drive)