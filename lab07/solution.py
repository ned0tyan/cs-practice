import numpy as np


def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []

    return np.asarray(values, dtype=float).reshape(-1, width).tolist()


def block(
    matrix: list[list[float]],
    rows: list[int],
    columns: list[int],
) -> list[list[float]]:
    array = np.asarray(matrix, dtype=float)
    return array[np.ix_(rows, columns)].tolist()


def column_means(matrix: list[list[float]]) -> list[float]:
    if not matrix:
        return []

    means = np.mean(np.asarray(matrix, dtype=float), axis=0)
    return np.round(means, 6).tolist()


def column_range(matrix: list[list[float]], column: int) -> float:
    if not matrix:
        return 0.0

    values = np.asarray(matrix, dtype=float)[:, column]
    return float(round(float(np.ptp(values)), 6))