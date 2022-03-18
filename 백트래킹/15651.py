# 탐색 한 값이 x 안에 있으면 거르는 것을 삭제한다.
N, M = map(int, input().split())

x = []

def dfs():
    if len(x) == M:
        print(' '.join(map(str,x)))
        return
    for i in range(1,N+1):
        x.append(i)
        dfs()
        x.pop()

dfs()
