# file = open("demo.txt", "w")
# file.close()

# file = open("demo.txt", "r")
# content = file.read()
# print(content)
# file.close()

file = open("demo.txt", "a")
file.write("\nWelcome to this world.")
file.close()
