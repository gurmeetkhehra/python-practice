# Homework 4-1 ----> 4-2

# pizzas = ['meat', 'cheese','pepperoni']
# for pizza in pizzas:
#     print (pizza)
#     print (pizza.title() + " , I love pepperoni pizza.")
#     print ("I really love pizza! " + pizza.title() + " .\n")
#
# animals = ['dog', 'cat', 'horse']
# print (animals)
# for animal in animals:
#     print (animal.title() + " , A dog would make a great pet.")
    # print ("Any of these animals would make a great pet!" + animal.title() + " .\n")

# homework 4-3 ----> 4-9

# numbers = list (range(1,21))
# print (numbers)
#
# squares = []
# for value in range (1, 100000):
#     square = value**2
#     squares.append(square)
#
# print (squares)

#
# even_numbers = list(range(2,20,2))
# print (even_numbers)
#
# multiples = list (range(3, 30, 3))
# print (multiples)

# Homwork 4-10 -4-12
#
# teamplayers =['khivi','jasmine', 'methab', 'madhava', 'heidi']
# print(teamplayers[0:3])
# print(teamplayers [2:4])
# print (teamplayers[2:])

pizzas = ['meat', 'cheese','pepperoni']
friend_pizzas = pizzas [:]
print ("My favorite pizzas are:")
print (pizzas)
print("\n My friend's favorite pizzas are:")
print (friend_pizzas)
pizzas.append('vegetable')
friend_pizzas.append('cake')
print ("My favorite pizzas are:")
print (pizzas)
print("\n My friend's favorite pizzas are:")
print (friend_pizzas)


