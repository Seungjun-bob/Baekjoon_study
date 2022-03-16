# append를 사용하면 메모리 효율이 떨어짐
# 계속해서 정렬하는 것 또한 메모리 효율 문제

import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)