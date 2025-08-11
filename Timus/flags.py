N = int(input())

if N <= 2:
    print(2)
else:
    dpW = [0] * (N+1)
    dpR = [0] * (N+1)

    dpW[1] = 1 
    dpR[1] = 1 

    dpW[2] = 1
    dpR[2] = 1

    for i in range(3, N+1):
        dpR[i] = dpW[i-1] + dpW[i-2]
        dpW[i] = dpR[i-1] + dpR[i-2]

    print(dpW[N] + dpR[N])