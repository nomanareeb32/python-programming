a = ''
for i in s:
    if i.isalnum():
        a += i.lower()
if a == a[::-1]:
    return true
else:
    return false
