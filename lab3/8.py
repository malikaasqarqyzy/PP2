#Number of different elements
n = input().split()
for i in range(len(n)):
  n[i] = int(n[i])
cnt = 1 if len(n) > 0 else 0
for i in range(1, len(n)):
  if n[i] != n[i - 1]:
    cnt += 1
print(cnt)
