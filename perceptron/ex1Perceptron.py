import pandas as pd
import random
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('exemplo1.xlsx', sheet_name='Sheet1')

lRate = random.random()  # taxa de aprendizagem - learning rate between 0 and 1
th = 1  # limiar - threshold

# pesos sinapticos- weights
w = [random.random() for _ in range(0, 3)]  # w10,w11,w12

# sinal de entrada - input value
x0 = 1  # x0 is always +1
x1 = df['firstInput']  # [0, 0, 1, 1]
x2 = df['secondInput']  # [0, 1, 0, 1]

# valor desejado - desired value
d = df['output']

# numero de exemplos - examples number
nEx = d.count()

# numero de ciclos - cicles
nC = 10
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


log = open("output.txt", "w")  # create/open the file to write the log


for i in range(nC):
    log.write('============ Cicle ' + str(i) + ' ============')
    for n in range(nEx):
        log.write('\n-------------------------\nExample ' +
                  str(n) + '\n-------------------------\n')
        log.write('weights: ' + str(w) + '\n')

        met1 = ((w[0] * x0) + (w[1] * x1[n]) + (w[2]*x2[n]))
        log.write('met1 = ' + str(met1) + '\n')

        y = f(met1)
        log.write('f(met1) = ' + str(y) + '\nd = ' + str(d[n]) + '\n')

        if(y != d[n]):
            log.write(
                'f(met1) != d, adjust the weights\n-------------------------\n')
            w = balance(w[0], w[1], w[2], x0, x1[n], x2[n], d[n], y)
        else:
            log.write('\n-------------------------\nf(met1) == d\n')
            log.write('\n-------------------------\nbest weights: ' +
                      str(w) + '\n-------------------------\n')

log.close()
