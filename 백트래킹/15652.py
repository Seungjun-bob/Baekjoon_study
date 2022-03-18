# start를 지정한다
N, M = map(int, input().split())

x = []

def dfs(k):
    if len(x) == M:
        print(' '.join(map(str,x)))
        return
    for i in range(k,N+1):  # 탐색 시작을 k로 지정해준다
        x.append(i)
        dfs(i)
        x.pop()

dfs(1) # 1부터 시작