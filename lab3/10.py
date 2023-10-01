#swap min and max
n = input().split()
for i in range(len(n)):
  n[i] = int(n[i])
mxi = n.index(max(n))
mni = n.index(min(n))
n[mxi], n[mni] = n[mni], n[mxi]
for i in range(len(n)):
  print(n[i], end=' ')