a = input()
is_lucky = True
count = a.count("4") + a.count("7")
b = str(count)
for i in range(len(b)):
    if b[i] != "4" and b[i] != "7":
        is_lucky = False

if is_lucky:
    print("YES")
else:
    print("NO")
