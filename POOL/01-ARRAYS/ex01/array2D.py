import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    try:
        if not isinstance(family, list) or not all(isinstance(i, list) for i in family):
            raise ValueError("Input should be a 2D list (list of lists).")
        row_lengths = [len(i) for i in family]
        if len(set(row_lengths)) > 1:
            raise ValueError("All rows in the 2D list must have the same number of elements.")
        np_arr = np.array(family)
        print(f"My shape is : {np_arr.shape}")
        sliced = np_arr[start:end]
        print(f"My new shape is : {sliced.shape}")
        return sliced.tolist()
    except Exception as error:
        print(error)
        return []


family = [
    [1.80, 78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88]
]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
