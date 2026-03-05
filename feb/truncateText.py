def truncate_text(text):
    if len(text) <= 20:
        return text
    else:
        return text[:17] + "..."
    
# Test cases
print(truncate_text("Hello, World!"))  # "Hello, World!"
print(truncate_text("This is a long piece of text that needs to be truncated."))