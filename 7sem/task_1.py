n = 5
lam = [1, 1.5, .7, 1.2, .5]
v = [.18, .15, .25, .2, .3]
c = [5, 4, 3, 2, 1]
d = .01

mu = [1 / v[i] for i in range(n)]
v_2 = [d + v[i] ** 2 for i in range(n)]
psy = [lam[i] / mu[i] for i in range(n)]
R_N = sum(psy)
print("Коэффициент использования прибора любыми требованиями:", R_N)

w = 0.5 * sum([v_2[i] * lam[i] for i in range(n)]) / (1 - R_N)
print("Средняя продолжительность ожидания в каждой очереди:", w)
print("Среднее время ожидания произвольного заказа на обслуживание:", w)

b = [lam[i] * w for i in range(len(lam))]
[print('Среднее число заказов в', i + 1, 'очереди:', b[i]) for i in range(len(b))]
print('Средняя длина очереди:', sum(b))

cost_f = sum([c[i] * b[i] for i in range(len(b))])
print('Функция стоимости:', cost_f)
