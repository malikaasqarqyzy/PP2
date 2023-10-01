#sherenga
h = input().split()
ph = int(input())
for i in range(len(h)):
  h[i] = int(h[i])
if (h[i] > 0 and h[i] <= 200):
  p = len(h) + 1
  for i in range(len(h)):
    if ph > h[i]:
      p = i + 1
      break
  print(p)
