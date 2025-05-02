import sys
input = sys.stdin.readline

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

st = input().strip()
for c in croatia:
    if c in st:
        st = st.replace(c, '*')
print(len(st))