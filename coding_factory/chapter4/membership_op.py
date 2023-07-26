# Bring the fruits from 2 list not the same in a new list 

fruits_first = ["Apple", "Banana", "Orange", "Mango",  "Banana", "Strawberry",  "Banana"]
fruits_second = ["Melon", "Orange", "Mango",  "Banana", "Strawberry", "Pear"]

new_fruits_list = []

for fruit in fruits_first:
    if fruit in fruits_second and fruit not in new_fruits_list:
            new_fruits_list.append(fruit)

print("New fruits list:", new_fruits_list) # New fruits list: ['Melon', 'Orange', 'Mango', 'Banana', 'Strawberry', 'Pear']

