from collections import deque

garage = deque() # create a deque

# simulation of cars arriving at tha garage
garage.append("Car 1")
garage.append("Car 2")
garage.append("Car 3")
garage.append("Car 4")

# print current state of garage (time 1)
print("Current state of garage: ", list(garage))

#simulate a car leaving the garage (FIFO)
car_left = garage.popleft()

# simulation of cars arriving at the garage
garage.append("Car 5")
garage.append("Car 6")

# print current state of garage (time 2)
print("Current state of garage: ", list(garage))
print("Last car wich left at the garage:", car_left)



