def gries_misra(n):
    factor = [0]*n
    primes = []
    for x in range(2, n):
        if not factor[x]:
            factor[x] = x
            primes.append(x)
        for p in primes:
            if p > factor[x] or p*x >= n:
                break
            factor[p*x] = p
    return factor, primes

fac, prm = gries_misra(30)
print(fac)
print(prm)










