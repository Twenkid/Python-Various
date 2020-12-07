#t6.py
# Code objects and code generation exercises
# Author: Todor Arnaudov, 28.5.2014 + 7.12.2020

x = 156
code = compile('a = 1 + 2', '<string>', 'exec')
exec(code)
print(a)


#code2 = compile('a = 1 + 2; print(globals()); print(gloabls()["x"]), '<string>', 'exec')
src = 'a = 1 + 2;' + "print(globals()" + "['x'])"
code2 = compile(src, '<string>', 'exec')
exec(code2)

def fin(inp):
	z = 35
	src = 'a = 565 + (23432*34)/inp;' + "print(a); print(locals()" + "['z'])"
	code3 = compile(src, '<string>', 'exec')
	exec(code3)
	
fin(5667)
fin(1234)

#28-5-2014, 15:28

#test functions, quick, generate code...

import os
import os.path

def callitA(mod, func, param, quote):
    if quote:
      exec(mod + "." + func + '(' + "'" + param + "'" + ')')
    else:
      exec(mod + "." + func + '(' + param + ')')

def callit(mod, func, param, quote):
    if quote:
      exec(mod + func + '(' + "'" + param + "'" + ')', globals(), locals())
    else:
      exec(mod + func + '(' + param + ')', globals(), locals())
    exec("xxx = xxx*2", globals(), locals()) #not changed

ssm = ['os.', 'os.', 'os.', '']
ssa = ['getcwd', 'listdir', 'system', 'str']
ssb = [' ', 'D:\\code', 'pause', 'xxx']
ssq = [False, True, True, False]

xxx = 999888
#for s in ssa: callit(s)
for m, f, p, q in zip(ssm, ssa, ssb, ssq): callit(m, f, p, q)
print(xxx)

#ssm = ['os', 'os', 'os', ' ']
#ssb = ['.', 'D:\\code', 'pause', 'xxx']