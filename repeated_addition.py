def mul(a, b):
    product = 0
    for i in range(1, b + 1):
        product = product + a

    print('product is :', product)


a = int(input('first number: '))
b = int(input('second number: '))
mul(a, b)
