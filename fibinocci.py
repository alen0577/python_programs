x = int(input('enter no.of terms: '))
num1 = 0
num2 = 1
c = 0

if x <= 0:
    print('enter a valid no.')
elif x == 1:
    print('Fibinocci series :', num1)
else:
    print('fibinocci series')
    while c < x:
        print(num1, end=' ')
        n = num1+num2
        num1 = num2
        num2 = n
        c += 1

