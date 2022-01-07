import csv
import csv

with open("data.csv") as file:
    # writer = csv.writer(file)
    # writer.writerow(["transaction_id", "product_id", "price"])
    # writer.writerow([1000, 1, 50])
    # writer.writerow([1001, 2, 200])
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)
