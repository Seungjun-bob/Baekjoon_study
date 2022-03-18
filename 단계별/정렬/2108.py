import sys
from collections import Counter

N = int(input())
l = [int(sys.stdin.readline()) for _ in range(N)]
l.sort()
print(round(sum(l)/len(l)))
print(l[N//2])
counter = Counter(l).most_common()
if len(counter) > 1:
    if counter[0][1] == counter[1][1]:
        print(counter[1][0])
    else:
        print(counter[0][0])
else:
    print(counter[0][0])

print(max(l)-min(l))
