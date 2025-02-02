'''
A. Create a 2D matrix using a LIST of LIST and get the input from the user.
If the matrix is a square matrix, then calculate the sum value for lower triangular matrix elements and upper triangular matrix elements in else block.
Otherwise, throw an out of bound predefined exception with print statement “ Given Matrix is not a square Matrix”.
In the Finally block, print the input matrix.
'''

class NotSquareMatrixException(Exception):
    pass

#Matrix Creation
def create_matrix():
    row=int(input('Enter Row size : '))
    col=int(input('Enter Column size : '))
    print(f'This is a {row}X{col} matrix')
    #Matrix Initialization
    mat=[]
    print('Enter elements in matrix')
    #User Input
    for i in range(row):
        rows=[]
        for j in range(col):
            rows.append(int(input()))
        mat.append(rows)
    return mat,row,col

# Calculate Sum of lower and upper triangle
def calculate_sum_triangular(matrix, size):
    lower_sum = 0
    upper_sum = 0

    for i in range(size):
        for j in range(size):
            if i >= j:
                lower_sum += matrix[i][j]
            if i <= j:
                upper_sum += matrix[i][j]

    return lower_sum, upper_sum

#Printing Matrix
def print_matrix(matrix):
    print('\nMatrix : ')
    for i in range(len(matrix)):
        for j in matrix[i]:
            print(j,end=' ')
        print()

#Main 
def main():
    try:
        matrix, rows, cols = create_matrix()

        if rows != cols:
            raise NotSquareMatrixException("Given Matrix is not a square Matrix")

        # Calculate sums of lower and upper triangular matrices
        lower_sum, upper_sum = calculate_sum_triangular(matrix, rows)
        print(f"Sum of lower triangular matrix elements: {lower_sum}")
        print(f"Sum of upper triangular matrix elements: {upper_sum}")

    except NotSquareMatrixException as e:
        print(e)
    finally:
        # Print the matrix
        #print(matrix)
        print_matrix(matrix)

if __name__ == "__main__":
    main()
