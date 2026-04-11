import numpy as np
from numpy.typing import NDArray


class Solution:

    def binary_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        # y_true: true labels (0 or 1)
        # y_pred: predicted probabilities
        # Hint: add a small epsilon (1e-7) to y_pred to avoid log(0)
        # return round(your_answer, 4)
        loss = np.float64(0)
        for i in range(len(y_true)):
            yi = y_true[i]
            pi = y_pred[i] + 1e-7
            loss += (
                yi * np.log(pi) + (1-yi) * np.log(1-pi)
            )
        return round(loss / len(y_true) * -1, 4)

    def categorical_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        # y_true: one-hot encoded true labels (shape: n_samples x n_classes)
        # y_pred: predicted probabilities (shape: n_samples x n_classes)
        # Hint: add a small epsilon (1e-7) to y_pred to avoid log(0)
        # return round(your_answer, 4)
        n, c = len(y_true), len(y_true[0])
        loss = np.float64(0)
        for i in range(n):
            for j in range(c):
                yic, pic = y_true[i][j], y_pred[i][j] + 1e-7
                loss += (
                    yic * np.log(pic)
                )
        
        return round(-1 * loss / n, 4)
