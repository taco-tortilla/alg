"""
ABC106

Problem: 
    B-105
Link:
    https://atcoder.jp/contests/abc106/tasks/abc106_b
"""

n = int(input())

ans = 0
for i in range(1, n + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 8 and i % 2 != 0:
        ans += 1
print(ans)
