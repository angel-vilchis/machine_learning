from math import sqrt
from collections import defaultdict

def get_statistics(input_list):
    input_list.sort()
    n = len(input_list)

    # Mean
    mean = sum(input_list) / n

    # Median
    is_even = (n % 2 == 0)
    if is_even: 
        median = (input_list[n // 2 - 1] + input_list[n // 2]) / 2
    else:
        median = input_list[n // 2]

    # Mode
    counts = defaultdict(lambda: 0)
    for num in input_list:
        counts[num] += 1
    mode = max(counts, key=counts.get)

    # Standard Deviation
    mean_squared = 0 
    for i in range(n): 
        mean_squared += (input_list[i] - mean) ** 2
    standard_deviation = sqrt(mean_squared / (n - 1))

    # Sample Variance 
    sample_variance = standard_deviation ** 2

    # Upper Limit and Lower Limit
    upper_limit = mean + (1.96 * standard_deviation / sqrt(n))
    lower_limit = mean - (1.96 * standard_deviation / sqrt(n))
    
    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "sample_variance": sample_variance,
        "sample_standard_deviation": standard_deviation,
        "mean_confidence_interval": [lower_limit, upper_limit],
    }
