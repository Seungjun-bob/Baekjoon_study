import sys
N = int(input())
array = []
for i in range(N):
    x,y =map(int, sys.stdin.readline().split())
    array.append([y,x])
array.sort()
for i in range(N):
    print(array[i][1], array[i][0])
