
def eval_legendre(n, x, arr):

    if not arr:
        arr = []

    if n == 0:
        return [1.0]
    elif n == 1:
        return [1.0, x]
    else:
        return eval_legendre(n-1, x, arr.insert(0, (1/n+1)*(2 * (n+1) * x * eval_legendre(n, x, arr) - (n) * eval_legendre(n-1, x, arr))))

