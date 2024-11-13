# Write a Python function that takes the dot product of a matrix and a vector. return -1 if the matrix could not be dotted with the vector

def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])->list[int|float]:
	c = []
	if not a or not b or any(len(sublist) != len(b) for sublist in a):
		return -1
	for sublist in a:
		sum_value = []
		[sum_value.append(sublist[i] * b[i]) for i in range(len(sublist))]
		c.append(sum(sum_value))
	return c