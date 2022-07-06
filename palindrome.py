def palindrome(data):
    rev = data[::-1]
    if data == rev:
        print("Palindrome")
    else:
        print("Not palindrome")


data = input("Enter a data to check palindrome: ")
palindrome(data)




