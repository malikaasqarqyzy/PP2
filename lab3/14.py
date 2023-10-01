#unique elems
n = input().split()
for i in range(len(n)):
  n[i] = int(n[i])
for i in range(len(n)):
  cnt = 0
  for j in range(len(n)):
    if n[i] == n[j]:
      cnt += 1
  if cnt == 1:
    print(n[i], end=' ')
