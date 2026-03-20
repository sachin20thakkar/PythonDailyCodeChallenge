def invert_matrix(matrix):
    inverted = []
    first_value = ''
    second_value = ''
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if first_value == '':
                first_value = matrix[i][j]
            elif second_value == '' and matrix[i][j] != first_value:
                second_value = matrix[i][j]
    
    for i in range(len(matrix)):
        inverted_row = []
        for j in range(len(matrix[i])):
            if matrix[i][j] == first_value:
                inverted_row.append(second_value)
            else:
                inverted_row.append(first_value)
        inverted.append(inverted_row)
    return inverted

# Example usage:
matrix =[
  ["a", "b"],
  ["a", "a"]
]
print(invert_matrix(matrix))  # Output: [['b', 'a'], ['b', 'b']]