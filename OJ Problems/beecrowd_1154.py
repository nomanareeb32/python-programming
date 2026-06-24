Sum = 0
count = 0
while 1:
    X = int(input())
    if 0 > X:
        break
    else:
        Sum = Sum + X
        count += 1
ave = Sum / count
print("%.2f" % ave)
