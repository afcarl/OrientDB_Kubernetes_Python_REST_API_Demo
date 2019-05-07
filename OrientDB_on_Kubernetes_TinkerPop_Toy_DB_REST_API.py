# -*- coding: utf-8 -*-
"""
Created on Thu May  2 07:54:50 2019

@author: afcarl
"""

# importing the requests library 
import requests 
import json

'''
HTTP Status Codes
Registration Procedure(s)
IETF Review
Reference
[RFC7231]
Note
1xx: Informational - Request received, continuing process
2xx: Success - The action was successfully received, understood, and accepted
3xx: Redirection - Further action must be taken in order to complete the request
4xx: Client Error - The request contains bad syntax or cannot be fulfilled
5xx: Server Error - The server failed to fulfill an apparently valid request
    
Available Formats

CSV
Value 	Description 	Reference 
100	Continue	[RFC7231, Section 6.2.1]
101	Switching Protocols	[RFC7231, Section 6.2.2]
102	Processing	[RFC2518]
103	Early Hints	[RFC8297]
104-199	Unassigned	
200	OK	[RFC7231, Section 6.3.1]
201	Created	[RFC7231, Section 6.3.2]
202	Accepted	[RFC7231, Section 6.3.3]
203	Non-Authoritative Information	[RFC7231, Section 6.3.4]
204	No Content	[RFC7231, Section 6.3.5]
205	Reset Content	[RFC7231, Section 6.3.6]
206	Partial Content	[RFC7233, Section 4.1]
207	Multi-Status	[RFC4918]
208	Already Reported	[RFC5842]
209-225	Unassigned	
226	IM Used	[RFC3229]
227-299	Unassigned	
300	Multiple Choices	[RFC7231, Section 6.4.1]
301	Moved Permanently	[RFC7231, Section 6.4.2]
302	Found	[RFC7231, Section 6.4.3]
303	See Other	[RFC7231, Section 6.4.4]
304	Not Modified	[RFC7232, Section 4.1]
305	Use Proxy	[RFC7231, Section 6.4.5]
306	(Unused)	[RFC7231, Section 6.4.6]
307	Temporary Redirect	[RFC7231, Section 6.4.7]
308	Permanent Redirect	[RFC7538]
309-399	Unassigned	
400	Bad Request	[RFC7231, Section 6.5.1]
401	Unauthorized	[RFC7235, Section 3.1]
402	Payment Required	[RFC7231, Section 6.5.2]
403	Forbidden	[RFC7231, Section 6.5.3]
404	Not Found	[RFC7231, Section 6.5.4]
405	Method Not Allowed	[RFC7231, Section 6.5.5]
406	Not Acceptable	[RFC7231, Section 6.5.6]
407	Proxy Authentication Required	[RFC7235, Section 3.2]
408	Request Timeout	[RFC7231, Section 6.5.7]
409	Conflict	[RFC7231, Section 6.5.8]
410	Gone	[RFC7231, Section 6.5.9]
411	Length Required	[RFC7231, Section 6.5.10]
412	Precondition Failed	[RFC7232, Section 4.2][RFC8144, Section 3.2]
413	Payload Too Large	[RFC7231, Section 6.5.11]
414	URI Too Long	[RFC7231, Section 6.5.12]
415	Unsupported Media Type	[RFC7231, Section 6.5.13][RFC7694, Section 3]
416	Range Not Satisfiable	[RFC7233, Section 4.4]
417	Expectation Failed	[RFC7231, Section 6.5.14]
418-420	Unassigned	
421	Misdirected Request	[RFC7540, Section 9.1.2]
422	Unprocessable Entity	[RFC4918]
423	Locked	[RFC4918]
424	Failed Dependency	[RFC4918]
425	Too Early	[RFC8470]
426	Upgrade Required	[RFC7231, Section 6.5.15]
427	Unassigned	
428	Precondition Required	[RFC6585]
429	Too Many Requests	[RFC6585]
430	Unassigned	
431	Request Header Fields Too Large	[RFC6585]
432-450	Unassigned	
451	Unavailable For Legal Reasons	[RFC7725]
452-499	Unassigned	
500	Internal Server Error	[RFC7231, Section 6.6.1]
501	Not Implemented	[RFC7231, Section 6.6.2]
502	Bad Gateway	[RFC7231, Section 6.6.3]
503	Service Unavailable	[RFC7231, Section 6.6.4]
504	Gateway Timeout	[RFC7231, Section 6.6.5]
505	HTTP Version Not Supported	[RFC7231, Section 6.6.6]
506	Variant Also Negotiates	[RFC2295]
507	Insufficient Storage	[RFC4918]
508	Loop Detected	[RFC5842]
509	Unassigned	
510	Not Extended	[RFC2774]
511	Network Authentication Required	[RFC6585]
512-599	Unassigned	'''

username = 'root'
#password = 'root'
password = 'hello'


'''http://tinkerpop.apache.org/docs/current/tutorials/getting-started/'''

#URL_prefix = "http://localhost:2480/"
URL_prefix = "http://192.168.99.118:32480/"

# Disconnect from server
#URL = "http://localhost:2480/disconnect"
URL = URL_prefix + "disconnect"
resp = None
#resp = requests.get(URL, auth=('root', 'root'))
resp = requests.get(URL)
print(resp)
print(resp.json())


# Connect to server & database ""
#Create a new database.
#Syntax: http://<server>:[<port>]/database/<database>/<type>
#HTTP POST request: http://localhost:2480/database/demo/plocal
#URL = "http://localhost:2480/database/TinkerPopToyDB/plocal"
URL = URL_prefix + "database/TinkerPopToyDB/plocal"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())


# Create "person" node 
#URL = "http://localhost:2480/class/TinkerPopToyDB/sql/create person extends V"
#URL = "http://localhost:2480/command/TinkerPopToyDB/sql/create class person extends V"
URL = URL_prefix + "command/TinkerPopToyDB/sql/create class person extends V"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())


# Create "person" node w/ properties "name"
#URL = "http://localhost:2480/class/TinkerPopToyDB/sql/create person extends V"
#URL = "http://localhost:2480/command/TinkerPopToyDB/sql/create property person.name string"
URL = URL_prefix + "command/TinkerPopToyDB/sql/create property person.name string"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())


# Create "person" node w/ properties "age"
#URL = "http://localhost:2480/class/TinkerPopToyDB/sql/create person extends V"
#URL = "http://localhost:2480/command/TinkerPopToyDB/sql/create property person.age integer"
URL = URL_prefix + "command/TinkerPopToyDB/sql/create property person.age integer"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())


# Create "software" node 
#URL = "http://localhost:2480/command/TinkerPopToyDB/sql/create class software extends V"
URL = URL_prefix + "command/TinkerPopToyDB/sql/create class software extends V"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())


# Create "software" node w/ properties "name"
#URL = "http://localhost:2480/command/TinkerPopToyDB/sql/create property software.name string"
URL = URL_prefix + "command/TinkerPopToyDB/sql/create property software.name string"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())


# Create "software" node w/ properties "lang"
#URL = "http://localhost:2480/command/TinkerPopToyDB/sql/create property software.lang string"
URL = URL_prefix + "command/TinkerPopToyDB/sql/create property software.lang string"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())


# Create "knows" edge 
#URL = "http://localhost:2480/command/TinkerPopToyDB/sql/create class knows extends E"
URL = URL_prefix + "command/TinkerPopToyDB/sql/create class knows extends E"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())


# Create "knows" edge w/ properties "weight"
#URL = "http://localhost:2480/command/TinkerPopToyDB/sql/create property knows.weight decimal"
URL = URL_prefix + "command/TinkerPopToyDB/sql/create property knows.weight decimal"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())


# Create "created" edge 
#URL = "http://localhost:2480/command/TinkerPopToyDB/sql/create class created extends E"
URL = URL_prefix + "command/TinkerPopToyDB/sql/create class created extends E"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())


# Create "created" edge w/ properties "weight"
#URL = "http://localhost:2480/command/TinkerPopToyDB/sql/create property created.weight decimal"
URL = URL_prefix + "command/TinkerPopToyDB/sql/create property created.weight decimal"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())



# Create "person" node named "Marko" age = 29
#URL = "http://localhost:2480/command/TinkerPopToyDB/sql/create vertex person set name='Marko', age=29"
URL = URL_prefix + "command/TinkerPopToyDB/sql/create vertex person set name='Marko', age=29"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())


# Create "person" node named "Josh" age = 32
#URL = "http://localhost:2480/command/TinkerPopToyDB/sql/create vertex person set name='Josh', age=32"
URL = URL_prefix + "command/TinkerPopToyDB/sql/create vertex person set name='Josh', age=32"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())


# Create "person" node named "Peter" age = 35
#URL = "http://localhost:2480/command/TinkerPopToyDB/sql/create vertex person set name='Peter', age=35"
URL = URL_prefix + "command/TinkerPopToyDB/sql/create vertex person set name='Peter', age=35"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())


# Create "person" node named "Vadas" age = 27
#URL = "http://localhost:2480/command/TinkerPopToyDB/sql/create vertex person set name='Vadas', age=27"
URL = URL_prefix + "command/TinkerPopToyDB/sql/create vertex person set name='Vadas', age=27"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())


# Create "software" node named "lop" lang = java
#URL = "http://localhost:2480/command/TinkerPopToyDB/sql/create vertex software set name='lop', lang='java'"
URL = URL_prefix + "command/TinkerPopToyDB/sql/create vertex software set name='lop', lang='java'"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())


# Create "software" node named "ripple" lang = java
#URL = "http://localhost:2480/command/TinkerPopToyDB/sql/create vertex software set name='ripple', lang='java'"
URL = URL_prefix + "command/TinkerPopToyDB/sql/create vertex software set name='ripple', lang='java'"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())


# Create "knows" edge from Marko to Josh weight = 1.0
#URL = "http://localhost:2480/command/TinkerPopToyDB/sql/create edge knows from (select from person where name='Marko') to (select from person where name='Josh') set weight=1.0"
URL = URL_prefix + "command/TinkerPopToyDB/sql/create edge knows from (select from person where name='Marko') to (select from person where name='Josh') set weight=1.0"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())


# Create "knows" edge from Marko to Vadas weight = 0.5
#URL = "http://localhost:2480/command/TinkerPopToyDB/sql/create edge knows from (select from person where name='Marko') to (select from person where name='Vadas') set weight=0.5"
URL = URL_prefix + "command/TinkerPopToyDB/sql/create edge knows from (select from person where name='Marko') to (select from person where name='Vadas') set weight=0.5"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())


# Create "created" edge from Marko to lop weight = 0.4
#URL = "http://localhost:2480/command/TinkerPopToyDB/sql/create edge created from (select from person where name='Marko') to (select from software where name='lop') set weight=0.4"
URL = URL_prefix + "command/TinkerPopToyDB/sql/create edge created from (select from person where name='Marko') to (select from software where name='lop') set weight=0.4"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())


# Create "created" edge from Josh to lop weight = 0.4
#URL = "http://localhost:2480/command/TinkerPopToyDB/sql/create edge created from (select from person where name='Josh') to (select from software where name='lop') set weight=0.4"
URL = URL_prefix + "command/TinkerPopToyDB/sql/create edge created from (select from person where name='Josh') to (select from software where name='lop') set weight=0.4"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())


# Create "created" edge from Peter to lop weight = 0.2
#URL = "http://localhost:2480/command/TinkerPopToyDB/sql/create edge created from (select from person where name='Peter') to (select from software where name='lop') set weight=0.2"
URL = URL_prefix + "command/TinkerPopToyDB/sql/create edge created from (select from person where name='Peter') to (select from software where name='lop') set weight=0.2"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())


# Create "created" edge from Josh to ripple weight = 1.0
#URL = "http://localhost:2480/command/TinkerPopToyDB/sql/create edge created from (select from person where name='Josh') to (select from software where name='ripple') set weight=1.0"
URL = URL_prefix + "command/TinkerPopToyDB/sql/create edge created from (select from person where name='Josh') to (select from software where name='ripple') set weight=1.0"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())


# Create traversal from knows out of Marko
#URL = "http://localhost:2480/command/TinkerPopToyDB/sql/traverse out('knows') from (select from person where name='Marko')"
URL = URL_prefix + "command/TinkerPopToyDB/sql/traverse out('knows') from (select from person where name='Marko')"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())


# Create traversal from knows out of Marko to a depth of 3 & bredth-first strategy
#URL = "http://localhost:2480/command/TinkerPopToyDB/sql/traverse out('knows') from (select from person where name='Marko') maxdepth 3 strategy breadth_first"
URL = URL_prefix + "command/TinkerPopToyDB/sql/traverse out('knows') from (select from person where name='Marko') maxdepth 3 strategy breadth_first"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())


# Create traversal from knows out of Marko to a depth of 3 & bredth-first strategy skipping start node of Marko
#URL = "http://localhost:2480/command/TinkerPopToyDB/sql/select from (traverse out('knows') from (select from person where name='Marko') maxdepth 3 strategy breadth_first) where $depth >= 1"
URL = URL_prefix + "command/TinkerPopToyDB/sql/select from (traverse out('knows') from (select from person where name='Marko') maxdepth 3 strategy breadth_first) where $depth >= 1"
resp = None
resp = requests.post(URL, auth=(username, password))
print(resp)
print(resp.json())
todos = json.loads(resp.text)
print("todos = ",todos)












