def digital_detox(logs):
    # Convert string timestamps to datetime objects
    from datetime import datetime, timedelta
    timestamps = [datetime.strptime(log, "%Y-%m-%d %H:%M:%S") for log in logs]
    # Count logins per day
    from collections import Counter
    days = [ts.date() for ts in timestamps]
    day_counts = Counter(days)
    if any(count > 2 for count in day_counts.values()):
        return False
    # Check for any two timestamps that are less than 4 hours apart
    for i in range(len(timestamps)):
        for j in range(i + 1, len(timestamps)):
            diff = abs((timestamps[j] - timestamps[i]).total_seconds())
            if diff < 4 * 3600:  # 4 hours in seconds
                return False
    return True

# Test cases
print(digital_detox(["2021-01-01 10:00:00", "2021-01-01 10:30:00", "2021-01-01 11:00:00"]))  # False
print(digital_detox(["2026-02-01 08:00:00", "2026-02-01 12:30:00", "2026-02-01 18:00:00"]))  # True
print(digital_detox(["2026-02-01 08:00:00", "2026-02-01 12:30:00"]))  # True
