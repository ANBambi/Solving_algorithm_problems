T = int(input())


coin = [25, 10, 5, 1]

for i in range(T):
    C = int(input())
    coin_list = []
    for j in range(4):
        if C >= coin[j]:
            coin_list.append(C//coin[j])
            C = C % coin[j]
        else:
            coin_list.append(0)
    print(*coin_list[0:])