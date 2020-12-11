#t20.py
#14-7-2014: NLTK, ngrams

import nltk
import nltk.collocations

bigrams = nltk.collocations.BigramAssocMeasures()

path = r"R:\onthefourfoldroot_principle_sufficient_reason-schopenhauer-philosophy-filosofia-9-6-2014.txt"

#finder = nltk.collocations.BigramCollocationFinder.from_words(open(r"R:\ngramtool-20040527-mingw32-static\ada2008text.txt").read().split())

finder = nltk.collocations.BigramCollocationFinder.from_words(open(path).read().split())

#r"R:\onthefourfoldroot_principle_sufficient_reason-schopenhauer-philosophy-filosofia-9-6-2014.txt"

out = finder.nbest(bigrams.pmi, 10)

#str.decode('utf-8')  #etc.

print(out)


#Template libraries, string.template, ... Mako, Cheetah, Zope Page; Option Parser ... from optparse import OptionParser -- standard library -- use! ...
#Indexing: Nuclear, ... Full Text Indexing/Search