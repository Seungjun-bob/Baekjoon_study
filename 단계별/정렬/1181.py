import sys
N = int(input())
x = [sys.stdin.readline().strip() for _ in range(N)]
x = list(set(x))
x.sort()
x.sort(key=lambda i:len(i))
for i in x:
    print(i)