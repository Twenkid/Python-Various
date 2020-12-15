import psycopg2
import sys
import os
import codecs, locale
#Author: Todor Arnaudov, 5.2015

import codecs

def readsend(path):
	conn = None
	try:         
		conn = psycopg2.connect(database='twenkid_config', user='postgres', password='********') 
		cur = conn.cursor()
		cur.execute('SELECT version()')          
		ver = cur.fetchone()
		print(ver)

		cur = conn.cursor()		
		
		cur.execute("INSERT INTO acsh (title) VALUES('test')")
		conn.commit() 
		
		
	except (psycopg2.DatabaseError):		
			tb= sys.exc_info()
			print(tb)
			#fo.write(bytes(tb, encoding))
		

	finally: conn.close() #conn.commit() 
		 

		#cur.execute("INSERT INTO acsh VALUES(NOW(), 'Абвгдежзийклмнодсф осдфксо косд ф', 't33.py', 1, 23, 46, 94, 'Good', 'Гъз', 'Far', 563423)")
 
		
if __name__ == '__main__':
    readsend(" ") #sys.argv[1])
    #main()
