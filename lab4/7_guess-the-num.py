n = int(input())
possible_numbers = set(range(1, n + 1))

while True:
    query = input()
    if query == "HELP":
        break
    else:
        query_numbers = set(map(int, query.split()))
        response = input()

        if response == "YES":
            possible_numbers.intersection_update(query_numbers)
        else:
            possible_numbers.difference_update(query_numbers)

print(*sorted(possible_numbers))