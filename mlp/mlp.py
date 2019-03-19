#!/usr/bin/python
import math
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('input.xlsx', sheet_name='Sheet1')

# taxa de aprendizagem - learning rate between 0 and 1
lRate = 0.5

# sinal de entrada - input value
x0 = 1  # x0 is always +1
x1 = df['x1']

#  valor desejado - desired value
d = df['d']

# numero de exemplos
nEx = x1.count()

# pesos dos neuronios da primeira camada // w1 = [(0.1, -0.3), (-0.7, 0.4)]
w110 = 0.1
w111 = -0.3
w120 = -0.7
w121 = 0.4

# pesos dos neuronios da camada escondida // w2 = [-0.6, 0.1, -0.8]
w210 = -0.6
w211 = 0.1
w212 = -0.8

log = open("output.txt", "w")  # create/open the file to write the log


'''
1) calculo da entrada liquida para os neuronios da camada escondida
net11 = ((w110 * x0) + (w111 * x1))
net12 = ((w120 * x0) + (w121 * x1))
'''


def calculateNet4HiddenLayer(example):
    net11 = ((w110 * x0) + (w111 * x1[example]))
    net12 = ((w120 * x0) + (w121 * x1[example]))
    log.write('\nnet11: ' + str(net11) + '\tnet12: ' + str(net12))
    return (net11, net12)


'''
2) calculo da funcao de saida para os neuronios da camada escondida
y11 = (1/(1 + math.exp(-net11)))
y12 = (1/(1 + math.exp(-net12)))
'''


def calculateY4HiddenLayer(net11, net12):
    y11 = (1/(1 + math.exp(-net11)))
    y12 = (1/(1 + math.exp(-net12)))
    log.write('\ny11: ' + str(y11) + '\ty12: ' + str(y12))
    return (y11, y12)


'''
3) calculo da entrada liquida para os neuronios de saida
net21 = ((w210*x0) + (w211*y11) + (w212*y12))
'''


def calculateNet4Output(y11, y12):
    net21 = ((w210*x0) + (w211*y11) + (w212*y12))
    log.write('\nnet21: ' + str(net21))
    return net21


'''
4) calculo da funcao de saida para os neuronios da camada de saida
y21 = (1/(1 + math.exp(-net21)))
'''


def calculateY4Output(net21):
    y21 = (1/(1 + math.exp(-net21)))
    log.write('\ny21: ' + str(y21))
    return y21


'''
5) calculo do erro para os neuronios da camada de saida
error = (d - y21)
'''


def calculateError(y21):
    error = (d - y21)
    log.write('\nerror: ' + str(error))
    return error


'''
6) calculo das sensibilidades para os neuronios da camada de saida
s21 = y21*(1-y21)*error
'''


def calculateSensibility4OutputLayer(y21, error):
    s21 = y21*(1-y21)*error
    log.write('\ns21: ' + str(s21))
    return s21


'''
7) calculo das sensibilidades para os neuronios da camada escondida
s11 = y11*(1-y11)*w211*s21
s12 = y12*(1-y12)*w212*s21
'''


def calculateSensibility4HiddenLayer(y11, y12, s21):
    s11 = y11*(1-y11)*w211*s21
    s12 = y12*(1-y12)*w212*s21
    log.write('\ns11: ' + str(s11) + '\ts12: ' + str(s12))
    return (s11, s12)


'''
8) reajuste dos pesos que ligam a camada de saida a camada escondida
w2ij(novo) = w2ij(antigo) + alpha*s2i*f1(met1j)
'''


def balanceWeightOutputLayer(w210, w211, w212, s21, y21):
    w210 = float(format((w210 + lRate*s21*y21), '.2f'))
    w211 = float(format((w211 + lRate*s21*y21), '.2f'))
    w212 = float(format((w212 + lRate*s21*y21), '.2f'))


'''
9)reajuste dos pesos que ligam a camada escondida a camada de entrada
w1ij(novo) = w1ij(antigo) + alpha * s1i * xj
'''


def balanceWeightHiddenLayer(w110, w111, w120, w121, s11, s12, x0, x1):
    w110 = float(format((w110 + lRate*s11*x0), '.2f'))
    w120 = float(format((w120 + lRate*s11*x0), '.2f'))
    w111 = float(format((w111 + lRate*s12*x1), '.2f'))
    w121 = float(format((w121 + lRate*s12*x1), '.2f'))


for i in range(nEx):
    log.write('---------------Exemplo' + str(i))
    (net11, net12) = calculateNet4HiddenLayer(i)
    (y11, y12) = calculateY4HiddenLayer(net11, net12)
    net21 = calculateNet4Output(y11, y12)
    y21 = calculateY4Output(net21)
    error = calculateError(y21)
    s21 = calculateSensibility4OutputLayer(y21, error)
    (s11, s12) = calculateSensibility4HiddenLayer(y11, y12, s21)

log.close()
