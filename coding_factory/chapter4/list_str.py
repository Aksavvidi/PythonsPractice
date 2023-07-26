# Create a list with differends  ways

empty_list = []
print("Empty List: " , empty_list)
print("Type: " ,type(empty_list))

populate_list =[10, 3.14, True, "CF"]
print("Populate List: " , populate_list)
print("Type: " ,type(populate_list))

dynamic_list = eval(input("Please insert a list: "))
print("Dynamic List: " , dynamic_list)
print("Type: " ,type(dynamic_list))

empty_f_list = list()
print("Empty f List: " , empty_f_list)
print("Type: " ,type(empty_f_list))

string = "Coding Factory"
string_list = list(string)
print("List of string: " , string_list)
print("Type: " ,type(string_list))

populate_tuple = (10, 3.14, True, "CF")
list_from_tuple = list(populate_tuple)
print("List from tuple: " , list_from_tuple)
print("Type: " ,type(list_from_tuple))

list_from_range = list(range(5))
print("List of rang: " , list_from_range)
print("Type: " ,type(list_from_range))

sentence = "Hello C F"
list_from_split = sentence.split()
print("List from split: " , list_from_split)
print("Type: " ,type(list_from_split))

sentence = "Hello Coding Factory"
list_from_split = sentence.split(maxsplit=2)
print("List from split: " , list_from_split)
print("Type: " ,type(list_from_split))