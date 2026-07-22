import bisect
st="qwertyuiopasdfghjkl;zxcvbnm,./"
res=""
t = input()
s = input()
for i in s:
    if t=="L":
        pos = st.index(i)
        res=res+st[pos+1]
    else:
        pos = st.index(i)
        res=res+st[pos-1]
print(res)        