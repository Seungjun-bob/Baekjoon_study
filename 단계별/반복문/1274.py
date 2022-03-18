n = int(input())
result = []
for i in range(1,n+1):
    if n%i ==0:
        result.append(i)
        
if len(result)==2:
    print("prime")
else:
    print("not prime")