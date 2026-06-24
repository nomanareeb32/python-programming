n = int(input())
marksheet = []
marks = []
names = []
for i in range(n):
    name = input()
    score = float(input())
    marksheet.append([name, score])
    if score not in marks:
        marks.append(score)
g = sorted(marks)
for i in marksheet:
    if g[1] == i[1]:
        names.append(i[0])
names = sorted(names)
for n in names:
    print(n)
