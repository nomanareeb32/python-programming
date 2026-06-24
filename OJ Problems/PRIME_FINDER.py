a = int(input())
b = int(input())
if a > 0:
    for num in range(2, a + 1):
        for i in range(2, num):
            if num % i == 0:
                break
            else:
                c = []
                c.append(num)
            print(c[b+1])
elif a == b:
    print("NOTHING FOUND!!!!!!")
elif a == 0:
    print("HAVE A NICE DAY.")
quit(0)
