LMT = 10**12

r = int(LMT**0.5) + 1
primes = [True]*r
primes[0] = primes[1] = False
for i in range(2, r):
    if primes[i]:
        for m in range(i*i, r, i):
            primes[m] = False


n = int(input())
inp = list(map(int, input().split()))

for el in inp:
    root = int(el**0.5)
    if root*root == el and primes[root]:
        print("YES")
    else:
        print("NO")


