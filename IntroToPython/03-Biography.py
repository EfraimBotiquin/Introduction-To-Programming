
name = input("Enter your name: ")
hometown = input("Enter your hometown: ")

while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter a valid number for age not letters.")
bio = {
    "name": name,
    "hometown": hometown,
    "age": age
}
print(f"{bio['name']}\n{bio['hometown']}\n{bio['age']}")
