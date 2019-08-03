# 4. Make a program that lists the countries in the list below using a while loop.

countries = "\n List the countries in that you visited:"
countries += "\n(Enter 'quit' when you are finished.)"

while True:
    countries = input(countries)
    if countries == 'quit':
        break
    else:
        print("I would like to visit the " + countries.title()+ "!")