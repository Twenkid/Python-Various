#t13.py
#NLTK 3.0, Python 2.7, R:\Python27\  S:\code\python\
#4-6-2014

import nltk
from timeit import Timer

words = 'I turned off the spectroroute'.split()
words.sort(cmp)

words.sort(lambda x, y: cmp(len(y), len(x)))
s = [pair[1] for pair in sorted((len(w), w) for w in words)[::-1]]
print(s)

#s = 
t = Timer("sorted(words, lambda x, y: cmp(len(y), len(x)))").timeit()
#print(str(s))

print(dir(t))
#print 
#print(str((s)))

#s1 = 
t1 = Timer("[pair[1] for pair in sorted((len(w), w) for w in words)]").timeit()
#print(dir(t1))
#print(str(s1))

#C:\Users\tosh>r:
#R:\>cd python27
#R:\Python27>python s:\code\Python\t13.py
#['spectroroute', 'turned', 'the', 'off', 'I']
#Traceback (most recent call last):
# File "s:\code\Python\t13.py", line 12, in <module>
#    t = Timer("sorted(words, lambda x, y: cmp(len(y), len(x)))").timeit()
#  File "R:\Python27\lib\timeit.py", line 193, in timeit
#    timing = self.inner(it, self.timer)
#  File "<timeit-src>", line 6, in inner
#NameError: global name 'words' is not defined
#
#R:\Python27>
#
#
# WHY "not defined"?  4-6-2014, 12:48

