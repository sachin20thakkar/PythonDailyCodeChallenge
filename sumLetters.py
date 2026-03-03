def sum_letters(s):
    total = 0
    for char in s:
        if char.isalpha():
            total += ord(char.lower()) - ord('a') + 1
    return total

# Test cases
print(sum_letters("Hello"))  # 52 (8 + 5 + 12 + 12 + 15)
print(sum_letters("freeCodeCamp"))   # 94 (f + r + e + e + c + o + d + e + c + a + m + p = 6 + 18 + 5 + 5 + 3 + 15 + 4 + 5 + 3 + 1 + 13 + 16)
print(sum_letters("</404>"))    # 0 (non-alphabetic characters are ignored)  