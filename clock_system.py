a, b = map(int, input().split(":"))  # "23:10"=> (23 10) = (a,b)
if a == 0 and b == 0:
    print(f"{12}:{b} pm")
elif a < 12:
    # print("%d:%d %s" % (a, b, 'am'))
    print(f"{a}:{b} am")
elif a > 12:
    a -= 12
    print(f"{a}:{b} pm")
elif a == 12:
    print(f"{a}:{b} pm")
