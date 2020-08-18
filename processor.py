def matrix_creator(n_of_matrices=1):
    if n_of_matrices == 1:
        r, c = map(int, input("Enter the size of matrix: ").split())
        print("Enter matrix:")
        matrix = [input().split() for i in range(r)]
        return matrix, r, c
    elif n_of_matrices == 2:
        r_1, c_1 = map(int, input("Enter the size of first matrix: ").split())
        print("Enter the first matrix: ")
        matrix1 = [input().split() for i in range(r_1)]
        r_2, c_2 = map(int, input("Enter the size of second matrix: ").split())
        print("Enter second matrix: ")
        matrix2 = [input().split() for i in range(r_2)]
        return matrix1, r_1, c_1, matrix2, r_2, c_2


def add_matrices(matrix1, rows1, columns1, matrix2, rows2, columns2):
    if rows1 == rows2 and columns1 == columns2:
        summed = [[(float(matrix1[i][j]) + float(matrix2[i][j]))
                   for j in range(columns1)] for i in range(rows1)]
        for p in summed:
            print(*p)
    else:
        print("The operation cannot be performed.")


def multiply_by_constant(matrix, rows, columns, scalar):
    multiplied = [[float(matrix[i][j]) * scalar for j in range(columns)]
                  for i in range(rows)]
    for w in multiplied:
        print(*w)


def multiply_matrices(matrix1, rows1, columns1, matrix2, rows2, columns2):
    if columns1 == rows2:
        product = [[sum(0 + float(matrix1[i][j]) * float(matrix2[j][w])
                   for j in range(rows2)) for w in range(columns2)]
                   for i in range(rows1)]
        for a in product:
            print(*a)
    else:
        print("Operation cannot be performed.")


def transpose_matrix(matrix, rows, columns, version_of_transpose):
    if version_of_transpose == 1:
        transposed = [[matrix[i][j] for i in range(columns)] for j in range(rows)]
    elif version_of_transpose == 2:
        transposed = [[matrix[i][j] for i in reversed(range(columns))]
                      for j in reversed(range(rows))]
    elif version_of_transpose == 3:
        transposed = [matrix[i][::-1] for i in range(rows)]
    elif version_of_transpose == 4:
        transposed = [matrix[i] for i in reversed(range(rows))]
    else:
        print("No such option, sorry.")
        transposed = []  # to avoid warning in the return
    return transposed    # if not for else statement, 'transposed' would be undefined


def matrix_minor(matrix, row, column):  # row and column of the cofactor
    return [line[:column] + line[column + 1:]
            for line in (matrix[:row] + matrix[row + 1:])]
    # skips the row and column of the cofactor, returning the minor matrix


def recursive_determinant(matrix, determinant=0):
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return float(matrix[0][0])
    elif len(matrix) == 2 and len(matrix[0]) == 2:
        return float(matrix[0][0]) * float(matrix[1][1]) \
               - float(matrix[1][0]) * float(matrix[0][1])
    else:
        for fc in range(len(matrix[0])):  # each row's length is the same
            cofactor = (-1) ** (fc % 2)  # 1 or -1 - as we follow the upper line
            # so that the cofactor is always in the first row
            sub_determinant = recursive_determinant(matrix_minor(matrix, 0, fc))
            determinant += cofactor * float(matrix[0][fc]) * sub_determinant
        return determinant


def inverse_matrix(matrix, rows, columns):
    if recursive_determinant(matrix) == 0:
        print("This matrix doesn't have an inverse.")
    else:
        adjoint = [[recursive_determinant(matrix_minor(matrix, i, j))
                    for j in range(columns)] for i in range(rows)]  # minors
        adjoint = transpose_matrix(adjoint, rows, columns, 1)       # determinants of minors
        adjoint = [[((-1) ** ((i + 1) + (j + 1))) * adjoint[i][j]
                    for j in range(columns)]for i in range(rows)]    # transposed
        inversed = [[round((1 / recursive_determinant(matrix)) * adjoint[i][j], 4)
                    for j in range(columns)] for i in range(rows)]
        for x in inversed:
            print(*x)


while True:
    print("""\n1. Add matrices \n2. Multiply matrix by a constant
3. Multiply matrices \n4. Transpose matrix \n5. Calculate a determinant
6. Inverse matrix \n0. Exit""")
    option = int(input("Your choice: "))
    if option == 1:
        add_matrices(*matrix_creator(n_of_matrices=2))  # '*' is placed to extract the returned values
    elif option == 2:
        matrix_1, row1, column1 = matrix_creator(n_of_matrices=1)
        constant = float(input("Enter constant: "))
        print("The result is: ")
        multiply_by_constant(matrix_1, row1, column1, constant)
    elif option == 3:
        multiply_matrices(*matrix_creator(n_of_matrices=2))
    elif option == 4:
        print("""\n1. Main diagonal \n2. Side diagonal
3. Vertical line \n4. Horizontal line""")
        version = int(input("Your choice: "))
        trans = transpose_matrix(*matrix_creator(n_of_matrices=1), version)
        print("The result is:")
        for m in trans:
            print(*m)  # as it returns a list, I am allowed to do this
    elif option == 5:
        det = recursive_determinant(matrix_creator(n_of_matrices=1)[0])  # to access only the matrix
        print(f"The result is: \n{det}")
    elif option == 6:
        inverse_matrix(*matrix_creator(n_of_matrices=1))
    elif option == 0:
        break
