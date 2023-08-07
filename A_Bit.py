test_case = int(input())
X = 0

for _ in range(test_case):

    opr = input()
    if opr  == "X++":
        X += 1
    elif opr  == "++X":
        X += 1
    elif opr == "X--":
        X -= 1
    elif opr == "--X":
        X -= 1
    sum = X
print(sum)

