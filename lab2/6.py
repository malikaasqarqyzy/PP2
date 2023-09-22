a = int(input())
b = int(input())
c = int(input())
if a == b and b == c and a == c:
  print('3')
elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a) or (
    b == a and b != c) or (c == a and c != b) or (c == b and c != a):
  print('2')
else:
  print('0')
