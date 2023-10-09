n = int(input())

languages_by_student = [set(input() for _ in range(int(input()))) for _ in range(n)]
all_know = set.intersection(*languages_by_student)
any_know = set.union(*languages_by_student)

print(len(all_know))
for lang in sorted(all_know):
    print(lang)

print(len(any_know))
for lang in sorted(any_know):
    print(lang)
    