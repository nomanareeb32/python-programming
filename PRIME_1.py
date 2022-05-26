s = int(input())
count = 0
for i in range(2, s):
    if s % i == 0:
        count += 1
        break
if count > 0:
    print("NOT PRIME")
else:
    print("PRIME")
