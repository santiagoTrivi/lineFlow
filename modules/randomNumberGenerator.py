import numpy as np


def randomPoissonNumbers(lambda_: float, variables_amount: int, random_numbers_amount: int):
    matrix = []
    for i in range(random_numbers_amount):
        matrix.append(np.random.poisson(lambda_, variables_amount).tolist())
    return matrix

def randomExponentialNumbers(lambda_, variables_amount, random_numbers_amount):
    matrix = []
    for i in range(random_numbers_amount):
        matrix.append(np.random.exponential(lambda_, variables_amount).tolist())
    return matrix


