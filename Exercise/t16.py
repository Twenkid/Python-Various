#t16.py
#nltk matplotlib
#python 2.7+

import nltk, matplotlib

def vocab_growth(text):
     vocabulary = set()
     for text in texts:
         for word in text:
             vocabulary.add(word)
             yield len(vocabulary)

			 
#def speeches():
#    presidents = []
#     texts = nltk.defaultdict(list)
     ##sen = nltk.corpus.state_union.sents()
     ##for speech in nltk.corpus.state_union.sents():
     ##for speechlist in sen:nltk.corpus.state_union.words()
#     for speech in nltk.corpus.state_union.words():
         ##print(speechlist)
#		 print(speech)
		 ##for s in speechlist: speech.append		 
#        president = speech.split('-')[1]
#         if president not in texts:
#             presidents.append(president)
#         texts[president].append(nltk.corpus.state_union.words(speech))
#     return [(president, texts[president]) for president in presidents]
	 
import matplotlib
 
def president():
   for president, texts in speeches()[-7:]:
      growth = list(vocab_growth(texts))[:10000]
      matplotlib.plot(growth, label=president, linewidth=2)
      matplotlib.title('Vocabulary Growth in State-of-the-Union Addresses')
      matplotlib.legend(loc='lower right')
      matplotlib.show()
	 	 
#president()

def drawtest():
  g = list(range(0, 100))
  #print(dir(matplotlib))
  s = dir(matplotlib)
  for s1 in s: print(s1)
  #matplotlib.plot(g, label="pre", linewidth=2)
  #matplotlib.title('Vocabulary Growth in State-of-the-Union Addresses')
  #matplotlib.legend(loc='lower right')
  #matplotlib.show()
  
drawtest()