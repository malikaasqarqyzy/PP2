#neighbours of a sign
n = input().split()
for i in range(len(n)):
  n[i] = int(n[i])
for i in range(len(n) - 1):
  if (n[i] > 0 and n[i + 1] > 0) or (n[i] < 0 and n[i + 1] < 0):
    print(n[i], n[i + 1])
    break
