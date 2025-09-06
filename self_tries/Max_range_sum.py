
def count(A):
    ans = 0
    summ = 0
    for i in range(len(A)):
        summ += A[i]
        ans = max(ans, summ)
        if summ < 0:
            summ = 0
    return ans


A = [4, -5, 3, -4, 4, 5, -4, 4, -5]
summ = count(A)
print(summ)