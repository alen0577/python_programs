import re
str = "Hi alen,  how are you? "
pattern = "[0-9][a-z][A-Z]"

# if re.match(pattern, "...Hi Alen welcome"):
#     print("matched")
#
# else:
#     print("not matched")


# if re.search(pattern, "hi Alen , welcome here"):
#     print("matched")
#
# else:
#     print("not matched")

# print(re.findall(pattern, "hi alen,welcome alen,alen alen akdjrlealenalennfjtalen"))

# new = re.sub(pattern, "ALEN ANTONY", str)
# print(new)
# if re.match(pattern, "aleenn"):
#     print("match")
#
# else:
#     print("not")
if re.search(pattern, "9sA"):
    print("T")

else:
    print("F")
