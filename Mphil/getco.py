import urllib2
import sys
from urllib2 import Request, urlopen, URLError, HTTPError
HEADERS={'User-Agent' : 'Mozilla/5.0(X11; U; Linux i686; en-US; rv:1.9.2.13)'}
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
		text = response.readlines()
		return text



'''
f = open('reviewerlink.txt') 
#f = open('test')
ftable = open('coauthor.txt','w')#id name
fstat = open('coauthorstat.txt','w') # num co-author-num
ftotal = open('mergecoauthor.txt','w')# total people
'''
f_map=open('name_id')
dic={}
templine=[]
for line in f_map:
	templine=line[:-1].split("\t")
	dic[templine[0]]=templine[1]


f_map.close()

fname=open('distinct_coauthor.txt')
f = open('distinctlink') 
#f = open('test')
ftable = open('deltacoauthor.txt','w')#id name
fstat = open('deltacoauthorstat.txt','w') # num co-author-num
ftotal = open('deltamergecoauthor.txt','w')# total people
ID=1
linetemp=''
fmiss=open('miss','w')
for line in f:
	linetemp=fname.readline()[:-1]
	#print line
	#text=''
	text =get(line)
	#print text
        if text!=None:
		num=0
		ftable.write(dic[linetemp]+'\t')

		for line2 in text:
			#print line2
			if line2.find('<td class="coauthor"')>0:
				#print line2
				num+=1
				#print num
				temp =line2.split('.html">')
				mark=temp[1].find('</a>')
				ftable.write( temp[1][:mark]+'\t')
				ftotal.write(temp[1][:mark]+'\n')
		ftable.write('\n')
		print str(ID)+'\t'+str(num)
		fstat.write(str(ID)+'\t'+str(num)+'\n')
		
	else:
		fmiss.write(linetemp+"  line:"+str(ID)+"   ID:"+dic[linetemp])
	ID+=1
	


ftemp.close()
f.close()
ftable.close()
fstat.close()
ftotal.close()
#open file
#get link content
#get co-authors, get the coauthor number in stat
#merge the total coauthor
'''
		ftemp=open('temp','w')
		ftemp.write(text)
		ftemp.close()
		ftemp=open('temp','r')
		#	print text

'''		
