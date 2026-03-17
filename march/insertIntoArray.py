def insert_into_array(arr, value, index):
    if index < 0 or index > len(arr):
        raise IndexError("Index out of bounds")
    arr.insert(index, value)
    return arr

print(insert_into_array([2, 4, 8, 10], 6, 2))  # Output: [2, 4, 6, 8, 10]