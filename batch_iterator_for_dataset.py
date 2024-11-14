# Write a Python function to create a batch iterator for the samples in a numpy array X and an optional numpy array y. The function should yield batches of a specified size. If y is provided, the function should yield batches of (X, y) pairs; otherwise, it should yield batches of X only.
# Example:
#     X = np.array([[1, 2], 
#                   [3, 4], 
#                   [5, 6], 
#                   [7, 8], 
#                   [9, 10]])
#     y = np.array([1, 2, 3, 4, 5])
#     batch_size = 2
#     batch_iterator(X, y, batch_size)
#     output:
#     [[[[1, 2], [3, 4]], [1, 2]],
#      [[[5, 6], [7, 8]], [3, 4]],
#      [[[9, 10]], [5]]]

#      Reasoning:
#     The dataset X contains 5 samples, and we are using a batch size of 2. Therefore, the function will divide the dataset into 3 batches. The first two batches will contain 2 samples each, and the last batch will contain the remaining sample. The corresponding values from y are also included in each batch.
import numpy as np
import math
X = np.array([[1, 2], 
                  [3, 4], 
                  [5, 6], 
                  [7, 8], 
                  [9, 10]])
y = np.array([1, 2, 3, 4, 5])
batch_size = 2

# ti = math.ceil(len(X)/batch_size)
# flag = 0

# list = []

# for _ in range(ti):
#     sublist = [[], []] if y is not None else [[]]
#     for _ in range(batch_size):
#         if flag <= (len(X)-1):
#             sublist[0].append(X[flag].tolist())
#             if y is not None:
#                 sublist[1].append(y[flag])
#             flag += 1
#         else:
#             break
#     list.append(sublist)
# print(list)

# import numpy as np

n_samples = X.shape[0]
print("n_samples: ",n_samples)
batches = []
for i in np.arange(0, n_samples, batch_size):
    begin, end = i, min(i+batch_size, n_samples)
    print(f"Begin: {begin}, End:{end}, I: {i}")
    if y is not None:
        batches.append([X[begin:end], y[begin:end]])
    else:
        batches.append( X[begin:end])