for _ in range(int(input())):
    r, s = input().split()
    for x in s:
        for i in range(int(r)):
            print(x, end='')
    print('')