def count_letters_and_numbers(s):
    letters = 0
    numbers = 0
    for char in s:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            numbers += 1
    letterString = "letter" if letters == 1 else "letters"
    numberString = "number" if numbers == 1 else "numbers"
    return f"The string has {letters} {letterString} and {numbers} {numberString}."

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    result = count_letters_and_numbers(input_string)
    print(result)