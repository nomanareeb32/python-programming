for _ in range(int(input())):
    b = int(input())
    c = input()
    count = 0
    for i in range((b + 1) // 2):
        temp = c[:i] + c[i + 1:]
        if temp == temp[::-1]:
            if b % 2 != 0 and i == ((b + 1) // 2) - 1:
                count += 1
            else:
                count += 2
    print(count)
