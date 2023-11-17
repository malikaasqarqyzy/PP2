#Write a Python program with builtin function to multiply all the numbers in a list

def multiply(nums):
    res = 1
    for num in nums:
        res *= num
    return res

nums = [int(x) for x in input().split()]
result = print(multiply(nums))