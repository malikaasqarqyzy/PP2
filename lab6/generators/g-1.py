#Create a generator that generates the squares of numbers up to some number N.
n = int(input())
generate_squares = (i**2 for i in range(1, n+1))
for square in generate_squares:
    print(square)