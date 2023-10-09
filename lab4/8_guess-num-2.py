n = int(input())
possible_numbers = set(range(1, n + 1))

while True:
    query = input()
    if query == "HELP":
        break
    query_numbers = set(map(int, query.split()))
    
    yes_numbers = possible_numbers.intersection(query_numbers)
    no_numbers = possible_numbers.difference(query_numbers)
    
    if len(yes_numbers) > len(no_numbers):
        print("YES")
        possible_numbers = yes_numbers
    else:
        print("NO")
        possible_numbers = no_numbers

print(*sorted(possible_numbers))