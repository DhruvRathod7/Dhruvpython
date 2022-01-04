def calculate_xfaxtor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfaxtor(-1)
except ValueError as error:
    print(error)
