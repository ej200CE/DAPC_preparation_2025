word_mapping = {letter: i+1 for i, letter in enumerate("abcdefgh")}
moves = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
N = int(input())
for _ in range(N):
    test = input()
    x = word_mapping[test[0]]
    y = int(test[1])
    count = 0
    for dx, dy in moves:
        if 1 <= x + dx <= 8 and 1 <= y + dy <= 8:
            count += 1
    print(count)

    

    
