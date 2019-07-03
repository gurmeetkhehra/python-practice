# magicians = ['alica', 'david', 'carolina']
# for magicians in magicians:
#     print (magicians)
#     print (magicians.title() + ", the was a great trick!  " )
#     print ( "I can't wait to see you next trick, " + magicians.title() + ". \n")
#     print ("Thank you everyone, that was a great magic show!")

for value in range (1,5):
    print(value)
for value in range (1,6):
    print(value)
numbers = list (range(1,6))
print (numbers)
even_numbers = list (range (2,11,2))
print (even_numbers)

squares = []
for value in range (1,11):
    square = value**2
    squares.append (square)
    print (squares)

    squares.append(value**2)
    print (squares)

digits = [1,2,3,4,5,6,7,8,9,0]
min (digits)
print (min (digits))
max (digits)
print (max(digits))
sum(digits)
print (sum (digits))

squares = [value**2 for value in range (1,11)]
print (squares)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print (players [1:4])
# print (players [:4])
# print (players[2:])
# print (players [-3:])
# print ("Here are the first three players on my team:")
# for players in players[:3]:
#     print (players.title())
#
#
# my_foods =['pizza', 'falafel', 'carrot cake ']
# friend_foods  = my_foods [:]
# print ("My favorite foods are:")
# print (my_foods)
#
# print ("\nMy  friend's favorite foods are:")
# print (friend_foods)
#
# my_foods.append ('cannoli')
# friend_foods.append ('ice cream')
# print ("My favorite foods are:")
# print (my_foods)
# print ("\nMy  friend's favorite foods are:")
# print (friend_foods)
#
# friend_foods = my_foods
# my_foods.append ('cannoli')
# friend_foods.append ('ice cream')
# print ("\nMy  friend's favorite foods are:")
# print (friend_foods)

dimensions = (200, 50)
# print (dimensions [0])
# print (dimensions [1])
# # dimensions [0] =250
#
# for dimensions in dimensions:
#     print (dimensions)

print ("Original dimensions:")
for dimension in dimensions:
        print (dimension)

dimensions = (400, 100)
print ("\nModified dimensions:")
for dimension in dimensions:
        print (dimension)





