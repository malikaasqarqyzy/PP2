x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y2 == y1):
  print('YES')
else:
  print('NO')
