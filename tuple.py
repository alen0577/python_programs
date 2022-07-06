t = ("apple", "mango", "banana")
t2 = (1, 2, 3, 4, 5)
print(t)
print(type(t))
print(t[2])
u = list(t)
print(type(u))
u[2] = "grapes"
t = tuple(u)
print(type(t))
print(t)
for i in t:
    print(i)
if "apple" in t:
    print("available")
t3 = t + t2
print(t3)
