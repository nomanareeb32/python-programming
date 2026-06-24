while True:
    try:
        m, n = map(int, input().split())
        if m >= n:
            d = m
            m = n
            n = d
        a = 1
        for i in range(2, m + 1):
            a *= i
        b = a
        for i in range(m + 1, n + 1):
            b *= i
        print(a + b)
    except EOFError:
        break
