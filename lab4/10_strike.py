N, K = map(int, input().split())
strike_days = [0] * (N + 1)

for _ in range(K):
    a, b = map(int, input().split())
    day = a
    while day <= N:
        if day % 7 not in [6, 0]:
            strike_days[day] = 1
        day += b

print(sum(strike_days))