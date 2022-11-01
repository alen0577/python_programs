def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


num1 = int(input('Enter a number: '))
lower = int(input('Enter lower limit: '))
upper = int(input('Enter upper limit: '))

for i in range(lower, upper+1):
    if gcd(num1, i) == 1:
        print(i, end=',')

