n = input() # just taking the input and ignoring it (trashing)
letters = input().upper() # s_task 1 completed(get input)

steps_up = steps_down = steps_left = steps_right = 0 # s_task2 completed (Iitialised counter variable)

# s_task3 iterating over
for dir in letters:
    if dir == "U":
        steps_up += 1
    elif dir == "D":
        steps_down += 1
    elif dir == "L":
        steps_left += 1
    else:
        steps_right += 1

# s_task4 making the pairs with u to down and left to right
pairs_ud = min(steps_down, steps_up)*2
pairs_lr = min(steps_left, steps_right)*2

sum = pairs_lr + pairs_ud
print(sum)