import statistics

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
a = statistics.mean(list)
b = []
for i in list:
    if i > a:
        b.append(i)
print(len(b))