def saddle_points(matrix):
    positions = list()
    if len(matrix) > 0:
        rows = len(matrix)
        cols = len(matrix[0])
        try:
            for row in range(rows):
                for col in range(cols):
                    if max(matrix[row]) <= matrix[row][col] <= min([matrix[r][col] for r in range(rows)]):
                        positions.append({'row': row+1, 'column': col+1})
        except Exception:
            raise ValueError('Matrix is not regular!')
    return positions