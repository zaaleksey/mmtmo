lam = [2, 5, 5]
c = [3, 2, 1]
mu = 15

v = 1 / mu
psy = [lam[i] / mu for i in range(len(lam))]
R_N = sum(psy)
print("Коэффициент использования прибора любыми требованиями:", R_N)

w = 0.5 * sum([2 * v ** 2 * lam[i] for i in range(len(lam))]) / (1 - R_N)
print("Средняя продолжительность ожидания в каждой очереди:", w)
print("Среднее время ожидания произвольного заказа на обслуживание:", w)

b = [lam[i] * w for i in range(len(lam))]
[print('Среднее число заказов в', i + 1, 'очереди:', b[i]) for i in range(len(b))]
print('Средняя длина очереди:', sum(b))

cost_f = sum([c[i] * b[i] for i in range(len(b))])
print('Функция стоимости:', cost_f)
