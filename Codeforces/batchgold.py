n = int(input())
ans = n // 2
if n % 2 == 0:
    print(ans)
    print(*([2] * ans))
else:
    print(ans)
    print(*([2] * ((n-3)//2) + [3]))

