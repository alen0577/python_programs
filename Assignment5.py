def div(num1, num2):
        print(num1 / num2)

try:
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second number"))
    div(num1, num2)

except:
    print("Sorry...,zero division error!")

finally:
    print("Finished")
