dic1 = {1: "abc", "b": "cba", 3: "bca"}
print(dic1.get(1))
print(dic1.get(5, "key not found"))
dic1[1] = "hello"
print(dic1)
for x in dic1:
    print(dic1[x])
if 1 in dic1:
    print("available")
print(len(dic1))
dic1[4] = "new"
print(dic1)
dic1.popitem()
print(dic1)
new = dict(a="apple", b="ball", c=155)
print(new)
print(new.values())
print(new.keys())
print(new.items())


