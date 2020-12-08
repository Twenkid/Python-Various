# Zrim, Зрим, ... (друго име трябва...)
# Explanation of walking directories and file with the Todor's cognitive notation "Zrim" (Зрим)
# Author: Todor Arnaudov - Тодор Арнаудов - Тош, Разумир, Razumir, Twenkid, Tosh... 22-3-2016
# t9_zrim1.py

def walkExample(path):		#  @  \|/ ({K}!({пП}) ... -*- обПмт.&[1] ...  (,нч)   ... 
	import os				#  @  -*-{К-К}("os") 
	for root, dirs, files in os.walk(path, topdown=False):
	# Обх.свеждане.{бр[.].вт=3(&[.]1 = "root", &[.]2 = "dirs", &[.]3="files"; &[.].вн = (!="os.walk", !.#=(&[.]1 = "path" = ОбПмт.&[1], &[.]2 = "topdown=False".свеждане)) (,нч)
	# &[.]1 = "root" -*- пмт.&[1], ...
	
	for name in files:		# (Обх.свеждане.{бр[.].вт=1(&[.]1 = "name"; &[.].вн = "files" (,нч)
			s = os.path.join(root, name);	#	пмт.&[1] = "s"; *пмт.&[1] = @{K}!(&! = "os.path.join", &!.# = "root" (?Т ...) ...
			print(s.encode(encoding='utf-8'))	# @{K}!(&!="print",  &!.# = ("s.encode(encoding='utf-u'))")   //unfold etc. ... recursive ... 
		for name in dirs:		#
			j = os.path.join(root, name)	#
			print(j.encode(encoding='utf-8'))	#
			
