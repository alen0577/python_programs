# x = lambda a, b: a * b
# print(x(6, 2))
# y = lambda c, d: c / d
# print(y(10, 5))
# evenodd = lambda n: "even" if n % 2 == 0 else "odd"
# x = int(input("enter a number"))
# print(evenodd(x))
# mm = lambda x, y: x if x > y else y
# print(mm(5,10))
def sum(x):
    return lambda y: x + y


a = sum(5)
print(a(10))
y = sum(15)
print(y(10))

lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newlis = list(filter(lambda x: (x % 2 == 0), lis))
print(newlis)

mylist = [1, 2, 3, 4, 5, 10]
a = list(map(lambda b: (b % 2 != 0), mylist))
print(a)

from functools import reduce

t = reduce(lambda a, b: a + b, [1, 2, 3, 4, 5, 6])
print(t)