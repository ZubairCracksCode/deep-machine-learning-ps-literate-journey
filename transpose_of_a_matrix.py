# Write a Python function that computes the transpose of a given matrix.
import numpy as np
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	a = np.array(a)
	b = a.T
	return b