"""Generative Fibonacci Computation

Comes from Rosetta Code: https://rosettacode.org/wiki/Fibonacci_sequence#Generative_3
Is only here since I needed a smaller example for testing the debugger.
"""


def fibGen(n):
    a, b = 0, 1
    while n > 0:
        yield a
        a, b, n = b, a + b, n - 1


for fibno in fibGen(11):
    print(fibno)
