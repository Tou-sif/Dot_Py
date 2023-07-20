for test in range(int(input())):
    a = int(input())
    mod = list()
    z = 1
    while a > 0:
        b = a % 10
        if b != 0:
            mod.append(b*z)
        z *= 10
        a = a // 10  # a//= 10
    print(len(mod))
    print(*mod)