number = [1, 1, 2, 3, 4, ]
first = set(number)
second = {1, 5}

print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

if 1 in first:
    print("yes")
