n = 5
# начальные условия
lam = [1, 1.5, .7, 1.2, .5]
v = [.18, .15, .25, .2, .3]
c = [5, 4, 3, 2, 1]
d = .01

mu = [1 / v[i] for i in range(n)]
print('mu:', mu)

v_2 = [d + v[i] ** 2 for i in range(n)]
print('v_2:', v_2)

psy = [lam[i] / mu[i] for i in range(n)]
R_N = []
s = 0
for i in range(n):
    s += psy[i]
    R_N.append(s)
print('R_N:', R_N)

theta = [v[j] / (1 - R_N[j - 1]) for j in range(n)]
theta[0] = v[0]
print('theta:', theta)

delta = [v_2[i] / (2 * v[i]) for i in range(n)]
sigma = []
s = 0
for i in range(n):
    s += psy[i] * delta[i]
    sigma.append(s)

w = [sigma[0] / (1 - R_N[0])]
for i in range(1, n):
    w.append(sigma[i] / ((1 - R_N[i - 1]) * (1 - R_N[i])))
print('Средняя продолжительность ожидания обработки инф. каждого типа:\n', w)

w_random = sum([w[i] * lam[i] / sum(lam) for i in range(n)])
print('Средняя продолжительность ожидания обработки инф. из общего потока:\n', w_random)

F = sum([c[i] * lam[i] * w[i] for i in range(n)])
print('F:', F)
# условия оптимизации абсолютных приоритетов
cond1 = [c[i] / v[i] for i in range(n)]
print("Первое условие:", cond1)

cond2 = [2 * v[i] * c[i] / v_2[i] for i in range(n)]
print("Второе условие:", cond2)

print('\tВторое условие\t\tПервое условие')
for i in range(n):
    print("i =", i, ":", round(cond2[i], 3), '\t\t', round(cond1[i], 3))
