from math import sqrt


def euler(h, x, y, f, xf):
    while x < xf:
        x += h
        y += h * f(x, y)
    return y


def runga_kutta_2(h, x, y, f, xf):
    h2 = (x + xf) / 2
    while x < xf:
        yln = f(x, y)
        deltay = f(x + h / 2, y + h2 * yln / 2) * h
        x += h
        y += deltay
    return y


def runga_kutta_4(h, x, y, f, xf):
    h2 = (x + xf) / 2.0
    while x < xf:
        sigma1 = h * f(x, y)
        sigma2 = h * f(x + h / 2, y + sigma1 / 2)
        sigma3 = h * f(x + h * h2 / 2, y + sigma2 / 2)
        sigma4 = h * f(x + h, y + sigma3)

        x += h
        y += (sigma1 + 2 * sigma2 + 2 * sigma3 + sigma4) / 6.0
    return y


def convergence_quotient(h, x, y, f, xf, method):
    s = method(h, x, y, f, xf)
    s1 = method(h / 2, x, y, f, xf)
    s2 = method(h / 4, x, y, f, xf)

    qc = abs((s1 - s) / (s2 - s1))
    order = round(sqrt(qc), 0)
    print("Metodo:", method.__name__)
    print("QC:", qc)
    print("Ordem:", order)
    print("Erro:",(s2-s1)/(order**2-1))

    return (s1 - s) / (s2 - s1)
