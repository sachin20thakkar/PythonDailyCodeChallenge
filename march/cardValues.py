def card_values(cards):
    face_cards = {'J': 10, 'Q': 10, 'K': 10, 'A': 1}
    result = []
    for card in cards:
        card_value = card[:-1]  # Get the part of the card that represents its value
        if card_value in face_cards:
            result.append(face_cards[card_value])
        else:
            result.append(int(card_value))
    return result

# Test cases
print(card_values(["2H", "3D", "5S", "9C", "KD"]))  # [2, 3, 5, 9, 10]