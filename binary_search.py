def search(list1, n):
    l = 0
    u = len(list1)

    while l <= u:
        mid = (l + u) // 2
        if list1[mid] == n:
            print('found at position:', mid+1)
            break
        else:
            if list1[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    else:
        print('Not found')


list1 = [1, 3, 5, 10, 18, 25, 36, 45, 54, 66, 78, 85, 99, 105]
n = int(input('Enter a number to search: '))
search(list1, n)
