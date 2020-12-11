import sys
import string
# Generate Buttons for activity log
# Author: Todor Arnaudov
# 29-3-2015

L1 = ["#40A580", "#40B590", "#50C09A", "#57C6A6", "#64CAAF", "#70D5B0", "#79DAB9", "#80E6C0", "#88EAC6", "#96F0D4", "#806040", "#8F7465", "#9F8078", "#A07065", "#A6408A"];
L2 = ["Лягане", "Ставане", "Ядене",  "Напитка",  "Дъмбели", "Набиране", "Лицеви опори", "Бройки", "Разходка", "Бягане", "Колело", "Друго"]

#T1 = "<button type=""button"" onclick=""fProcess(";
T1 = "<button type=\"button\""
#T1_4 = "onclick=\"fProcess("
T1_4 = "onclick=fProcess("  #no quote " before and after!
T1_1 = "style=\"background-color: "
#T1_2 = color...
T1_3 = "\" ";
T1_1_1 = "font-size: ";


#T2 = 11, 12, 13 ...
#T3 = ")\">";
T3 = ")>";
#T4 = Ядене, Напитки, ... L2
T5 = "</button>"
#T6 = 

size = "17px";
i = 11
j = 0
for s1 in L2: #s = T1 + T1_1 + L1[j] + T1_3 + T1_4 + str(i) + T3 + L2[j] + T5; print(s); i=i+1; j=j+1;
              s = T1 + T1_1 + L1[j] + "; " + T1_1_1 + size + T1_3 + T1_4 + str(i) + "," + "\"" + L2[j] + "\"" + T3 + L2[j] + T5; print(s); i=i+1; j=j+1;
			  
