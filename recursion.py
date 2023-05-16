# Fibonacci numbers: commonly denoted F(n) form a sequence,
# called the Fibonacci sequence, such that each number is the sum of the two preceding ones,
# starting from 0 and 1. That is,F(0) = 0, F(1) = 1. F(n) = F(n - 1) + F(n - 2), for n > 1.
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(3)) # the output is 2
print(fib(4)) # the output is 3
print('--------_---------')
# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of 2/3/4..., if there exists an integer x such that n == 2/3/4...^x.
def ispower(n):
    if n == 1:
        return True
    elif n == 0 or n % 2 != 0:
        return False
    else:
        return ispower(n/2)
print(ispower(4)) # the output is True
print(ispower(5)) # the output is False