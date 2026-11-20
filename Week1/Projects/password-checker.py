password = input("Enter your password: ")

if len(password) < 8:
    print("Weak: Password is too short!")
else:
    print("Strong: Good password!")
