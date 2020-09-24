class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(num) for num in row.split()] for row in matrix_string.split('\n')]
        # self.matrix = [list(map(int, row.split())) for row in self.matrix]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [col[index-1] for col in self.matrix]