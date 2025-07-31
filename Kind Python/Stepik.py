N = int(input())

lst = [[x2 for x1 in range(N)] for x2 in range(N) ]

for i in range(len(lst)):
    print(*lst[i])