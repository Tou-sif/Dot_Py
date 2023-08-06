# p = int(input())
# count = 0
# while p > 0:
#     line = input()
#     vars = line.split()
#     a = int(vars[0])
#     b = int(vars[1])
#     c = int(vars[2])
#     if a+b+c >= 2:
#         count += 1
        
#     p -= 1
# print(count)



test_cases = int(input())
count = 0
for _ in range(test_cases):
    a, b, c = map(int, input().split())
    if a + b + c >= 2:
        count += 1

print(count)