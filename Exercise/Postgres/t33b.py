import psycopg2
import sys
import os
# Author: Todor Arnaudov, 28.3.2015. Postgres database used for logging. Select, Insert ...  
#install... ?Т psycopg2 windows ... install ... http://www.stickpeople.com/projects/python/win-psycopg/
#postgre ...

def main():
	conn = None
	try:     
		conn = psycopg2.connect(database='twenkid_config', user='postgres', password='******') 
		cur = conn.cursor()
		cur.execute('SELECT version()')          
		ver = cur.fetchone()
		print(ver)

		cur = conn.cursor()
	
		#cur.execute("SELECT * from loggeraa") # id, name, address, salary  from COMPANY")
		
		s = "python"
		#cur.execute("INSERT INTO logger 'sfsdsdfdsfd'")#(\"" + s + "\")"
		cur.execute("INSERT INTO mouse VALUES(NOW(), 146, 2356)")
		#cur.execute("INSERT INTO logger VALUES(NOW(), 'Python', 't33.py', 1, 23, 46, 94, 'Good', 'White', 'Far', 563423)")
		cur.execute("INSERT INTO logger VALUES(NOW(), 'Абвгдежзийклмнодсф осдфксо косд ф', 't33.py', 1, 23, 46, 94, 'Good', 'Гъз', 'Far', 563423)")
		cur.execute("INSERT INTO logger VALUES(NOW(), 'HAHAHAHA', 't33.py', 4, 23, 46, 94, 'Good', 'White', 'Far', 563423)")

		#cur.execute("SELECT * from logger where time > '2015-01-24 14:56:59'")   #OK

		# id, name, address, salary  from COMPANY")
		
		
		#cur.execute("SELECT * from logger where time > '2014-1-29 14:56:59' AND time < '2014-03-01'")   #OK
		
		cur.execute("SELECT * from logger where time > '2015-1-1 14:56:59' AND time < '2016-03-01'")   #OK
		
		# id, name, address, salary  from COMPANY")
		#rows = cur.fetchall()
		rows = cur.fetchmany(1000)
		
		#for row in rows:		
		#	print( "ID = ", row[0])
		#	print ("NAME = ", row[1])
		#	print ("ADDRESS = ", row[2])
		#	print( "SALARY = ", row[3], "\n")
		s1 = str()
		for row in rows: 
						s1 = row[0]
						s2 = row[1]
						s3 = row[2]# + row[2] + row[3]#.__repr__#toappend('\t')# + row[1] + "\t" + row[2] + "\t" + row[3];
						print(s1, '\t', s2, '\t', s3)
		
						
		print("Operation done successfully")
		print(cur.rowcount);
		s = dir(cur)
		s = s + dir(conn);
		print(s);
		print()
		print(dir(rows))
		
		print("Script Info:")
		#print(sys.argv[0], sys.argv[1])
		print(sys.argv)
		print(os.getcwd())
		print(os.path.dirname(os.path.realpath(__file__)))
		print(os.listdir(os.path.dirname(os.path.realpath(__file__))))
		
	except (psycopg2.DatabaseError):
			tb= sys.exc_info()
			print('Error %s', psycopg2.DatabaseError); print(tb); 
			#send somewhere - Гъвче ... Обща памет...
    #sys.exit(1)

	finally: conn.commit() 
	if conn:	 conn.close()

	
	conn.close()


#except psycopg2.DatabaseError, e:
#    print 'Error %s' % e    
#    sys.exit(1)
    
    
	
		
if __name__ == '__main__':
    main()
