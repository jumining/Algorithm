N = int(input())
C = input()
st = []
num = []
for i in range(N):
    num.append(int(input()))

for c in C:
    if c == '*':
        b = st.pop()
        a = st.pop()
        st.append(a*b)
    elif c == '+':
        b = st.pop()
        a = st.pop()
        st.append(a+b)
    elif c == '-':
        b = st.pop()
        a = st.pop()
        st.append(a-b)
    elif c == '/':
        b = st.pop()
        a = st.pop()
        st.append(a/b)
    else:
        st.append(num[ord(c)-ord('A')])

print(f"{st.pop():.2f}")