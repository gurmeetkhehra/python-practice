def describe_food(cuisine, name, spice_level):
    print("Cuisine name is " + cuisine)
    print("Food item name is" + name)
    print("Spice level is" + spice_level)
    print("\n")


describe_food("Punjabi", "Chole Bhature", "medium")
describe_food("Mexcian", "Taco", "mild")
describe_food("American", "Pizza", "super spicy")

#Using keyword
describe_food(name='Pineapple rice', spice_level='Spicy', cuisine='Thai')
