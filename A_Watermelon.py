#Watermelon

# watermelon_weight = int(input())
# if watermelon_weight % 2 == 0:
#     even = watermelon_weight // 2
#     if (even % 2 == 0) and ((watermelon_weight - even) % 2 == 0):
#         print("YES")
#     elif (even+1) % 2 == 0 and (even+1) < watermelon_weight:
#         print("YES")
#     else:
#         print("NO")
# else:
#     print("NO")



# simple version
watermelon_weight = int(input())
if watermelon_weight == 2:
    print("NO")
elif watermelon_weight % 2 == 0:
    print("YES")
else:
    print("NO")