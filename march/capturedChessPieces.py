from collections import Counter

def get_captured_value(pieces):
    piece_values = {
        'P': {'value': 1, 'count': 8},  # Pawn
        'N': {'value': 3, 'count': 2},  # Knight
        'B': {'value': 3, 'count': 2},  # Bishop
        'R': {'value': 5, 'count': 2},  # Rook
        'Q': {'value': 9, 'count': 1},   # Queen
        'K': {'value': 0, 'count': 1}    # King
    }

    current_piece = dict(Counter(pieces))
    
    total_value = 0
    for piece, piece_info in piece_values.items():
        if piece == 'K' and current_piece.get(piece, 0) == 0:
            return "Checkmate"
        current_piece_count = current_piece.get(piece, 0)
        total_value += piece_info.get('value', 0) * (piece_info.get('count', 0) - current_piece_count)
        
    
    return total_value

# Example usage:
print(get_captured_value(["P", "P", "P", "P", "P", "R", "B"])) # Output: "Checkmate"