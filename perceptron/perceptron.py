#!/usr/bin/python

lRate = 1  # taxa de aprendizagem - learning rate between 0 and 1
th = 1  # limiar - threshold

# pesos sinapticos- weights
w = [0, 3, 3]  # w10,w11,w12

# sinal de entrada - input value
x0 = 1  # x0 is always +1
x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]

# valor desejado - desired value
d = [0, 0, 0, 1]

# numero de exemplos - examples number
nEx = 4
# ---------------------


def f(met):
    if(met >= 0):
        return 1
    else:
        return 0


def balance(w10, w11, w12, x0, x1, x2, d, y):  # ajustar os pesos - adjust the weights
    w10 = w10 + lRate*(d-y)*x0
    w11 = w11 + lRate*(d-y)*x1
    w12 = w12 + lRate*(d-y)*x2
    return [w10, w11, w12]


for n in range(nEx):
    y = f(w[0] * x0) + (w[1] * x1[n]) + (w[2]*x2[n])
    if(y != d[n]):
        print(w)
        w = balance(w[0], w[1], w[2], x0, x1[n], x2[n], d[n], y)
        print(w)
    else:
        print(y)


#file = open("weights.txt", "w")

# print(w)
# file.close
#met1(w10, w11, w12, x0, x1, x2)
