#Write a Python program that invoke square root function after specific milliseconds.

from time import sleep
import math

def delay(x, ms):
  sleep(ms / 1000)
  return math.sqrt(x)

x = int(input())
ms = int(input())
print("Square root of", x ,"after", ms, "miliseconds is", delay(x, ms))