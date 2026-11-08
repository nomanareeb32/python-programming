matrix = []

for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            found_row = i
            found_col = j

print(abs(found_row - 2) + abs(found_col - 2))