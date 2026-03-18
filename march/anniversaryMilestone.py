def get_milestone(years):
    if years < 1:
        return "Newlyweds"
    elif years >= 1 and years < 5:
        return "Paper"
    elif years >= 5 and years < 10:
        return "Wood"
    elif years >= 10 and years < 25:
        return "Tin"
    elif years >= 25 and years < 40:
        return "Silver"
    elif years >= 40 and years < 50:
        return "Ruby"
    elif years >= 50 and years < 60:
        return "Gold"
    elif years >= 60 and years < 70:
        return "Diamond"
    elif years >= 70 and years < 100:
        return "Platinum"
    
# Example usage:
print(get_milestone(0))   # Output: "Newlyweds"
print(get_milestone(3))   # Output: "Paper"
print(get_milestone(7))   # Output: "Wood"

def get_milestone_map(years):
    milestones = [
        (0, 1, "Newlyweds"),
        (1, 5, "Paper"),
        (5, 10, "Wood"),
        (10, 25, "Tin"),
        (25, 40, "Silver"),
        (40, 50, "Ruby"),
        (50, 60, "Gold"),
        (60, 70, "Diamond"),
        (70, 100, "Platinum"),
        (100, float('inf'), "Centennial"),
    ]
    for lower, upper, name in milestones:
        if years >= lower and years < upper:
            return name
        
# Example usage:
print(get_milestone_map(0))   # Output: "Newlyweds"
print(get_milestone_map(3))   # Output: "Paper"
print(get_milestone_map(7))   # Output: "Wood"
