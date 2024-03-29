import sys

N = int(input())
arr = [int(sys.stdin.readline()) for _ in range(N)]
dp = []


if N==1:
    print(arr[0])
    exit()
elif N==2:
    print(max(arr[0]+arr[1],arr[1]))
    exit()

dp.append(arr[0])
dp.append(max(arr[0]+arr[1],arr[1]))
dp.append(max(arr[0]+arr[2],arr[1]+arr[2]))

for i in range(3,N):
    dp.append(max(dp[i-2]+arr[i],dp[i-3]+arr[i-1]+arr[i]))

print(dp.pop())