try:
    with open("the with statement.py") as file:
        print("File opened")

    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exception were thrown.")
