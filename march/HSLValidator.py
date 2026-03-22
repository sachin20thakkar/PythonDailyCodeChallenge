def is_valid_hsl(hsl):
    if not isinstance(hsl, str):
        return False
    if not hsl.startswith('hsl('):
        return False

    start_index = hsl.find('(') + 1
    end_index = hsl.find(')', start_index)
    content = hsl[start_index:end_index]
    parts = content.split(',')
    if not (0 <= int(parts[0].strip()) <= 360):
        return False
    if not parts[1].strip().endswith('%') or not (0 <= int(parts[1].strip().rstrip('%')) <= 100):
        return False
    if not parts[2].strip().endswith('%') or not (0 <= int(parts[2].strip().rstrip('%')) <= 100):
        return False

    if len(parts) != 3:
        return False

    return True

# Example usage:
print(is_valid_hsl("hsl(120, 100%, 50%)"))  # Output: True
print(is_valid_hsl("hsl(360, 0%, 0%)"))  # Output: True
print(is_valid_hsl("hsl(361, 100%, 50%)"))  # Output: False
print(is_valid_hsl("hsl(120, 101%, 50%)"))  # Output: False
print(is_valid_hsl("hsl (80, 20%, 10%)"))  # Output: False