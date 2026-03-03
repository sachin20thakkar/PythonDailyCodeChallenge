def is_flat(arr):
    for i in arr:
        if isinstance(i, list):
            return False
    return True

# Test cases
print(is_flat([1, 2, 3]))  # True
print(is_flat([1, [2, 3], 4]))  # False