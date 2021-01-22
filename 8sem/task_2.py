from math import factorial


def product(_k, _s, _beta):
    prod = 1
    for m in range(1, _s + 1):
        prod *= (_k + m * _beta)
    return prod


def get_p_0(_k, _alpha, _beta, _B):
    res_1 = sum([_alpha ** n / factorial(n) for n in range(0, _k + 1)])
    res_2 = _alpha ** _k / factorial(_k)
    res_3 = sum([_alpha ** s / product(_k, s, _beta) for s in range(1, _B + 1)])
    res = 1 / (res_1 + res_2 * res_3)
    return res


def get_p_n(_n, _alpha, _p_0):
    return (_alpha ** _n / factorial(_n)) * _p_0


def get_p_ks(_k, _s, _alpha, _beta, _p_0):
    res = (_alpha ** (_k + _s)) / (factorial(_k) * product(_k, _s, _beta))
    return res * _p_0


if __name__ == '__main__':
    lambda_ = 3.8  # (19 * 2) / 10
    mu = 3
    v = 1 / 2

    k = 2
    B = 5

    alpha = lambda_ / mu
    beta = v / lambda_

    # а) вероятность того, что все бригады будут сидеть без дела из-за отсутствия овощей
    p_0 = get_p_0(k, alpha, beta, B)
    print("Вероятность того, что все бригады будут сидеть без дела из-за отсутствия овощей:", p_0)

    # б) вероятность того, что привезенные овощи не будут своевременно обработаны;
    p_otk = (alpha - k + sum([(k - n) * get_p_n(n, alpha, p_0) for n in range(0, k + 1)])) / alpha
    print("Вероятность того, что привезенные овощи не будут своевременно обработаны:", p_otk)

    # в) среднее число бригад, занятых обработкой овощей;
    h = sum([n * get_p_n(n, alpha, p_0) for n in range(1, k + 1)]) + \
        k * sum([get_p_ks(k, s, alpha, beta, p_0) for s in range(1, B + 1)])
    print("Среднее число бригад, занятых обработкой овощей:", h)

    # г) доля бригад, простаивающих или занятых обработкой овощей;
    g = k - h
    k_g = g / k
    print("Доля простаивающих бригад:", k_g)

    k_w = 1 - k_g
    print("Доля бригад, занятых обработкой овощей:", k_w)

    # д) среднее число тонн овощей, обработанных за сутки, и среднее число тонн
    # овощей, потерянных за сутки из-за их несвоевременной обработки
    avg_processed = lambda_ * (1 - p_otk)
    print("Среднее число тонн овощей, обработанных за сутки:", avg_processed)

    avg_lost = lambda_ * p_otk
    print("Среднее число тонн овощей, потерянных за сутки:", avg_lost)

    # е) среднее число тонн овощей, ожидающих обработки;
    b = sum([s * get_p_ks(k, s, alpha, beta, p_0) for s in range(1, B + 1)])
    print("Среднее число тонн овощей, ожидающих обработки:", b)

    # Определить необходимое количество бригад,
    # чтобы потери привезенных овощей из-за несвоевременной их обработки составляли не более 10%.
    required_prob = 0.1
    while p_otk >= required_prob:
        k += 1
        p_0 = get_p_0(k, alpha, beta, B)
        p_otk = (alpha - k + sum([(k - n) * get_p_n(n, alpha, p_0) for n in range(0, k + 1)])) / alpha
        print(f"---вероятность отказа равна {p_otk} при {k} бригадах")

    print(f"Чтобы потери привезенных овощей составляли не более 10%, необходимо {k} бригады.")
