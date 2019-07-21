def greet_user(username, age):
    print('Hello user ' + username.title() + ' with age ' + str(age))

counter = 1
while counter < 5:
    greet_user('Khivi', 4)
    counter = counter + 1


