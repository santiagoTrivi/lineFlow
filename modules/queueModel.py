ROUND_DIGITS = 8

def calculate_unlimited(lambda_, mu):
    if lambda_ >= mu:
        raise ValueError("Lambda debe ser menor que Mu")

    rho = round((lambda_ / mu), 4)
    Po = 1 - rho
    Ls = lambda_ / (mu - lambda_)
    Lq = rho * Ls
    Ws = 1 / (mu - lambda_)
    Wq = rho / (mu - lambda_)
    lambda_eff = lambda_

    return {
        "Lambda": lambda_,
        "Mu": mu,
        "Rho": rho,
        "Po": Po,
        "Ls": Ls,
        "Lq": Lq,
        "Ws": Ws,
        "Wq": Wq,
        "Lambda_eff": lambda_eff,
        "Prob_dist": calculate_prob_dist_unlimited(lambda_, mu)
    }


def calculate_limited(lambda_, mu, N):
    if lambda_ == mu:
        rho = 1
        Po = 1 / (N + 1)
        Ls = N / 2
        Lq = (N * (N - 1)) / (2 * (N + 1))
        Ws = Ls / (lambda_ * (1 - Po))
        Wq = Lq / (lambda_ * (1 - Po))
        lambda_eff = lambda_ * (1 - Po)
    else:
        rho = lambda_ / mu
        Po = (1 - rho) / (1 - rho**(N + 1))
        Ls = rho * (1 - (N + 1) * rho**N + N * rho**(N + 1)) / ((1 - rho) * (1 - rho**(N + 1)))
        Lq = Ls - (1 - Po)
        Ws = Ls / (lambda_ * (1 - Po))
        Wq = Lq / (lambda_ * (1 - Po))
        lambda_eff = lambda_ * (1 - Po)

    return {
        "Lambda": lambda_,
        "Mu": mu,
        "Rho": rho,
        "Po": Po,
        "Ls": Ls,
        "Lq": Lq,
        "Ws": Ws,
        "Wq": Wq,
        "Lambda_eff": lambda_eff,
        "Prob_dist": calculate_prob_dist_limited(lambda_, mu, N)
    }


def calculate_prob_dist_unlimited(lambda_, mu):
    rho = lambda_ / mu
    prob_dist = []
    Fn = 0
    n = 0

    while Fn < 0.9999 or Fn == 1:
        Pn = (1 - rho) * rho**n
        Fn += Pn
        prob_dist.append({"n": n, "Pn": Pn, "Fn": Fn})
        n += 1

    return prob_dist

def calculate_prob_dist_limited(lambda_, mu, N):
    rho = lambda_ / mu
    prob_dist = []
    Fn = 0
    for n in range(N + 1):
        if rho == 1:
            Pn = 1 / (N + 1)
        else:
            Pn = (1 - rho) * rho**n / (1 - rho**(N + 1))
        Fn += Pn
        prob_dist.append({"n": n, "Pn": Pn, "Fn": Fn})
    return prob_dist