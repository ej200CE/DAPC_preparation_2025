def is_zero(x):
    return -1e-6 < x and x < 1e-6


def gauss_jordan(A, b):
    n, m = len(A[0]), len(A)
    S = []
    x = [0] * n
    for i in range(m):
        S.append(A[i] + [b[i]])
    S.append(list(range(n)))
    k = diagonalize(S, n, m)
    if k < m:
        for i in range(k, m):
            if not S[i][n] == 0:
                return "ZERO SOLUTIONS", S, x
    for j in range(n):
        x[S[-1][j]] = S[j][-1]
    if k < n:
        for j in range(k, n):
            x[S[-1][j]] = 0
        return "MULTIPLE SOLUTIONS", S, x
    return "ONE SOLUTION", S, x


def diagonalize(S, n, m):
    for k in range(min(n, m)):
        val, i, j = max((abs(S[i][j]), i, j) for i in range(k, m)
                        for j in range(k, n))

        if is_zero(val):
            return k

        # Swap rows:
        S[k], S[i] = S[i], S[k]

        # Swap columns:
        for el in range(m + 1):
            S[el][k], S[el][j] = S[el][j], S[el][k]

        # Dividing pivot row by biggest element:
        pivot = S[k][k]
        for el in range(n + 1):
            S[k][el] /= pivot

        # Subtracting
        for i in range(m):
            if i != k:
                fact = S[i][k]
                for j in range(n + 1):
                    S[i][j] -= fact * S[k][j]

    return min(n, m)


A = [[2, 1, 0],
     [1, -1, 0],
     [3, 0, 0]]  # third column is all zeros → that variable is free
b = [3, 0, 3]
mess, S, x = gauss_jordan(A, b)
print(mess)
print(S)
print(x)
