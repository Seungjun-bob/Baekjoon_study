import sys

N = int(input())
x = list(map(int, sys.stdin.readline().split()))
x2 = sorted(list(set(x)))
print(x)
print(x2)

dic = {x2[i]: i for i in range(len(x2))}
print(dic)
for i in x:
    print(dic[i], end=' ')