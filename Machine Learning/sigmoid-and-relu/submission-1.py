import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        res = []
        for i in z:
            s = 1 / (1 + np.exp(-1 * i))
            res.append(np.round(s, 5))
        
        return np.array(res)

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        res = []
        for i in z:
            res.append(np.float64(max(0, i)))

        return np.array(res)
