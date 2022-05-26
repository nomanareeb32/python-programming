a = int(input("GIVE THE SMALLER NUMBER\n"))
b = int(input("GIVE THE BIGGER NUMBER\n"))
count = 0
pld = []
for i in range(a, b + 1):
    i = str(i)
    c = i[::-1]
    if int(c) == int(i) and int(c) > 9:
        count += 1
        pld.append(int(c))
if count > 1:
    print("THERE ARE {} PALINDROMES BETWEEN {} AND {}".format(count, a, b))
    print("THEY ARE: ")
    for x in range(len(pld)):
        print(pld[x])
elif count == 1:
    print("THERE IS {} PALINDROME BETWEEN {} AND {}".format(count, a, b))
    print("IT IS: ")
    for x in range(len(pld)):
        print(pld[x])
else:
    print("THERE IS NO PALINDROMES BETWEEN {} AND {}".format(a, b))
