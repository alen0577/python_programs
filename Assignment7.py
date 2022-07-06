dict1 = {"pen": 10, "pencil": 5, "notebook": 20, "bag": 500,
         "shoes": 650, "uniform": 1500, "water bottle": 30}
for i in dict1:
    print(i)
product = input("Enter the name of product :")

if product in dict1:
    print(dict1.get(product))
else:
    print("invalid product")





