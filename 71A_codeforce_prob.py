for i in range(int(input())):
    w = input()
    l = len(w)
    if l <= 10:
        print(w)
    elif l > 10:
        fl = w[0]
        ll = w[l - 1]
        print(fl+str(l-2)+ll)
