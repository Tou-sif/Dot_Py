#Watermelon

watermelon_weight = int(input())
if watermelon_weight % 2 == 0:
    even = watermelon_weight / 2
    if even %2 == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")