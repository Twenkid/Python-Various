# Activity templates
# Author: Todor

import sys
import string

for i in range(0, 101): print("0.5.",i)
for i in range(0, 61): print("0.2.",i)
for i in range(0, 61): print("0.3.",i)


L1 = ["#40A580", "#40B590", "#50C09A", "#57C6A6"];
L2 = ["Лягане", "Ставане", "Ядене",  "Напитка",  "Дъмбели", "Набиране", "Лицеви опори", "Бройки", "Разходка", "Бягане", "Колело", "Друго"]

T1 = "<button type=""button"" onclick=""fProcess(";
#T2 = 11, 12, 13 ...
T3 = ")"">";
#T4 = Ядене, Напитки, ... L2
T5 = "</button>"

i = 11
j = 0
for s1 in L1: s = T1 + str(i) + T3 + L2[j] + T5; print(s)


start = 783
step = 2194884.21875  
bins = 32

#for i in range(1, 35): print(start); start = start + step
for i in range(1, 35): print("=COUNTIF(D1:D2000; ", "\"<", str(start), "\")"); start = start + step

#for i in range(1, 32): print("start); start +=step