# 5. Write a Python program to print prime numbers from list below:
# # numbers = [1,2,3,4,5,6,7,8,10,13,15,17]

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):
    # prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)