#paste elem
n = input().split()
for i in range(len(n)):
  n[i] = int(n[i])
k, C = map(int, input().split())
n.append(0)
for i in range(len(n) - 1, k, -1):
  n[i] = n[i - 1]
n[k] = C
for num in n:
  print(num, end=' ')
