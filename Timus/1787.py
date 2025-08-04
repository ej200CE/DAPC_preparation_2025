k, n = map(int, input().split())
arr = list(map(int, input().split()))

leftover = 0
for i in range(n):
    throughput = max(arr[i] + leftover - k, 0)
    leftover = throughput
print(leftover)
