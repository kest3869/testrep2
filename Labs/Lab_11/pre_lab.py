
# code from ChatGPT
def composite_trapezoidal_rule(a, b, f, N):
    h = (b - a) / N
    result = 0.5 * (f(a) + f(b))
    for i in range(1, N):
        result += f(a + i * h)
    result *= h
    return result

def simpsons_rule(a, b, f, N):
    h = (b - a) / N
    result = f(a) + f(b)
    for i in range(1, N, 2):
        result += 4 * f(a + i * h)
    for i in range(2, N-1, 2):
        result += 2 * f(a + i * h)
    result *= h / 3
    return result

# Example usage:
def example_function(x):
    return x**2

a, b = 0, 2
N = 100

trapezoidal_result = composite_trapezoidal_rule(a, b, example_function, N)
simpsons_result = simpsons_rule(a, b, example_function, N)

print(f"Composite Trapezoidal Rule result: {trapezoidal_result}")
print(f"Simpson's Rule result: {simpsons_result}")
