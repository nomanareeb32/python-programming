a = str(input())
b = str(input())
a = a.lower().replace(" ", "")
b = b.lower().replace(" ", "")
a = sorted(a)
b = sorted(b)
if a == b:
    print("Anagrams")
else:
    print("Not Anagrams")