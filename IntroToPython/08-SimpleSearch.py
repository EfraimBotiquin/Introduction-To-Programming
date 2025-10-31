
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
search = input("Enter a name to search for: ").strip()

if search in names:
    print(f"{search} was found in the list!")
else:
    print(f"{search} was not found.")
