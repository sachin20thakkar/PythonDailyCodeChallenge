def convert_words(s):
    if not s:
        return s
    result = ""
    words = s.split()
    result = str(len(words[0]))
    for word in words[1:]:
        if word:
            result += " " + str(len(word))
    return result

# Example usage:
print(convert_words("Hello World"))  # Output: "5 5"
print(convert_words("Python is great"))  # Output: "6 2 5"