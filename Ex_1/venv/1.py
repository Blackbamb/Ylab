#Задание 1
#Оптимальный путь для 5 городов
import math
from itertools import *

count = 0

print('Сколько городов нужно объехать?') #Для решения нашей задачи необходимо ввести 5
#kol_gor=input() #для решения нашей задачи скорее не нужно
kol_gor=5
if int(kol_gor) > 1:
    print(f"Вам нужно объехать {kol_gor} городов")
    p=math.factorial((int(kol_gor)-1))
    print(f"У вас {p} возможных маршрута!")
else:
    print("Укажите корректное кол-во городов!")
print()

for i in permutations('12345'):
    count += 1
    print(f"{count}) {i}")
    print()
    if count == 24:
        break

print()

print("Координаты городов:")
point_1 = (0, 2)
point_2 = (2, 5)
point_3 = (5, 2)
point_4 = (6, 6)
point_5 = (8, 3)
mylist=[point_1,point_2,point_3,point_4,point_5]
math.sqrt(9)
for m in mylist:
    print(m)
r12=math.sqrt((point_2[0]-point_1[0])**2+(point_2[1]-point_1[1])**2)
r13=math.sqrt((point_3[0]-point_1[0])**2+(point_3[1]-point_1[1])**2)
r14=math.sqrt((point_4[0]-point_1[0])**2+(point_4[1]-point_1[1])**2)
r15=math.sqrt((point_5[0]-point_1[0])**2+(point_5[1]-point_1[1])**2)
r23=math.sqrt((point_3[0]-point_2[0])**2+(point_3[1]-point_2[1])**2)
r24=math.sqrt((point_4[0]-point_2[0])**2+(point_4[1]-point_2[1])**2)
r25=math.sqrt((point_5[0]-point_2[0])**2+(point_5[1]-point_2[1])**2)
r34=math.sqrt((point_4[0]-point_3[0])**2+(point_4[1]-point_3[1])**2)
r35=math.sqrt((point_5[0]-point_3[0])**2+(point_5[1]-point_3[1])**2)
r45=math.sqrt((point_5[0]-point_4[0])**2+(point_5[1]-point_4[1])**2)

m12345=r12+r23+r34+r45+r15#1
m12354=r12+r23+r35+r45+r14#2
m12435=r12+r24+r34+r35+r15#3
m12453=r12+r24+r45+r35+r13#4
m12534=r12+r25+r35+r34+r14#5
m12543=r12+r25+r45+r34+r13#6
m13245=r13+r23+r24+r45+r15#7
m13254=r13+r23+r25+r45+r14#8
m13425=r13+r34+r24+r25+r15#9
m13452=r13+r34+r45+r25+r12#10
m13524=r13+r35+r25+r24+r14#11
m13542=r13+r35+r45+r24+r12#12
m14235=r14+r24+r23+r35+r15#13
m14253=r14+r24+r25+r35+r13#14
m14325=r14+r34+r23+r25+r15#15
m14352=r14+r34+r35+r25+r12#16
m14523=r14+r45+r25+r23+r13#17
m14532=r14+r45+r35+r23+r12#18
m15234=r15+r25+r23+r34+r14#19
m15243=r15+r25+r24+r34+r13#20
m15324=r15+r35+r23+r24+r14#21
m15342=r15+r35+r34+r24+r12#22
m15423=r15+r45+r24+r23+r13#23
m15432=r15+r45+r34+r23+r12#24

marshrut_list=[m12345,m12354,m12435,m12453,m12534,m12543,m13245,m13254,m13425,m13452,m13524,m13542,m14235,m14253,m14325,m14352,m14523,m14532,m15234,m15243,m15324,m15342,m15423,m15432]
n=0
print()
print("Расстояния возможных маршрутов:")
list=[]
for p in marshrut_list:
    n+=1
    print(f"{n}) {p} км")
    if p==min(marshrut_list):
        list.append(n)

print()
print(f"Маршрут №{list} является оптимальным.")
print()
print("Оптимальный маршрут №4:")
print(f"{point_1} -> {point_2}[{r12}] -> {point_4}[{r12+r24}] -> {point_5}[{r12+r24+r45}] -> {point_3}[{r12+r24+r45+r35}] -> {point_1}[{r12+r24+r45+r35+r13}] = {marshrut_list[3]}")
print()
print("Оптимальный маршрут №12:")
print(f"{point_1} -> {point_3}[{r13}] -> {point_5}[{r13+r35}] -> {point_4}[{r13+r35+r45}] -> {point_2}[{r13+r35+r45+r24}] -> {point_1}[{r13+r35+r45+r24+r12}] = {marshrut_list[11]}")