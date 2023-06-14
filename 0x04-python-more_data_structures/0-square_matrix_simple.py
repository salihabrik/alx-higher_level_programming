#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result =  [[0 for _ in range(len(row))] for row in matrix]
     for i in range(len(matrix)):
        for s in range(len(matrix[i])):
            result[i][s] = matrix[i][s] ** 2

    return result
