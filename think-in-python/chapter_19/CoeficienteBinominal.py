def binominal_coeff(n, k):
    """Compute the binominal coefficiente "n choose k"
     n: number of trials
     k: number of successes
     return: int
    """

    if k == 0:
        return 1
    if n == 0:
        return 0

    res = binominal_coeff(n-1, k) + binominal_coeff(n-1, k-1)
    return res

if __name__ == "__main__":
    print(binominal_coeff(2, 2))