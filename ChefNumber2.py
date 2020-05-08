for t in range(int(input())):
    n = int(input())
    r = [int(x) for x in input().split()]
    l = []
    m = []
    for i in range(n - 1):
        if r[i] == 0:
            continue
        elif r[i] == r[i + 1]:
            r[i + 1] = 0
    for i in r:
        if i != 0:
            l.append(i)
    for i in l:
        m.append(l.count(i))
    h = max(m)
    d = dict(zip(l, m))
    dish = []
    for keys in d:
        if d[keys] == h:
            dish.append(keys)
    print(min(dish))
