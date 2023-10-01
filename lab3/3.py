#more than previous
a = input().split()
for i in range(1, len(a)):
  a[i] = int(a[i])
  if (a[i] > int(a[i - 1])):
    print(a[i], end=' ')
