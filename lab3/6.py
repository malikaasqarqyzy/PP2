#greatest element
n = input().split()
for i in range(len(n)):
  n[i] = int(n[i])
max_value = max(n)
index_of_max = n.index(max_value)
print(max_value, index_of_max)