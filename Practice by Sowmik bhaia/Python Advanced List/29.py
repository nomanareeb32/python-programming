l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
csum = []
for i in range(len(l)):
    csum.append(sum(l[:i+1]))
print(csum)