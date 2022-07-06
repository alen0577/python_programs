def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num - 1)


try:
    num = int(input("enter number to find factorial: "))
    print(fact(num))

except:
    print("enter a valid number!!!")
finally:
    print("finished")
