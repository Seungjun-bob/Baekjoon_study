n, m = map(int, input().split())

x = []
def dfs():
    if len(x) == m:
        print(' '.join(map(str, x)))
        return

    for i in range(1, n + 1):
        if i not in x:
            x.append(i)
            dfs()
            x.pop()


dfs()