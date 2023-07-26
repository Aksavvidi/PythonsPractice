#String Indexing and Slicing
message = input("Please give me a message: ")#Coding Factory

print(message[0])
print(message[len(message) - 1], " - ", message[-1]) #y  -  y

# The first 5 letters
print(message[0:5]) #Codin

#The letters "Coding"
print(message[0:6])  # the same as message[:6] 

# full message
print(message[:] ) # SAME as message[0:len(message) - 1]

# The even index letters
print(message[::2])  #Cdn atr