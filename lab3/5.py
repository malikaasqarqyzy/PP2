#greater than neigbours
n = input().split()
for i in range(len(n)):
  n[i] = int(n[i])
cnt = 0
for i in range(1, len(n) - 1):
  if n[i] > n[i - 1] and n[i] > n[i + 1]:
    cnt += 1
print(cnt)