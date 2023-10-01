#queen
queens = [input().split() for _ in range(8)]

found = False

for i in range(8):
  for j in range(i + 1, 8):
    x1, y1 = int(queens[i][0]), int(queens[i][1])
    x2, y2 = int(queens[j][0]), int(queens[j][1])
    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
      found = True
      break
  if found:
    break

if found:
  print("YES")
else:
  print("NO")
