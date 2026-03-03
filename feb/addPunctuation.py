def add_punctuation(sentences):
    result = ''
    sentences_length = len(sentences)
    for idx, char in enumerate(sentences):
        if char.isspace() and idx < sentences_length - 1 and sentences[idx+1].isalpha() and sentences[idx+1].isupper():
            result += '.'
        result += char
        
    if sentences and sentences[-1].isalpha():
        result += '.'
    return result

if __name__ == "__main__":
    input_sentences = input("Enter sentence: ")
    result = add_punctuation(input_sentences)
    print(result)
    