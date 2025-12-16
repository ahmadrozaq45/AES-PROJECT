import numpy as np

def random_affine_matrix():
    return np.random.randint(0, 2, (8, 8))

def from_flat_list(lst):
    return np.array(lst).reshape(8, 8)
