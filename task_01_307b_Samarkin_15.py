from pathlib import Path as pth
import matplotlib.pyplot as plt
import numpy as np
import math as m

#Переменные по заданию 15
A = -0.25
x = np.linspace(-10,10,343)

#Функция
def f(x):
  Sum1 = 0
  Sum2 = 0
  for i in range(1,5):
    Sum1 += i * m.cos((i + 1)* x + i)
    Sum2 += i * m.cos((i + 1)* A + i)
  return Sum1 * Sum2

y = [f(_x) for _x in x]

#Открываем ./rsults/task<...>.txt и записываем результат
p = pth('results')
res = p / 'task_01_307b_Samarkin_15.txt'
if p.exists():
  with res.open('w') as f:
    i = 0
    for _x in x:
      f.write(str(_x) + '    ' + str(y[i]) + '\n')
      i += 1
else:
  print("Error: \'results\' dir does not exists")

