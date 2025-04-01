_, m = map(int, input().split())
tarr = list(map(int, input().split()))

st = 1
en = max(tarr)

while st<=en:
  mid = (st+en)//2
  wood_cut = 0

  for t in tarr:
    if t>mid:
      wood_cut += t-mid

  if wood_cut < m:
    en = mid-1
  else:
    st = mid+1

print(en)    