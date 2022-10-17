low = int(input('enter lower limit: '))
up = int(input('enter upper limit: '))

for num in range(low, up + 1):
    order = len(str(num))
    s = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        s += digit ** order
        temp //= 10
    if num == s:
        print(num)

