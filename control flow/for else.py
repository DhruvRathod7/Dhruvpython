successful = True
for number in range(3):
    print("attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attepted 3 times and failed")
