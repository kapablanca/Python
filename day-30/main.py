# File not found

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} doesn't exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up.")

height = float(input("Height: "))
if height > 3:
    raise ValueError("Human height should not be over 3 meters.")
weight = float(input("Weight: "))


bmi = weight/height**2
print(bmi)