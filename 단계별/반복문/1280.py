a,b = map(int, input().split())

result = 0

for i in range(a,b+1):
    if i % 2 !=0:
        if a==i:
            print(str(i),end='')
            result += i
        else:
            print('+' + str(i),end ='')
            result += i
    elif i % 2 ==0:
        print('-' + str(i),end='')
        result -= i
print('=' + str(result))