# amount = 2000

# try:
#     if (price > 300):
#         print("You are eligible")
# except NameError as e:
#     print(f"You are not eligible {e}")


# mylist = [1, 2, 3, 4, 5, 6]

# try:
#     print(mylist[10])

# except IndexError as I:
#     print(f"Index out of range {I}")


# try:
#     import masiha
# except ImportError as IE:
#     print(f"Module not found {IE}")


try:
    age = int(input("Enter the age: "))
except ValueError as e:
    print(f"Invalid input {e}")
