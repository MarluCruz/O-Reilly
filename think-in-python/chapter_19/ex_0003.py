def binominal_coeff(n, k):
    return 1 if k == 0 else 0 if n == 0 else  binominal_coeff(n-1, k) + binominal_coeff(n-1, k-1)

if __name__ == "__main__":
    print(binominal_coeff(8, 2))
    