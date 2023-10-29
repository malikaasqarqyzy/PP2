#Write a program using generator to print the even numbers between 0 and n in comma 
# separated form where n is input from console.

def even_nums(n):
    return (i for i in range(n+1) if i%2 == 0)

n = int(input())
print(",".join(map(str, even_nums(n))))