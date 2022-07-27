def recursive(n, l_arrow):
    if n == 0:
        print(l_arrow)
        return
    for i in range(4):
        l_arrow[i] += 1
        recursive(n-1, l_arrow)
        l_arrow[i] -= 1


recursive(4, [0 for _ in range(4)])
