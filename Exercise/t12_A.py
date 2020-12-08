#Reports ... Notes, tables ... generation ... 3-6-2016
# Generation of a HTML table with number index links within the document 1, 2, 3, 4, 5, ...
# Author: Todor Arnaudov - http://twenkid.com
# See also the other t12_... files

print(r"""
<!DOCTYPE html><html><head>
<Meta Http-Equiv="Content-Type" content="text/html;windows-1251">
<Meta Name="Title" content=Бележки по номера"></head><br>
<body>
<div style="width: 1000px; font-size: 12px; font-family: Arial; color: blue">
""")
#charset=utf-8
def numbersA(n):
  for i in range(n):
    print(r"""<span style="font-size: 130%"><b>"""+str(i)+"</b></span><br><br>\n\n\n<hr>")
	
def numbersB(w,x,y,wc):
  print(r"<table width=" + str(w) + " border=1>")
  c = 0
  for y1 in range(y):
    print("<tr>")
    for x1 in range(x+1):    
      print("<td width=" + str(wc) +">")
      #print(r"""<center><span style="font-size: 130%; color: black">"""+str(c)+"</span></center><br><br>\n\n\n") #<b></b>
      print(r"""<center><span style="font-size: 130%; color: black">"""+r"""<a href="#""" +  str(c) + "\">" + str(c) + r"""</a>""""</span></center><br>\n\n\n") #<b></b>
      print("</td>")
      c+=1
  print("</tr>")
  print(r"</table>")
  
def articles(st,en):
  i=st
  while(i<en):  print("<br><br><p></p><b>" + str(i) + "</b>: " + r"""<a name=""" + "\"" + str(i) + "\"" + r"""</a>""" + r"""<p><br></br><br></br></p>""" + r"""<hr>"""+"\n\r"); i=i+1

def divA(w, style, size): print("<div style=" + "width: " + str(w) + "px;" + "font-style: " + style + ";" + "font-size: " + str(size) + "px;" + ">");

def divB(font): print("</div>")

numbersB(1580, 20, 31, 20)
divA(1500, "Consolas", 14)
articles(0,900)

  
print(r"""</body></html>""")
