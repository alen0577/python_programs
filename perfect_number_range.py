lower = int(input('Enter the lower limit: '))
upper = int(input('Enter the upper limit: '))

for num in range(lower, upper + 1):
    sum1 = 0
    for i in range(1, num):
        if num % i == 0:
            sum1 += i
    if sum1 == num:
        print(num, end=',')
