result = []

for j in range(1,10001):
    sum = 0
    for i in str(j):
        sum += int(i)
    result.append(int(j) + sum)
result = list(set(result))

for i in range(1,10001):
    if not i in result:
        print(i)

