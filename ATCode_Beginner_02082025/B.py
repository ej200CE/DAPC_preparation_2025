N, M = map(int, input().split())
A_string = list(map(int, input().split()))
B_string = list(map(int, input().split()))

for i in B_string:
    try:
        index = A_string.index(i)
        A_string.pop(index)
    except:
        pass

print(*A_string)
