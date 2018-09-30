# Treine o perceptron por 1 ciclo
# x1 = existencia de restricao em nome do cliente (s=1;n=0)
# x2 = tempo de conta no banco > 5 anos (s=1;n=0)
# x3 e x4 = Bairro (centro=11;suburbio=01;outros=00)
# x5 = bens imoveis (s=1;n=0)
# x6 = bens moveis  (s=1;n=0)
# x7 = aplicacoes financeiras (s=1;n=0)
# x8 = experiencia de credito < 1 ano (s=1;n=0)
# x9 = crediario em outro banco (s=1;n=0)

import pandas as pd
import random
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('input.xlsx', sheet_name='Sheet1')

# taxa de aprendizagem - learning rate between 0 and 1
lRate = 0.7  # dado pelo professor

# pesos sinapticos- weights
w = [0.11, -0.83, -0.54, 0.25, 0.89, -0.14, -0.69, -0.48, 0.31, 0.77]
# w = df['w'] nao esta pegando somente os valores, quebrando o log

# sinal de entrada - input value
x0 = 1  # x0 is always +1
x1 = df['x1']
x2 = df['x2']
x3 = df['x3']
x4 = df['x4']
x5 = df['x5']
x6 = df['x6']
x7 = df['x7']
x8 = df['x8']
x9 = df['x9']

# valor desejado - desired value
d = df['d']

# numero de exemplos - examples number
nEx = d.count()

# numero de ciclos - cicles
nC = 1
# ---------------------


def f(net):
    if(net >= 0):
        return 1
    else:
        return 0


# ajustar os pesos - adjust the weights
def balance(w0, w1, w2, w3, w4, w5, w6, w7, w8, w9, x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, d, y):

    w0 = float(format((w0 + lRate*(d-y)*x0), '.2f'))
    w1 = float(format((w1 + lRate*(d-y)*x1), '.2f'))
    w2 = float(format((w2 + lRate*(d-y)*x2), '.2f'))
    w3 = float(format((w3 + lRate*(d-y)*x3), '.2f'))
    w4 = float(format((w4 + lRate*(d-y)*x4), '.2f'))
    w5 = float(format((w5 + lRate*(d-y)*x5), '.2f'))
    w6 = float(format((w6 + lRate*(d-y)*x6), '.2f'))
    w7 = float(format((w7 + lRate*(d-y)*x7), '.2f'))
    w8 = float(format((w8 + lRate*(d-y)*x8), '.2f'))
    w9 = float(format((w9 + lRate*(d-y)*x9), '.2f'))

    return [w0, w1, w2, w3, w4, w5, w6, w7, w8, w9]


log = open("output.txt", "w")  # create/open the file to write the log


for i in range(nC):
    log.write('\t\t\t============ Cicle ' + str(i) + ' ============')
    for n in range(nEx):
        log.write('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t\t\t\tExample ' +
                  str(n+1) + '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        log.write('\t # weights: ' + str(w) + '\n')

        # calculate net
        net = ((w[0] * x0) + (w[1] * x1[n]) + (w[2] * x2[n]) + (w[3] * x3[n]) + (w[4] * x4[n]) + (w[5] * x5[n])
               + (w[6] * x6[n]) + (w[7] * x7[n]) +
               (w[8] * x8[n]) + (w[9] * x9[n])
               )

        log.write('\t # net = ' + str(net) + '\n')

        # calculate f(net)
        y = f(net)

        log.write('\t # f(net) = ' + str(y) + '\n\t # d = ' + str(d[n]) + '\n')

        if(y != d[n]):
            log.write(
                '\t # f(net) != d, adjust the weights\n')

            # adjust the weights
            w = balance(w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[7], w[8], w[9],
                        x0, x1[n], x2[n], x3[n], x4[n], x5[n], x6[n], x7[n], x8[n], x9[n], d[n], y)

            log.write('---------------------------------------------------------------------------\nnew weights: ' +
                      str(w) + '\n---------------------------------------------------------------------------\n\n\n')

        else:
            log.write('\t # f(net) == d\n')
            log.write('---------------------------------------------------------------------------\nbest weights: ' +
                      str(w) + '\n---------------------------------------------------------------------------\n\n\n')

log.close()
