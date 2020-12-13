#t36.py
#5-5-2015, 0:14
#Author: Todor Arnaudov

import zipfile

s = []

s.append("E:\Canon\event-1.zip")
s.append("E:\Canon\event-2.zip")
s.append("E:\Canon\event-3.zip")
s.append("E:\Canon\event-4.zip")
s.append("E:\Canon\event-5.zip")
s.append("E:\Canon\event-6.zip")
s.append("E:\Canon\event-7.zip")
s.append("E:\Canon\event-8.zip")
s.append("E:\Canon\event-9.zip")
s.append("E:\Canon\event-10.zip")

s.clear()

s.append("S:\AssistantData\Events\event-15.zip")
s.append("S:\AssistantData\Events\event-14.zip")
s.append("S:\AssistantData\Events\event-13.zip")
s.append("S:\AssistantData\Events\event-12.zip")
s.append("S:\AssistantData\Events\event-11.zip")

for j in s: print(j)

#for j in s: z = zipfile.ZipFile(j); v1 = z.printdir(); print(v1);

v2 = " "

#for j in s: z = zipfile.ZipFile(j); v1 = z.printdir(); v2 = v2 + v1;

#ZipFile.infolist()
##Return a list containing a ZipInfo object for each member of the archive. The #objects are in the same order as their entries in the actual ZIP file on disk if #an existing archive was opened.

# for j in s: z = zipfile.ZipFile(j); v1 = z.infolist(); v2 = v2 + v1; #later ... v1[0] ... file_size ... 

line = '--------------------------------------------------';
line = line + line;
print(line)
for j in s: print(j); z = zipfile.ZipFile(j); z.printdir();

#f1 = open("listEvents.txt", "w+")
#f1.write(v2)
#f1.close()



