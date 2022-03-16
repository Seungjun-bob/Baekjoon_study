n = map(int, input().split())
n = list(n)
b=0
for i in n:
    if i%5==0:
        print(i)
        break
    else:
        b+=1
if b==len(n):
    print(0)
