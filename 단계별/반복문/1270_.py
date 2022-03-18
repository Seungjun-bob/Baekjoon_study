n = input()
result = 0

for i in range(1, int(n)+1):
    i = str(i)
    if int(i[len(i)-1])==1:
        result +=1
print(result)