def power(a, b):
    if b == 0:
        return 1
    product = a
    increment = a
    for i in range(1, b):
        for j in range(1, a):
            product += increment
        increment = product
    return product


a = int(input('Enter the base number: '))
b = int(input('Enter the exponent number: '))
print('Result: ', power(a, b))
