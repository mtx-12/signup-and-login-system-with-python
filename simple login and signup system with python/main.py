
print("Create your account")
username = input("Input username: ")
password = input("Input password: ")
print("User "+username+" created successfully")
print("Login now ")
#username
user_comp = input("Enter username: ")
while user_comp != username:
    print("incorrect username try again")
    user_comp = input("Input username: ")
    if user_comp == username:
        print("welcome back "+username)
#password
password_comp = input("Enter your password: ")
while password_comp != password:
    print("incorrect username try again")
    user_comp = input("Enter your password: ")
    if password_comp == password:
        print("your login was sucessfull")
