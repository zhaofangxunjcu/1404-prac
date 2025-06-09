# name = input("Enter your name: ")
#
# file = open("name.txt", "w")
# file.write(name)
# file.close()
# print("Name has been written to name.txt.")
# file = open("name.txt", "r")
# name = file.read()
# file.close()
# print(f"Hi {name}!")
with open("numbers.txt", "r") as file:
    first_number = int(file.readline())
    second_number = int(file.readline())
result = first_number + second_number
print(result)
