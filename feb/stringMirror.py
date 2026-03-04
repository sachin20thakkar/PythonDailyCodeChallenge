def mirror(s):
    return s + s[::-1]

# Test cases
print(mirror("abc"))  # "abccba"
print(mirror("hello"))  # "helloolleh"