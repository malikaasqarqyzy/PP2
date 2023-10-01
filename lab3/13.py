#number of pairs
n = input().split()
for i in range(len(n)):
  n[i] = int(n[i])
pairs = 0
for i in range(len(n)):
  for j in range(i + 1, len(n)):
    if n[i] == n[j]:
      pairs += 1
print(pairs)
