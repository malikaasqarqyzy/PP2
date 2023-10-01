#swap neighbours
n = input().split()
for i in range(len(n)):
  n[i] = int(n[i])
for i in range(0, len(n) - 1, 2):
  n[i], n[i + 1] = n[i + 1], n[i]
for i in range(len(n)):
  print(n[i], end=' ')
