n, k = map(int, input().split())

if n <= k:
    print(2)
else:
    time_needed = (2*n + k - 1) // k
    print(time_needed)