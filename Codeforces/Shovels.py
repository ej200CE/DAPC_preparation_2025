import math

t = int(input())
pairs = [tuple(map(int, input().split())) for _ in range(t)]

def largest_divisor(n, ceiling):
    if n % ceiling == 0:
        return ceiling
    ans = 1
    for d in range(1, math.isqrt(n) + 1):
        # Check if d is divider of n
        if n % d == 0:
            if d <= ceiling and d > ans:
                ans = d
            inverse = n // d
            if inverse <= ceiling and inverse > ans:
                ans = inverse
    return ans


for pair in pairs:
    n, k = pair
    if k >= n:
        print(1)
    else:
        print(n//largest_divisor(n, k))





