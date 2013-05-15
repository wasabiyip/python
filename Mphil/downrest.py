#! /urs/bin/python
from urllib2 import Request, urlopen, URLError, HTTPError
import urllib2

HEADERS={'User-Agent' : 'Mozilla/5.0(X11; U; Linux i686; en-US; rv:1.9.2.13)'}

def coauthor(url,fileok,filenone,name):
	request = urllib2.Request(url,headers=HEADERS)
	
	
	try:
		response = urllib2.urlopen(request)
	except HTTPError, e:
		filenone.write(name) 
	    	#print 'Error code: ', e.code
	except URLError, e:
	    	filenone.write(name) 
	    	#print 'Reason: ', e.reason
	else:
		text = response.read()
		fileok.write(name)
	    # everything is fine
	
	if 0:
		if response == "404: ('Not Found', 'Nothing matches the given URI')":
			print "404: ('Not Found', 'Nothing matches the given URI')"
		else:
			text = response.read()
			print text


f = open('restlink')
#f=open('test')
fok = open('validate','w')
fnon = open('cannotfind','w')
fname= open('rest')
num=1
for line in f:
	#line=f.readline()
	#print line
	name = fname.readline()
	text = coauthor(line,fok,fnon,name)
	print str(num)+'\t'
	num+=1
	if 0:
		if text == '1':
			fnon.write(line)
		else:
			fok.write(line)

f.close()
fok.close()
fnon.close()
fname.close()
fnon.close()
