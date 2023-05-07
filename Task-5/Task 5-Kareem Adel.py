def get_measures_of_spread(numbers):
    numbers = sorted(numbers)
    n = len(numbers)
 
    q1 = numbers[n//4]        # Calculate quartiles
    q2 = numbers[n//2]        # Calculate quartiles
    q3 = numbers[(3*n)//4]    # Calculate quartiles
    
    data_range = numbers[-1] - numbers[0]         # Calculate range and interquartile range
    iqr = q3 - q1                                # Calculate range and interquartile range
    
    mean = sum(numbers) / n                                 # Calculate variance and standard deviation
    variance = sum((x-mean)**2 for x in numbers) / (n-1)   # Calculate variance and standard deviation
    stdev = variance ** 0.5                               # Return the measures of spread
    
    return [numbers[0], q1, q2, q3, numbers[-1]], [data_range, iqr], [variance, stdev] # Return the measures of spread

# test numbers
numbers = [23, 45, 12, 67, 34, 89, 56, 43, 21, 78]
spread = get_measures_of_spread(numbers)
print("Measures of spread:", spread)