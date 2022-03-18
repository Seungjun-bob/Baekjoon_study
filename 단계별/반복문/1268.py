n = int(input())
result = []
for i in map(int,input().split()):
    if i%2==0:
        result.append(i)
print(len(result))