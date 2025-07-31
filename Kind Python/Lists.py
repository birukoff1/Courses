Input = input().split()
Input = [x.split('=') for x in Input]

print(Input)

d = dict(Input)
for i in d:
    d[i] = int(d[i])
print(*sorted(d.items()))