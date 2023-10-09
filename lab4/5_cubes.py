N, M = map(int, input().split())

anya_colors = {int(input()) for _ in range(N)}
borya_colors = {int(input()) for _ in range(M)}

common_colors = anya_colors.intersection(borya_colors)

anya_unique_colors = anya_colors.difference(borya_colors)
borya_unique_colors = borya_colors.difference(anya_colors)

print(len(common_colors))
for color in sorted(common_colors):
    print(color)

print(len(anya_unique_colors))
for color in sorted(anya_unique_colors):
    print(color)

print(len(borya_unique_colors))
for color in sorted(borya_unique_colors):
    print(color)
