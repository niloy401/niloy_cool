
def fibonacci_series(n):
    series = []
    a, b = 0, 1
    
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    
    return series

# Example: Generate Fibonacci series with nth terms
n_terms = 90
result = fibonacci_series(n_terms)
print(result)
