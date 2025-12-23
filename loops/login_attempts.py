attempts = 2
correct_password = "admin"

while attempts > 0:
    password = input("Enter the password: ")

    if password == correct_password:
        print("Login successful")
        break
    else:
        attempts -= 1
        print("Wrong password. Attempts left:", attempts)

if attempts == 0:
    print("Account locked")
