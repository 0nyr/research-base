from typing import Tuple
import numpy as np

def count_labels(array: np.ndarray) -> dict:
    """
    Count the number of labels in an array and return a dictionary with the counts.
    """
    unique, counts = np.unique(array, return_counts=True)
    return dict(zip(unique, counts))


def dict_to_csv_value(dictionary: dict) -> str:
    """
    Convert a dictionary to a string, to be written as a value to a CSV file (wich doesn't have whitespace as delimiter).
    """
    return " ".join(["class-" + str(key) + "=" + str(value) for (key, value) in dictionary.items()])