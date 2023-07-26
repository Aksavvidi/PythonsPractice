# strange message

strange_message = "C12o655di6598ng Fa54+ct4o12ry"

decrypted_message = ""

for char in strange_message:
    if not char.isnumeric():
        decrypted_message += char

print("Message:", decrypted_message)