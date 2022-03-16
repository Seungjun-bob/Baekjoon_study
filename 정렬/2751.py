import sys
N = int(input())
l = [int(sys.stdin.readline()) for _ in range(N)]
l.sort()
[print(l[_]) for _ in range(N)]
