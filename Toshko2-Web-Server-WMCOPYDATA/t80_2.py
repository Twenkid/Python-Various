#t80_2.py ... Python 2.7
#Web POST client
#Here is an example session that shows how to POST requests:
#2-4-2016
#OK, works! :)

import httplib, urllib

params = urllib.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = httplib.HTTPConnection("localhost:8079")
#conn = httplib.HTTPConnection("77.77.164.35:8079")

conn.request("POST", "", params, headers)
response = conn.getresponse()
print(response.status, response.reason)
#302 Found
data = response.read()
print(data)

import base64
decoded = base64.b64decode(data)
f = open("resp12345678.mp3", "wb")
f.write(decoded)
f.close()

#>>> data
#'Redirecting to <a href="http://bugs.python.org/issue12524">http://bugs.python.org/issue12524</a>'

conn.close()

