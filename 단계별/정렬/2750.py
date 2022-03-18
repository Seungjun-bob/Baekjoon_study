import sys
# num = int(input())
# nums = []
# for _ in range(num):
#     a = int(input())
#     nums.append(a)
#
# for i in sorted(nums):
#     print(i)


s = sys.stdin.read
input()
l = sorted(map(int, s().split()))
print(*l, sep='\n')