N1 = int(input())
values = set(map(int, input().split()))
N2 = int(input())
values = values & set(map(int, input().split()))
N3 = int(input())
values = values & set(map(int, input().split()))
print(len(values)) 


