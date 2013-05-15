#get all name
#save in corresponding file

#expertlink
#expertname

import urllib2
from urllib2 import Request, urlopen, URLError, HTTPError
HEADERS={'User-Agent' : 'Mozilla/5.0(X11; U; Linux i686; en-US; rv:1.9.2.13)'}
head="http://www.arnetminer.org/expertfinding.do?keyword="
tail="&searchRange=0&searchAlgorithm=1&start="#0"

def get(url):
	#handle exception
	request = urllib2.Request(url,headers=HEADERS)
	try:
		response = urllib2.urlopen(request)
	except HTTPError, e:
		print 'The server couldn\'t fulfill the request.'
	    	print 'Error code: ', e.code
	except URLError, e:
	    	print 'We failed to reach a server.'
	    	print 'Reason: ', e.reason
	else:
		text = response.read()
		return text


temp=[]
tempin=[]
tempmore=[]
tempt=[]




#number write in a file
for i in range(1,52):
	fname =open ("expertname/"+str(i),"w")
	flink =open ("expertlink/"+str(i))
	print i
	for line in flink.readlines():
		test=get( line[:-1])
		temp=test.split('<a href="/viewperson.do?naid')
		for much in range(len(temp)):
			if much%2==1:
				tempin=temp[much].split('">')
				tempmore = tempin[1].split("</a>")[0]
				fname.write(tempmore+"\n")
				if temp[much].count("ALIAS:")>0:
					tempt=temp[much].split("(ALIAS: ")[1].split(")")[0].split(", ")
					for many in range(len(tempt)):
						fname.write(tempt[many]+"\n")
	print i,"end"
	fname.close()
	flink.close()		
