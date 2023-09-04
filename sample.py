# compilation error: compile time error
# logical error: syntax ok, o/p fail
# run-time error: user information error
# exception handling

# try:
#     a = int(input("Enter the number: "))
#     print(a)
# except ValueError:
#     raise ValueError("Invalid input. Please enter a valid integer")
# finally:
#     print("hello")

# try:
#     num = int(input("Enter a number: "))
#     if num % 2 == 0:
#         print("Number is even")
#     else:
#         print("Number is odd")
# except ValueError:
#     raise ValueError("Invalid input. Please enter a valid integer")
# finally:
#     print("Thank you")

def oddEven():
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
try:
    num = int(input("Enter the input: "))
    oddEven()
except ValueError:
    raise ValueError("Invalid input. Please enter a valid integer")
finally:
    print("Hi")
