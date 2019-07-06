# 7. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Go to the editor

# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']


colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

colors.remove('Red')
colors.remove('Pink')
colors.remove('Yellow')

print(colors)