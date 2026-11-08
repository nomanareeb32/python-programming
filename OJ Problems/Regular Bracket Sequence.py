a = input()
st = []
c = 0
for i in a:
    if i == "(":
        st.append("(")
    else:
        if st == []:
            continue
        st.pop()
        c += 2
print(c)