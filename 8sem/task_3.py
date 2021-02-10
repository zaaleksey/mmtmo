import matplotlib.pyplot as plt
from math import factorial


def product(_k, _s, _beta):
    prod = 1
    for m in range(1, _s + 1):
        prod *= (_k + m * _beta)
    return prod


def get_p_0(_k, _alpha, _beta):
    res_1 = sum([_alpha ** n / factorial(n) for n in range(0, _k + 1)])
    res_2 = _alpha ** _k / factorial(_k)
    res_3 = sum([_alpha ** s / product(_k, s, _beta) for s in range(1, 500)])
    res = 1 / (res_1 + res_2 * res_3)
    return res


def get_p_n(_n, _alpha, _p_0):
    return (_alpha ** _n / factorial(_n)) * _p_0


def get_p_ks(_k, _s, _alpha, _beta, _p_0):
    res = (_alpha ** (_k + _s)) / (factorial(_k) * product(_k, _s, _beta))
    return res * _p_0


if __name__ == '__main__':
    k = 5
    lambda_ = 2
    v = 1.25
    mu = 1 / v
    mu_ = k * mu

    t_wait = .5
    q_v = 1 / t_wait

    alpha = lambda_ / mu_
    beta = q_v / mu_

    # а) среднее время обработки отделом одной сводки
    v_ = 1 / mu_
    print('Среднее время обработки отделом одной сводки:', v_)

    # б) вероятность того, что сотрудники свободны от работы
    p_0 = get_p_0(1, alpha, beta)
    print('\nВероятность того, что сотрудники свободны от работы:', p_0)

    # в) вероятность того, что в отделе одна сводка обрабатывается, а сводок, ожидающих обработки, нет
    p_1 = get_p_n(1, alpha, p_0)
    print('\nВероятность того, что в отделе одна сводка обрабатывается, а сводок, ожидающих обработки, нет:', p_1)

    # г) среднее число сводок, ожидающих обработки
    b = sum([s * get_p_ks(1, s, alpha, beta, p_0) for s in range(1, 500)])
    print('\nСреднее число сводок, ожидающих обработки:', b)

    # д) процент своевременно использованной информации
    p_otk = b * (beta / alpha)
    print('\nПроцент своевременно использованной информации:', (1 - p_otk) * 100, '%')

    # е) вероятность того, что информация не будет использована из-за того, что до окончания обработки она уже
    # потеряла свою ценность
    print('\nВероятность того, что информация не будет использована из-за того, '
          'что до окончания обработки она уже потеряла свою ценность:', p_otk)

    # Определить процент своевременно использованной информации в зависимости от:

    # а) изменения числа сотрудников – увеличения, но не более, чем в 2 раза (построить график зависимости)

    k_count = list(range(1, k * 2 + 1))
    percent = []

    for i in k_count:
        mu_temp = i * mu
        alpha_temp = lambda_ / mu_temp
        beta_temp = q_v / mu_temp

        p_0 = get_p_0(1, alpha_temp, beta_temp)
        b = sum([s * get_p_ks(1, s, alpha_temp, beta_temp, p_0) for s in range(1, 500)])

        percent.append((1 - (b * (beta_temp / alpha_temp))) * 100)

    plt.plot(k_count, percent)
    plt.title('Процент своевремнно использованной инфомации\nв зависимости от числа сотрудников')
    plt.xlabel('k')
    plt.ylabel('percent')
    plt.grid()
    plt.show()

    # б) изменения времени, необходимого одному сотруднику на обработку каждой сводки данных,
    # за счет механизации труда – уменьшения на 10, 15, 20, …, 50 процентов (построить график зависимости)

    proc = [0, .1, .15, .2, .25, .3, .35, .4, .45, .5]

    v_list = [v - (v * i) for i in proc]
    percent = []

    for i in v_list:
        mu = 1 / i
        mu_ = k * mu

        alpha = lambda_ / mu_
        beta = q_v / mu_

        p_0 = get_p_0(1, alpha, beta)
        b = sum([s * get_p_ks(1, s, alpha, beta, p_0) for s in range(1, 500)])

        percent.append((1 - (b * (beta / alpha))) * 100)

    plt.plot(v_list, percent)
    plt.title('Процент своевремнно использованной инфомации\nв зависимости от изменения времени на обработку')
    plt.xlabel('v')
    plt.ylabel('percent')
    plt.grid()
    plt.show()
