import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('exemplo1.xlsx', sheet_name='Sheet1')

lRate = 1  # taxa de aprendizagem - learning rate between 0 and 1
th = 1  # limiar - threshold

# pesos sinapticos- weights
w = df['weight']  # [0, 3, 3]  # w10,w11,w12

# sinal de entrada - input value
x0 = 1  # x0 is always +1
x1 = df['firstInput']  # [0, 0, 1, 1]
x2 = df['secondInput']  # [0, 1, 0, 1]

# valor desejado - desired value
d = df['output']

# numero de exemplos - examples number
nEx = d.count()

# numero de ciclos - cicles
nC = 2
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


for i in range(nC):
    print('============ Cicle ' + str(i) + ' ============')
    for n in range(nEx):
        print('\n-------------------------\nExample ' +
              str(n) + '\n-------------------------')
        print('weights: ' + str(w))

        met1 = ((w[0] * x0) + (w[1] * x1[n]) + (w[2]*x2[n]))
        print('met1 = ' + str(met1))

        y = f(met1)
        print('f(met1) = ' + str(y) + '\nd = ' + str(d[n]))

        if(y != d[n]):
            print('f(met1) != d, adjust the weights\n-------------------------')
            w = balance(w[0], w[1], w[2], x0, x1[n], x2[n], d[n], y)
        else:
            print('-------------------------\nf(met1) == d')
            print('-------------------------\nbest weights: ' +
                  str(w) + '\n-------------------------\n')
