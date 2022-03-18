k, h = map(int, input().split())
result = 0
if k%2==0:
    result += (k//2*10)
else:
    result += k//2+1
if h%2==0:
    result += (h//2*10)
else:
    result += h//2+1
print(result)
