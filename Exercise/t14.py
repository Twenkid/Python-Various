#t14.py
#nltk
#4-6-2014

import nltk

nltk.download("words")
words = nltk.corpus.words.words('en')
wordlist = set(words)
rev_wordlist = set(word[::-1] for word in words)

def bad():
	for word1 in words:
		for word2 in words:
			if word1 == word2[::-1]:
				print(word1)
			 
def effic():
  s = sorted(wordlist.intersection(rev_wordlist))
  return s

bad()  
s1 = effic()
print(s1)
  
