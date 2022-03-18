a,b = map(int, input().split())

result = 0
a = print()
for i in range(a,b+1):
    if i % 2 !=0:
        result += i
    elif i % 2 ==0:
        result -= i
print(result)