import math

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

def choose(n,k):
    return math.factorial(abs(n)) / (math.factorial(abs(k)) * math.factorial(abs(n-k)))
