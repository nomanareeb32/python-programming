count = 0
avg = 0.0
for i in range(1, 7):
    n = float(input())
    if n > 0:
        avg = avg + n
        count = count + 1
print("{} valores positivos".format(count))
print("%0.1f" % (avg / count))
