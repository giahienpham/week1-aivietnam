import math

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def approx_sin(x, n):
    result = 0
    for i in range(n):
        term = ((-1)**i * x**(2*i + 1)) / factorial(2*i + 1)
        result += term
    return result

def approx_cos(x, n):
    result = 0
    for i in range(n):
        term = ((-1)**i * x**(2*i)) / factorial(2*i)
        result += term
    return result

def approx_sinh(x, n):
    result = 0
    for i in range(n):
        term = (x**(2*i + 1)) / factorial(2*i + 1)
        result += term
    return result

def approx_cosh(x, n):
    result = 0
    for i in range(n):
        term = (x**(2*i)) / factorial(2*i)
        result += term
    return result

x = 3.14
n = 10

print(f"approx_sin(x={x}, n={n})")
print(f">> {approx_sin(x, n)}\n")

print(f"approx_cos(x={x}, n={n})")
print(f">> {approx_cos(x, n)}\n")

print(f"approx_sinh(x={x}, n={n})")
print(f">> {approx_sinh(x, n)}\n")

print(f"approx_cosh(x={x}, n={n})")
print(f">> {approx_cosh(x, n)}\n")

print(f"approx_cos(x={1}, n={10})")
print(f">> {approx_cos(1, 10)}\n")

print(f"approx_sin(x={1}, n={10})")
print(f">> {approx_sin(1, 10)}\n")

print(f"approx_sinh(x={1}, n={10})")
print(f">> {approx_sinh(1, 10)}\n")

print(f"approx_cosh(x={1}, n={10})")
print(f">> {approx_cosh(1, 10)}\n")