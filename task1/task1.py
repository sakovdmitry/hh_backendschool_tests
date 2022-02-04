N = input().split()
M = int(N[1])
N = int(N[0])
Cn = [int(input()) for i in range(N)]
summa = sum(Cn)
lower_bound = 0
upper_bound = summa // M
while upper_bound - lower_bound > 1:
    center = (lower_bound + upper_bound) // 2
    summa = 0
    for i in range(len(Cn)):
        summa += Cn[i] // center
    if summa < M:
        upper_bound = center
    else:
        lower_bound = center
summa = 0
if upper_bound > 0:
    for i in range(len(Cn)):
        summa += Cn[i] // upper_bound
    if summa >= M:
        lower_bound = upper_bound
print(lower_bound)