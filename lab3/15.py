#kegelban
n, k = input().split()
n = int(n)
k = int(k)

pins = ['I'] * n

for a in range(k):
  l, r = input().split()
  li = int(l)
  ri = int(r)
  for j in range(li - 1, ri):
    pins[j] = '.'

print(''.join(pins))
