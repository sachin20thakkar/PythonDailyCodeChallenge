def count_perfect_cubes(a, b):
    count = 0
    low = min(a, b)
    high = max(a, b)
    for num in range(low, high + 1):
        if num < 0:
            cube_root = -round(abs(num) ** (1/3))
        else:
            cube_root = round(num ** (1/3))
        if cube_root ** 3 == num:
            count += 1
    return count

# Test cases
print(count_perfect_cubes(-64, 64))  # 9 (perfect cubes are -64, -27, -8, -1, 0, 1, 8, 27, 64)