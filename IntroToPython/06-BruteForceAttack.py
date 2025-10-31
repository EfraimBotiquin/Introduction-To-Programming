
password = "12345"
attempts = 5

while attempts > 0:
    entry = input("Enter password: ")
    if entry == password:
        print("Access granted")
        break
    else:
        attempts -= 1
        print(f"Incorrect password. {attempts} attempts remaining.")
else:
    print("Too many incorrect attempts. Authorities have been alerted")
