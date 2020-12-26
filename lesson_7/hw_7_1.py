class Matrix:
    def __init__(self, all_matrix):
        self.all_matrix = all_matrix

    def __str__(self):
        return '\n'.join('\t'.join(map(str, el)) for el in self.all_matrix)

    def __add__(self, other):
        matr = []
        for el in zip(self.all_matrix, other.all_matrix):
            matr.append([sum([i, j]) for i, j in zip(*el)])
        return Matrix(matr)


if __name__ == "__main__":
    list_1 = Matrix([[5, 18, 1], [6, 17, 1], [41, 50, 1]])
    print(list_1, '\n')
    list_2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    print(list_2, '\n')
    print(list_1 + list_2)
