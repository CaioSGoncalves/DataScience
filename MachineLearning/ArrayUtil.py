import numpy as np

def one_dim_array_reshape(oneDimArray):
    oneDimArray = np.expand_dims(oneDimArray, axis=1)
    return oneDimArray
