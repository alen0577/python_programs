def lcm(a, b):
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    lcm1 = (a * b) // gcd(a, b)
    return lcm1


a = int(input('Enter first no: '))
b = int(input('Enter second no: '))
print(lcm(a, b))
