#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for ii in range(len(matrix[i])):
            if ii != 0:
                print(" ", end="")
            print("{:d}".format(matrix[i][ii]), end="")
        print()
