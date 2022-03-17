import sys
N = int(input())
lst = []
for i in range(N):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    lst.append([age, name])
lst.sort(key=lambda x:x[0])
for j in lst:
    print(j[0],j[1])