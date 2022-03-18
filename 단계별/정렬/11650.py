import sys
N = int(input())
x = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
x.sort()
for i in range(N):
    print(x[i][0], x[i][1])
