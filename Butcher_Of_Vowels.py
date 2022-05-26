t = int(input())
for i in range(t):
    s = input()
    s = list(s)
    for j in s:
        if j == "A" or j == "a":
            print("Yes")
            break
        elif j == "E" or j == "e":
            print("Yes")
            break
        elif j == "I" or j == "i":
            print("Yes")
            break
        elif j == "O" or j == "o":
            print("Yes")
            break
        elif j == "U" or j == "u":
            print("Yes")
            break
    else:
        print("No")
