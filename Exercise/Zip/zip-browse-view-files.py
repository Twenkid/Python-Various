import zipfile
import os  #if os.mkdir, os.rm.
"""
24-10-2022
By Twenkid
For browsing images etc. packed in a zipfile
Without unpacking all
"""
path = "z:\\aitextures12.zip"
z = zipfile.ZipFile(path)

"""
z.printdir()
dir(zipfile)
dir(z)
['NameToInfo', '_RealGetContents', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_allowZip64', '_comment', '_didModify', '_extract_member', '_filePassed', '_fileRefCnt', '_fpclose', '_lock', '_open_to_write', '_sanitize_windows_name', '_seekable', '_strict_timestamps', '_windows_illegal_name_trans_table', '_write_end_record', '_writecheck', '_writing', 'close', 'comment', 'compression', 'compresslevel', 'debug', 'extract', 'extractall', 'filelist', 'filename', 'fp', 'getinfo', 'infolist', 'mode', 'namelist', 'open', 'printdir', 'pwd', 'read', 'setpassword', 'start_dir', 'testzip', 'write', 'writestr']
z.filelist
z.extract
"""

print(z.filelist)

"""
[<ZipInfo filename='aitextures12/' filemode='drwxr-xr-x' external_attr=0x10>, <ZipInfo filename='aitextures12/leafy_carved_feathered_decorative_tx_614_3.jpg' ...
"""

print(help(z.extract))

"""
>>> help(z.extract)
Help on method extract in module zipfile:

extract(member, path=None, pwd=None) method of zipfile.ZipFile instance
    Extract a member from the archive to the current working directory,
    using its full name. Its file information is extracted as accurately
    as possible. `member' may be a filename or a ZipInfo object. You can
    specify a different directory using `path'.
"""
cache =  "z:\\temp\\"
import os
os.mkdir(cache) #"z:\\temp")
z.extract(info[1], cache)

import pathlib
print(pathlib.Path(info[1].filename))
# aitextures12\leafy_carved_feathered_decorative_tx_614_3.jpg
# Do whatever ... Open it with cv2... to show it etc. Adjust for Linux etc.

import cv2
i = cv2.imread(cache+info[1].filename)
cv2.imshow("IMAGE", i)
cv2.waitKey(0)

#Store in a circular list for cache and delete the oldest etc., input cycle etc.
