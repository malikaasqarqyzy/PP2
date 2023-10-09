n = int(input())
unique_words = set()

for _ in range(n):
    line = input().split()
    unique_words.update(line)

print(len(unique_words))