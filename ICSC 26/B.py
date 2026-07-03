def generate_shape(n, shape):

    grid = []  # This will hold our final N x N grid

    if shape == "checkerboard":
        """
        Checkerboard logic:
        - Cells alternate between 0 and 1 like a chess board.
        - The top-left cell (row 0, col 0) must always be 0.
        - A cell is 0 when the SUM of its row index and column index is even.
        - A cell is 1 when the sum of its row index and column index is odd.
        Why? Because (0,0) -> sum = 0 (even) -> must be 0. This matches the rule.
        """

        for i in range(n):
            x = []
            for j in range(n):
                if (i + j) % 2 == 0:
                    x.append(0)
                else:
                    x.append(1)
            grid.append(x)

    elif shape == "diamond":
        """
        Diamond logic:
        - N is always odd, so there is a single, exact center cell.
        - The center of the grid is at row = n//2, col = n//2. Call this "mid".
        - A diamond shape is made of all cells whose absolute distance from the center is <= c.
        Absolute distance from center = |i - c| + |j - c|
        Why does this work?
        - At the very center (i=c, j=c), distance = 0, which is always <= c, so the center is always filled.
        - As we move away from the center, the distance increases by 1 for every step in row or column.
        - The diamond's "radius" is exactly c (half the grid, since N is odd), so any cell within that radius is part of the diamond shape.
        """

        mid = n // 2
        for i in range(n):
            x = []
            for j in range(n):
                distance = abs(i - mid) + abs(j - mid)
                if distance <= mid:
                    x.append(1)
                else:
                    x.append(0)
            grid.append(x)

    else: #If the shape is not checkerboard or diamond
        print("Unknown shape:", shape)
    return grid

#Taking Inputs
n = int(input())
shape = input()

#Run and Print
grid = generate_shape(n, shape)
for x in grid:
    print(*x) #Loops through the list of nested loops and prints each at a new line after unpacking