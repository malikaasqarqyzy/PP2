#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, 
# between a given range 0 and n.

def div_by_3_4(n):
    return (i for i in range(n+1) if i%3 == 0 and i%4 == 0)

n = int(input())
for num in div_by_3_4(n):
    print(num)