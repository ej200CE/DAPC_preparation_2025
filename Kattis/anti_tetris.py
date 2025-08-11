
# input module
h, w = map(int, input().split())

inp = []

for i in range(h):
    inp.append(input())

def rotate(arr):
    ht = len(arr)
    wt = len(arr[0])
    rotated = [[0] * ht for _ in range(wt)]
    for i in range(wt):
        for j in range(ht):
            rotated[i][j] = arr[ht - (j+1)][i]
    return [''.join(row) for row in rotated]

def check(arr):
    ht = len(arr)
    wt = len(arr[0])
    for i in range(wt):
        isdot = False
        for j in range(ht):
            if arr[j][i] == '.':
                isdot = True
            else:
                if isdot == True:
                    return False
    return True 

def output(grid):
    height = len(grid)
    width = len(grid[0])
    result = [['#' if c == '.' else '.' for c in row] for row in grid]
    print(height, width)
    print('\n'.join(''.join(row) for row in result))


grid = inp
for i in range(4):
    if check(grid):
        output(grid)
        break
    else:
        grid = rotate(grid)
    if i == 3:
        print('impossible')