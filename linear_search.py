def search(list1, n):
    for i in range(len(list1)):
        if list1[i] == n:
            print('Number found at position:', i + 1)
            break
    else:
        print('Number not found')


list1 = [1, 2, 5, 12, 15, 13, 25, 45, 36, 34]
n = int(input('Enter a number to search:'))
search(list1, n)
