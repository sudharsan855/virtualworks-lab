correct_password = "Admin@123"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login Successful!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print("Incorrect password.")

        if remaining > 0:
            print("Attempts remaining:", remaining)

if attempts == max_attempts:
    print("Access Restricted. Too many failed attempts.")