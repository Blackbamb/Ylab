import math

import numpy as np
from numpy import exp, sqrt

from itertools import permutations

count = 0
way = []
kol_gor = 5
if int(kol_gor) > 1:
    print(f"Вам нужно объехать {kol_gor} городов")
    p = math.factorial((int(kol_gor) - 1))
    print(f"У вас {p} возможных маршрута!")
else:
    print("Укажите корректное кол-во городов!")
print()

for i in permutations([1, 2, 3, 4, 5]):
    if i[0] == 1:  # создаём условие, что начало пути происходит из города №1
        count += 1
        print(f"{count}) {i}")

print()

print("Координаты городов:")
point_1 = [0, 2]
point_2 = [2, 5]
point_3 = [5, 2]
point_4 = [6, 6]
point_5 = [8, 3]
mylist = [point_1, point_2, point_3, point_4, point_5]
for m in mylist:
    print(f"{mylist.index(m) + 1}) {m}")
X = np.array([0, 2, 5, 6, 8])
Y = np.array([2, 5, 2, 6, 3])
M = np.zeros([kol_gor, kol_gor])
for i in np.arange(0, kol_gor, 1):
    for j in np.arange(0, kol_gor, 1):
        if i != j:
            M[i, j] = sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)  # Заполнение матрицы
        else:
            M[i, j] = float('inf')
print()
print('Матрица расстояний:')
print(M)

way.append(0)
for i in np.arange(1, kol_gor, 1):
    s = []
    for j in np.arange(0, kol_gor, 1):
        s.append(M[way[i - 1], j])
    way.append(s.index(min(s)))  # Индексы пунктов ближайших городов соседей
    for j in np.arange(0, i, 1):
        M[way[i], way[j]] = float('inf')
        M[way[i], way[j]] = float('inf')
S = sum(
    [sqrt((X[way[i]] - X[way[i + 1]]) ** 2 + (Y[way[i]] - Y[way[i + 1]]) ** 2) for i in np.arange(0, kol_gor - 1, 1)]) + sqrt(
    (X[way[kol_gor - 1]] - X[way[0]]) ** 2 + (Y[way[kol_gor - 1]] - Y[way[0]]) ** 2)
num=0
a=0
dist=[]
for i in np.arange(0, kol_gor - 1, 1):
    num=sqrt((X[way[i]] - X[way[i + 1]]) ** 2 + (Y[way[i]] - Y[way[i + 1]]) ** 2)
    a=a+num
    dist.append(a)
dist.append(a+sqrt(
    (X[way[kol_gor - 1]] - X[way[0]]) ** 2 + (Y[way[kol_gor - 1]] - Y[way[0]]) ** 2))
way=[i+1 for i in way]
print()
print(f"{way[0]}->{way[1]}({dist[0]}км)->{way[2]}({dist[1]}км)->{way[3]}({dist[2]}км)->{way[4]}({dist[3]}км)->{way[0]}({dist[4]} км)")

