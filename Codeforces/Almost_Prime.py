LMT = 3000

factor = [0]*LMT
primes = []
for x in range(2, LMT):
    if not factor[x]:
        factor[x] = x
        primes.append(x)
    for p in primes:
        if p > factor[x] or p*x >= LMT:
            break
        factor[p*x] = p

n = int(input())
count = [0]*(n+1)
for p in primes:
    for m in range(p, n+1, p):
        count[m] += 1

print(sum(1 for x in count if x == 2))


