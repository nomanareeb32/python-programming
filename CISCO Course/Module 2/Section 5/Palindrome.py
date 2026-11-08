a = str(input())
a = a.lower()
a = a.strip()
a = a.replace(" ", "")
reversed_a = a[::-1]
if reversed_a == a:
    print("It's a palindrome")
else:
    print("It's not a palindrome")