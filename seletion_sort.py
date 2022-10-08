def sort(num):
    for i in range(len(num) - 1):
        min_pos = i
        for j in range(i, len(num)):
            if num[j] < num[min_pos]:
                min_pos = j
        temp = num[i]
        num[i] = num[min_pos]
        num[min_pos] = temp
        print(num)


num = [10, 20, 5, 14, 47, 12, 32, 25, 4, 9, 7, 35]
sort(num)
print(num)