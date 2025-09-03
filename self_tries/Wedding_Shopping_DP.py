M = 20
price = [[6,4,8],[5,10],[1,5,3,5]]

def shopping_top_down(M:int, price: list[list[int]]) -> str:
    C = len(price)
    reach = [False] * (M + 1)
    reach[0] = True
    for g in range(C):
        new = [False] * (M + 1)
        for s in range(M+1):
            if reach[s]:
                for p in price[g]:
                    if s + p <= M:
                        new[s + p] = True
        reach = new
    for i in range(M, 0, -1):
        if reach[i]:
            return i


def shopping_bottom_up(M:int, price: list[list[int]]) -> str:
    C = len(price)
    states = [[0] * M for _ in range(C)]
    for p in price[0]:
        if M - p >= 0:
            states[0][M-p] = 1
    for row in range(1, C):
        for state in range(M):
            if states[row-1][state] == 1:
                for p in price[row]:
                    r = state - p
                    if r >= 0:
                        states[row][r] = 1
    for s in range(0, M):
        if states[-1][s] == 1:
            return M - s
    return "not reachable"


res = shopping_bottom_up(M, price)
print(res)
