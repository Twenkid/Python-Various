import psycopg2
import sys
import os
import codecs, locale
import re
#ACS parser to Postgres DB...
#Author: Todor Arnaudov, 5.2015


def init():
  global razdelitel;
  razdelitel = []
  razdelitel.append("\t");
  razdelitel.append(" ");
  razdelitel.append(":")
  
  
def sys1(path):
		list1 = []
		f = codecs.open(path, "r") # "utf-8")
		list1 = f.readlines()
		f.close()
		
		i = 0	
		for item in list1:
		   list2 = item.split(razdelitel[2])
		   #recursive...
		   #list3 = list3.split(razdelitel[1])
		   print(list2[0])
		   
		   
		  
if __name__ == '__main__':
  init()
  sys1(sys.argv[1])
		