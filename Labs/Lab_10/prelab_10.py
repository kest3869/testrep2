
def eval_legendre(n, x):
    if n == 0:
        return [1.0]
    elif n == 1:
        return [1.0, x]
    else:
        phi = [1.0, x]
        for i in range(2, n + 1):
            phi_next = (1/i)((2 * (i - 1)) * x * phi[-1] - (i - 1) * phi[-2])
            phi.append(phi_next)
        return phi
