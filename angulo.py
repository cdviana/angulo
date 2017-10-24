# -*- coding: utf-8 -*-
from sys import argv
import numpy as np

if len(argv) != 3:
    print u"""\
Rotina para cálculo de ânguo entre pares de planos. Modo de uso:
python angulo.py arquivo_1 arquivo_2

Os arquivos devem ser de rumo de mergulho, mergulho, separados
por um espaço e com uma medida por linha. Ambos os arquivos
devem ter o mesmo número de medidas.
Copyright 2015, Camila Duelis Viana.
"""
    exit()

a = np.loadtxt(argv[1])
b = np.loadtxt(argv[2])

def dircos(rumo, mergulho):
    return np.array((np.sin(rumo)*np.sin(mergulho),
                      np.cos(rumo)*np.sin(mergulho),
                      np.cos(mergulho))).T

dcos_a = dircos(*np.radians(a).T)
dcos_b = dircos(*np.radians(b).T)

angulo = np.degrees(np.arccos((dcos_a*dcos_b).sum(axis=1)))

for a, b, ang in zip(a, b, angulo):
    print u"ângulo entre {a[0]}/{a[1]} e {b[0]}/{b[1]} ==> {ang}".format(a=a, b=b, ang=ang)