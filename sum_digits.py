def sum_digit(n):
    s = 0
    while n > 0:
        digits = n % 10
        s += digits
        n //= 10
    return s


n = int(input('enter a number: '))
print(sum_digit(n))
