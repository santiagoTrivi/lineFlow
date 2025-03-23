import numpy as np


def randomPoissonNumbers(lambda_: float, variables_amount: int, random_numbers_amount: int):
    matrix = []
    for i in range(random_numbers_amount):
        matrix.append(np.random.poisson(lambda_, variables_amount).tolist())
    stadistics = calculateStadistics(matrix)
    return {
        "matrix": matrix,
        "averages": stadistics["averages"],
        "standard_deviations": stadistics["standard_deviations"]
    }

def randomExponentialNumbers(lambda_, variables_amount, random_numbers_amount):
    matrix = []
    for i in range(random_numbers_amount):
        matrix.append(np.random.exponential(lambda_, variables_amount).tolist())
    stadistics = calculateStadistics(matrix)
    return {
        "matrix": matrix,
        "averages": stadistics["averages"],
        "standard_deviations": stadistics["standard_deviations"]
    }


def calculateStadistics(matrix):
    matrix = np.array(matrix)
    # Select a random row from the matrix
    row_averages = np.mean(matrix, axis=0).tolist()

    standard_deviation = np.std(matrix, axis=0).tolist()

    return {
        "averages": row_averages,
        "standard_deviations": standard_deviation
    }