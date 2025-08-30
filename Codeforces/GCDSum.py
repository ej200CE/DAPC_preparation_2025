def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)

def gcdSum(n):
    return gcd(n, sum(map(int, str(n))))

n = int(input())
ns = [int(input()) for _ in range(n)]

for val in ns:
    while gcdSum(val) == 1:
        val += 1
    print(val)


