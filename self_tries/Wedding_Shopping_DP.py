M = 20
price = [[6,4,8],[5,10],[1,5,3,5]]

def shopping(M:int, price: list[list[int]]) -> str:
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

res = shopping(M, price)
print(res)
