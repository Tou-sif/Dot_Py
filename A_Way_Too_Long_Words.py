test_cases = int(input())
for _ in range(test_cases):
    words = input()
    f_letter = words[0]
    l_letter = words[-1]
    if len(words) > 10:
        
        print(f"{f_letter}{len(words) - 2}{l_letter}")
    else:
        print(words)
