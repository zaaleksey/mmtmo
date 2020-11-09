
n = 3
lam = [2, 5, 5]
mu = 15

v = 1 / mu
psy = [lam[i] / mu for i in range(len(lam))]

R_n = sum(psy)
print("R_n =", R_n)

w = 0.5 * sum([2 * v ** 2 * lam[i] for i in range(len(lam))]) / (1 - R_n)
print("w =", w)

u = w + v
print("u ", u)

b = [lam[i] * w for i in range(len(lam))]
print("b_i -", b)
print("b =", sum(b))
print("Средняя очередь", sum(b) / len(b))

n = [b[i] + psy[i] for i in range(len(b))]
print("n_i -", n)
print("n =", sum(n))