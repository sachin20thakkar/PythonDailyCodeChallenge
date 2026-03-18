def get_flag(code):
    code = code.upper()
    result = ""
    for letter in code:
        result += chr(ord(letter) + 127397)
    return result
# Test cases
print(get_flag("US"))  # Output: 🇺🇸