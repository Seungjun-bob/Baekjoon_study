import sys
n = int(sys.stdin.readline())
result=[]
for i in range(1,n+1):
    result.append(i)
result=result[::-1]
for i in result:
    print(i)

import sys
N=int(sys.stdin.readline())
for i in range(N):
    print(N-i)