#Welcome App

def welcome_quest():
    return "Welcome guest!"

def welcome_user(username):
    return f"Welcome {username}"

def main():
    username = input('Give us your username: ')

    message = welcome_user(username) if username else welcome_quest()

    print(message)

if __name__ == '__main__':
    main()