n = int(input())
result = 0
for i in map(int,input().split()):
    if i%5==0:
        result += i
print(result)