numbers = input().split()
seen = set()

for n in numbers:
    if n in seen:
        print("YES")
    else:
        seen.add(n)
        print("NO")