from datetime import datetime, timedelta
def get_shadow(time):
    time = datetime.strptime(time, "%H:%M")
    hour = time.hour
    minute = time.minute
    current_time = hour + minute / 60
    if current_time < 6 or current_time >= 18 or current_time == 12:
        return "No shadow"
    diff = abs(current_time - 12)
    length = diff ** 3
    if length.is_integer():
        length = int(length)
    if current_time < 12:
        direction = "west"
    else:
        direction = "east"
    return f"{length}ft {direction}"

# Example usage:
print(get_shadow("05:30"))  # Output: "No shadow"
print(get_shadow("12:00"))  # Output: "No shadow"
print(get_shadow("10:00"))  # Output: "8ft west"
