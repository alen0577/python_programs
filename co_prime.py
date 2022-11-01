def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

if gcd(a, b) == 1:
    print(a, 'and', b, 'are co-prime')
else:
    print('not co-prime')
