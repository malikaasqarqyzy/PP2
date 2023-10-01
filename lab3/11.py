#delete elem
n = input().split()
for i in range(len(n)):
  n[i] = int(n[i])
k = int(input())
for i in range(k, len(n) - 1):
  n[i] = n[i + 1]
n.pop()
for i in range(len(n)):
  print(n[i], end=' ')
