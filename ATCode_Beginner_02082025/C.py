
N = int(input())
A_string = list(map(int, input().split()))

count = 0
dictionary = {}

for pos in range(N):

    j_Aj = pos - A_string[pos]
    i_Ai = pos + A_string[pos]

    if j_Aj in dictionary:
        count += dictionary[j_Aj]

    dictionary[i_Ai] = dictionary.get(i_Ai, 0) + 1

print(count)






