a = str(input())
b = str(input())
a = a.lower()
b = b.lower()
position = 0
found_all = True
for letter in a:
    index = b.find(letter, position)
    if index == -1:
        found_all = False
        break
    position = index + 1
if found_all:
    print("Yes")
else:
    print("No")