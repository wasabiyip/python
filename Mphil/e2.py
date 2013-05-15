#generate first link for eacy topic
#get total number and how many page 
#generate all the links
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




def getnumber (name,number):
	tt=[]
	tt1=[]
	for l in range(0,len(name)):
		print name[l]
		test=get(name[l]+"0")
		tt=test.split("</b> of <b>");
		tt1=tt[1].split("</b> experts for")
		#print tt1[0],l
		number.append(tt1[0])
"""
open the link 
get the number
put in number []
"""



f= open("topic_arnet")
i=0
temp=[]#topic

temp1=[]



#1.generate link for eacy topic
for line in f.readlines():
	"""
	if i==32:
		temp1 = line[:-1].split("\t")
		temp.append(head+temp1[0]+tail)	
		temp.append(head+temp1[1]+tail)
		i+=2
	#print head+line[:-1]+tail
	
	else:
	"""
	temp.append(head+line[:-1]+tail)	
	i+=1


#2.get number
number=[]#numbers
getnumber(temp,number)

#print number
fnu=open("expertlink/topic-number","w")
for l in range(len(number)):
	fnu.write(str(l+1)+" "+number[l]+"\n")
fnu.close()
#3.generate link
"""
generate link file 
loop1 for all element in number [] 
	loop2 generate a number and write in 
"""
for l in range(len(number)):
	flink=open("expertlink/"+str(l+1),"w")
	#calculate page
	page=0
	if int(number[l])<15:
		page=1
		flink.write(temp[l]+"0"+"\n")
	else:
		page=int(number[l])/15
		for k in range(page):
			flink.write(temp[l]+str(k*15)+"\n")
		if int(number[l])-page*15 >0:	
			flink.write(temp[l]+str(page*15)+"\n")


	flink.close()
f.close()
