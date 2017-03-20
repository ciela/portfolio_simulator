import sys
import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt


A = 0.7
SEED = 10000
TRIAL = 100


def calc_assets(portfolio, days):
    result = SEED
    for _ in range(days):
        seed_a = result * portfolio
        seed_b = result - seed_a
        result = 2 * rnd.choice([seed_a, seed_b], p=[A, 1.0 - A])
    return result


def main():
    portfolio, days = float(sys.argv[1]), int(sys.argv[2])
    log10_results = []
    for _ in range(TRIAL):
        assets = calc_assets(portfolio, days)
        log10_results.append(np.floor(np.log10(assets / SEED)).astype('int'))
    log10_hist, log10_bin, _ = plt.hist(log10_results)
    print(log10_hist)
    print(log10_bin)
    plt.show()


main()
