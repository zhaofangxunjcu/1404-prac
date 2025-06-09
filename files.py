# name = input("Enter your name: ")
#
# file = open("name.txt", "w")
# file.write(name)
# file.close()
#
# print("Name has been written to name.txt.")
file = open("name.txt", "r")
name = file.read()
file.close()

print(f"Hi {name}!")
