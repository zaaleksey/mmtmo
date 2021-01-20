n = 5
lam = [1, 1.5, .7, 1.2, .5]
v = [.18, .15, .25, .2, .3]
c = [5, 4, 3, 2, 1]
d = .01

v_2 = [d + v[i] ** 2 for i in range(n)]
mu = [1 / v[i] for i in range(n)]
psy = [lam[i] / mu[i] for i in range(len(lam))]
R_N = []
s = 0
for i in range(n):
    s += psy[i]
    R_N.append(s)
print('R_N:', R_N)

w = []
for j in range(n):
    if j == 0:
        w.append((0.5 * sum([lam[i] * v_2[i] for i in range(n)])) /
                 (1 - R_N[j]))
    else:
        w.append((0.5 * sum([lam[i] * v_2[i] for i in range(n)])) /
                 ((1 - R_N[j - 1]) * (1 - R_N[j])))
print('Среднее время ожидания в очередях:', w)

w_random = sum([w[i] * lam[i] / sum(lam) for i in range(n)])
print('Среднее время ожидания произвольного заказа:', w_random)

b = [lam[i] * w[i] for i in range(n)]
[print('Среднее число заказов в', i + 1, 'очереди:', b[i]) for i in range(n)]
print('Средняя длина очереди:', sum(b))

F = sum([lam[i] * w[i] * c[i] for i in range(n)]) + sum([c[i] * psy[i] for i in range(n)])
print('F =', F)

fines = [c[i] / v[i] for i in range(n)]
print('Скорости извлечения прибором штрафов из СМО:', fines)
