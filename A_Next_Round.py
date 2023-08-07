n, k = map(int, input().split())
m = list(map(int, input().split()))
count = 0
kth_score = m[k - 1]

for _ in m:
    if _ >= kth_score and _ > 0:
        count += 1
print(count)