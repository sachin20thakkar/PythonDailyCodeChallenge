def count_change(change):
    # Implementation for counting change
    dollar = 0
    cents = 0
    for coin in change:
        cents += coin
        if cents >= 100:
            dollar += cents // 100
            cents %= 100
    return f"${dollar}.{cents:02d}"

# Example usage:
print(count_change([25, 10, 5, 1]))  # Output: $0.41
print(count_change([100, 50, 25, 25]))  # Output: $2.00