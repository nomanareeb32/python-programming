lst = ["aPpLe", "bAnAnA", "OrAnGe", "uMbReLlA", "KiWi", "IgLoO", "", "gRaPe", ""]
for i in lst:
    if i == "":
        lst.remove(i)
print(lst)