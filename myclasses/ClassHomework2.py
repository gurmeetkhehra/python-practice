# 2. Write a Python class which has two methods get_String and print_String. get_String accept a string from the
# user and print_String print the string in upper case

class stuff:
    """Write a Python class which has two methods get_String and print_String. get_String accept a string
     from the user and print_String print the string in upper case"""

    def __init__(self):
        self.x = input("Enter a text")

    def get_String(self):
        return self.x

    def print_String(self):
        return self.x.upper()


stuff = stuff()
print(stuff.print_String())


