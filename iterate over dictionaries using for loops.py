# 9. Write a Python program to iterate over dictionaries using for loops.


address_house = {'Hang': 'San Jose', 'Gurmeet': 'Evergreen', 'Mahiveer': 'San Francisco', 'Khivi': 'Los Gatos'}

print (address_house.keys())

for owner_name, owner_address in address_house.items():
   print( 'Owner name:' + owner_name)
   print ('owner address:' + owner_address)