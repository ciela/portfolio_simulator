import sys
import numpy as np
import numpy.random as rnd


A = 0.7
SEED = 10000


def calc_assets(portfolio, days):
    result = SEED
    for _ in range(days):
        seed_a = result * portfolio
        seed_b = result - seed_a
        result = rnd.choice([2.0 * seed_a, 2.0 * seed_b], p=[A, 1.0 - A])
    return result


def main():
    portfolio, days = float(sys.argv[1]), int(sys.argv[2])
    log10_results = []
    for _ in range(1000):
        assets = calc_assets(portfolio, days)
        log10_results.append(np.log10(assets / SEED))
    print(np.histogram(log10_results))


main()
