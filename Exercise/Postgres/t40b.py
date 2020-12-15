import psycopg2
import sys
import os
import codecs, locale
import re
#ACS log parser to Postgres DB
#Author: Todor Arnaudov, 5.2015
#install... ?Т psycopg2 windows ... install ... http://www.stickpeople.com/projects/python/win-psycopg/
#postgre ...
#t38.py, Postgre, acsh, logs - send to DB, ... 12/5/2015, 13/5/2015, 14/5/2015 ...
#...
#python t38.py "..."

import codecs

def init():
	global pt;
	#pt = re.compile('\d+\.\d+\.')	
	pt = re.compile('\d+')

def content2(cont):
	lines = cont.splitlines()
	i = 0
	for s in lines:	
		print("##"+s+"##")
		found = pt.match(s);
		#if (found.start >=0): break;
		if (found): print('FFFFFFOUND!'); break;
		else: print('Not found')
		i=i+1
		
	#for s in lines:	
	#	print(s)
		#found = pt.match(s);
		  #res = re.search(s, page, re.MULTILINE)
		  #if (found.start >=0): break;
		#if (found): break;
		#else: print('Not found')
	#	i=i+1
		
			
	replaced = cont;
	if (i<len(lines)):
		print('Replace?')
		replaced = lines[i].replace('г.', ' ')
		replaced = replaced.replace('ч.', ' ')
		replaced = replaced.replace('.', '-')
		print(replaced)
	#else: replaced = cont;
	
	return replaced
	#Example: 8.5.2015 г. 16:16:11 ч.

	
	
def content(cont):
	lines = cont.splitlines()
	i = 0	
	found = None
	for s in lines:	
		print(s)
		found = pt.match(s);
		#if (found.start >=0): break;
		if (found): print('FFFFFFOUND!'); break;
		else: print('Not found')
		i=i+1
	else: i=-1
	
	replaced = cont;
		
	if ( (i<len(lines) and found)):
		print('Replace?')
		replaced = lines[i].replace('г.', ' ')
		replaced = replaced.replace('ч.', ' ')
		replaced = replaced.replace('.', '-')	
    
	return (i,replaced)
	
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
		
		list3 = []
		f = codecs.open(path, "r", "utf-8")
		list3 = f.readlines(5)
		f.close()
		delimiter = list3[0];
		#delimiter = list3[0].strip() #don't strip, include new line?
		extended = '#$#'
		
		list2 = []
		list2.append(delimiter)
		list2.append(extended)

		#{	hwnd, hwndChild, title, class	8309
		
		print("Delimiter =["+delimiter+"]")
		f = codecs.open(path, "r", "utf-8")	
		data1 = f.read() #all
		f.close()
		list4 = data1.split(delimiter) #"<#>")
		len4 = len(list4)
		print(str(len(list4) - 2) + "data items in " + path + os.sep + list2[0])
		print(len4)
		#print(list4[len4-1].encode(sys.stdout.encoding, 'replace'))
	    
		text = list4[len4-1]
		#text = list4[len4-1].replace('\u2013', '-')
		#print(text)
		#sys.stdout.encoding  = 'utf-8'
		#print(list4[len4-1])
		
		
		
		
		# sys.stdout = codecs.getwriter('utf8')(sys.stdout)  ?
		
		
		
		#sys.stderr = codecs.getwriter('utf8')(sys.stderr)
		#sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout); 
		#sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout); 

		#print("sys.stdout...?")
		#print(bytes(text,'utf-8').decode('utf-8'))
		#print(list4[len4-10])
		
		fo = open('acsh999.txt', 'wb') #'ab')
		encoding='utf-8'
		fo.write(bytes(text, encoding))
		

		list5 = text.split("\n")
		
		i = 0
		while(len(list5[0])==0): i+=1
		if (list5[i]==extended): i+=1
		if (list5[i][0]=='{'): i+=1
		len5 = len(list5) - 1;
		
		fo.write(bytes("####", encoding));
		try:
			while(len(list5[i])>0):	
									if list5[i][0]=='{': break
									i=i+1
									
			i=i+1
			j = 3
			while(i < len5):	
								if (list5[i][0]!='}'):
													#fo.write(i); # encoding);
													#fo.write(bytes(list5[i], encoding));
													list6 = list5[i].split('\t');
													if (len(list6) > -1):
																		#fo.write(bytes(list6[0], encoding));
																		fo.write(bytes(list6[0], encoding));
																		fo.write(bytes('\r\n', encoding))
																		
																		list7 = []
																		
																		
																		lines = content(list4[j])
																		if (len(lines)>0):
																			fo.write(bytes("LINES: " + list4[j], encoding))
																																				
																		
																		
																		list6[2] = list6[2].replace("\'","''") 
																		#list6[2].replace("\"","\"\"") 
																		#cur.execute("INSERT INTO acsh (title) VALUES('test')")
																		
																		
																		#OK: cur.execute("INSERT INTO acsh (hwnd, title) VALUES(" + "'" + list6[0] + "','" + list6[2] + "')");
																		
																		time = 'NOW()'
																		ln = 0
																		#if (j<len(list4)):
																		#print("LIST4["+list4[j]+"]")
																		(ln, time) = content(list4[j])
																		print("Line="+str(ln))
																		
																		if (ln==-1):
																			time = 'NOW()'#2015-5-1'#NOW()'
																		print(time)
																		
																		#cont = list4[j]
																		cont = ""
																		#if (ln>-1):
																		#	for k in range(ln, len(list4)): cont = cont + list4[k] + "\n"
																		#else: cont = list4[0]
																		
																		
																		cont = list4[j]
																		#print(list4[j])
																		fo.write(bytes("\n===========", encoding))
																		fo.write(bytes(list4[j], encoding))
																		
																		cont = cont.replace("\'","''")
																		cont = cont.strip()
																		#and still sends first line, time ...
																			
																		
																		cur.execute("INSERT INTO acsh (time, hwnd, hwndchild, title, content) VALUES("+ "'" + time + "'," + "'" + list6[0] + "','" + list6[1] +"','" + list6[2] + "'" + ",'" + cont+ "')");
																		
																		####cur.execute("INSERT INTO acsh (realtime, hwnd, title) VALUES("+ "'" + time + "'," + "'" + list6[0] + "','" + list6[2] + "')");
																		
																		j = j + 1
																		conn.commit()
								i=i+1;								
		except():
		
			#finally: fo.close
		
			fo.close()
		
		
			

		#i = 0
		#for s in list4: print(i, s); i=i+1;
		
		
		#).encode(sys.stdout.encoding, 'replace')
		
	except (psycopg2.DatabaseError):		
			tb= sys.exc_info()
			print(tb)
			#print(list
			#fo.write() #, encoding))
			#print(bytes(tb, encoding)))
			#print(tb)
			#print('Error %s', psycopg2.DatabaseError); print(tb); 
			#send somewhere - Гъвче ... Обща памет...
    #sys.exit(1)

	finally: conn.close() #conn.commit() 
		

		#cur.execute("INSERT INTO acsh VALUES(NOW(), 'Абвгдежзийклмнодсф осдфксо косд ф', 't33.py', 1, 23, 46, 94, 'Good', 'Гъз', 'Far', 563423)")
 
def main():
	conn = None
	try:     
		conn = psycopg2.connect(database='twenkid_config', user='postgres', password='********') 
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
   
#18-5-2015 ...    
def createTable(name):
   s = ["create table", "windowclass character varying(250)", "title character varying(250)"]
   #s.append("create table")
   #s.append(
   qu = s[0] + name + "("
   qu = qu + "id serial" + ","
   qu = qu + "time timestamp without timezone" + "," #default columns
   #qu = qu + ","
   
     
   #//Търси, ИЗС, Обх, стига до дъно ... връща се ...

#  sys1_state = 0  
  
#def sys1():
 # 	os.startfile("sys1.bat");
#	sys1_state = sys1_state+1
#	list1 = []
 #   list1 = f.readlines()
#	f.close()
		
if __name__ == '__main__':
	init()
	readsend(sys.argv[1])	
	#ct = content('\r\n\r\n10.5.2015 г. 22:34:33 ч.\r\n Past.Add(data);')
	#print(ct)
    #main()
