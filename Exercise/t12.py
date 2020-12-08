# Generation of a HTML table with number index links within the document 1, 2, 3, 4, 5, ...
# Author: Todor Arnaudov - http://twenkid.com
# For the book "Какво му трябва на човек..."?
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
	
def numbersB(w, x,y):
  print(r"<table width=" + str(w) + " border=1>")
  c = 0
  for y1 in range(y):
    print("<tr>")
    for x1 in range(x):    
      print("<td>") # width=30>")
      print(r"""<center><span style="font-size: 130%; color: black">"""+str(c)+"</span></center><br><br>\n\n\n") #<b></b>
      print("</td>")
      c+=1
  print("</tr>")
  print(r"</table>")

numbersB(900, 20, 31)
  
print(r"""</body></html>""")
