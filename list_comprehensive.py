# def sqr():
#     for i in range(10):
#         print(i ** 2)
#
#
# sqr()
# lis = [i ** 2 for i in range(10)]
# print(lis)
# letters = []
# for i in "alen":
#     letters.append(i)
# print(letters)
# lis = [i for i in "alen"]
# print(lis)
# even = []
# for i in range(10):
#     if i % 2 == 0:
#         even.append(i)
# print(even)
lis = [i for i in range(10) if i % 2 != 0]
print(lis)
