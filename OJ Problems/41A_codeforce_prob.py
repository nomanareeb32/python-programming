s = input()
t = input()
t_is_s = True
if len(s) == len(t):
    head = 0
    tail = len(t)
    while head < len(s):
        if s[head] != t[tail-1]:
            t_is_s = False
            break
        else:
            head += 1
            tail -= 1
else:
    t_is_s = False
if t_is_s:
    print('YES')
else:
    print('NO')
