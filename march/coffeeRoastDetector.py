def detect_roast(beans):
    num_light = 0
    num_medium = 0
    num_dark = 0
    for bean in beans:
        if bean == "'":
            num_light += 1
        elif bean == '-':
            num_medium += 1
        elif bean == '.':
            num_dark += 1

    light_score = num_light * 1
    medium_score = num_medium * 2
    dark_score = num_dark * 3

    roast_score = (light_score + medium_score + dark_score) / (num_light + num_medium + num_dark)

    if roast_score < 1.75:
        return "Light"
    elif roast_score <= 2.5:
        return "Medium"
    else:
        return "Dark"


print(detect_roast("''-''''''-'-''--''''"))  # Output: "Light"
print(detect_roast(".--.-..-......----.'"))  # Output: "Medium"