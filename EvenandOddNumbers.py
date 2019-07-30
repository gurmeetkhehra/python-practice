# 1. Write a Python program to count the number of even and odd numbers from a series of numbers
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Expected Output :

# Number of even numbers : 5
# Number of odd numbers : 4


num = (1,2,3,4,5,6,7,8,9)
count_even = 0
count_odd = 0
for x in num:
    if not x % 2:
        count_even += 1
    else:
        count_odd += 1

print ("num of even num:", count_even)
print ("num of odd num :", count_odd)


