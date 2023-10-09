common = list(map(int, set(input().split()) & set(input().split())))
print(' '.join(map(str, sorted(common))))