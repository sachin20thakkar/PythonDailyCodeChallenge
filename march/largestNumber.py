import re
def largest_number(s):
    numbers = re.findall(r'-?\d+\.?\d*', s)
    print(numbers)
    float_numbers = [float(num) if '.' in num else int(num) for num in numbers]
    print(float_numbers)
    return max(float_numbers) if float_numbers else None

# Example usage:
print(largest_number("12;-50,99.9,49.1!-10.1?88?16"))  # Output: 99.9