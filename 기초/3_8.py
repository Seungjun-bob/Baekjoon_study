import sys
T = sys.stdin

for i in range(1,int(T.readline())+1):
    a, b = map(int, T.readline().split())
    print("Case #%d: %d + %d ="%(i,a,b),a+b)