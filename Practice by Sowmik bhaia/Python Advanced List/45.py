lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunks = []
for i in range(0, len(lst), 3): #range(start, end, step)
    chunks.append(lst[i:i+3])
print(chunks)