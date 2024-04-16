def print_spiral(matrix):
    if not matrix:
        return

    rows, cols = len(matrix), len(matrix[0])
    top = left = 0
    bottom = rows - 1
    right = cols - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            print(matrix[top][i], end=" ")
        top += 1
        
        for i in range(top, bottom + 1):
            print(matrix[i][right], end=" ")
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                print(matrix[bottom][i], end=" ")
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                print(matrix[i][left], end=" ")
            left += 1

matrix = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'J'],
    ['K', 'L', 'M', 'N', 'O'],
    ['P', 'Q', 'R', 'S', 'T'],
    ['U', 'V', 'W', 'X', 'Y']
]

print_spiral(matrix)
