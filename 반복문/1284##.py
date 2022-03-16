n = int(input())

for i in range(n+1):
    for j in range(n+1):
        if i*j==n:
            print(i,j)
            break
        else:
            print("wrong number")