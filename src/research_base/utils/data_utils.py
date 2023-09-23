from typing import Tuple
import numpy as np

def count_labels(array: np.ndarray) -> dict:
    """
    Count the number of labels in an array and return a dictionary with the counts.
    """
    unique, counts = np.unique(array, return_counts=True)
    return dict(zip(unique, counts))