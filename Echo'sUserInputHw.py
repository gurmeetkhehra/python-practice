# 3. Write a Python program that echo's User input until 'quit' is provided by User.

prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "


while True:
    topping = input(prompt)
    if topping != 'quit':
        print (" I'll add" + topping + "to your pizza.")
    else:
        break

