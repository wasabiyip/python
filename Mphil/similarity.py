#!/usr/bin/env python
import math
 
ti="tfidf/"
profile="profile/"
paper = "paper/"
topic = "topic/"

similarity = "similarity/"

def dot(a,b):
	a_di={}
	b_di={}
	for var in range(0,len(a)):
		temp=a[var].split("\t")
		a_di[temp[0]]=temp[1]
		#print temp[1]
	for var in range(0,len(b)):
		temp =b[var].split("\t")
		b_di[temp[0]]=temp[1]
		#print temp[1]
	result=0.0
	for item in a_di.keys():
		if b_di.has_key(item)>0:
			#print item
			result+=float(a_di[item])*float(b_di[item])
	return result


def sq(a):
	return math.sqrt(a)

def cos(x,y):
	up=dot(x,y)
	#print "up=" +str(up)
	down=sq(dot(x,x)*dot(y,y))
	#print "down=" +str(down)
	#down=1
	return up/down


"""
r={}
t={}
r["1"]=3
r["2"]=5

t["1"]=5
t["4"]=5
result=0.0
for item in r.keys():
		if t.has_key(item)>0:
			print item
			result+=float(r[item])*float(t[item])
		print result
#fileopen topic{paper profile} readlines()


f= open("1")
line = f.readlines()
print dot(line,line)

print cos(line,line)
"""


PT=open(similarity+"PT",'w')
RT=open(similarity+"RT",'w')
for var in range(1,50):
	print "topic "+str(var)
	f_topic=open(ti+topic+str(var))
	topic_c=f_topic.readlines()
	for var in range (1,551):
		f_reviewer=open(ti+profile+str(var))	
		reviewer_c=f_reviewer.readlines()
		value=cos(topic_c,reviewer_c)
		RT.write(str(value)+"\t")	
		f_reviewer.close()
		print "reviewer "+str(var)
	RT.write("\n")			
		
	for var in range (1,497):
		f_paper = open(ti+paper+str(var))
		paper_c=f_paper.readlines()
		value=cos(topic_c,paper_c)
		PT.write(str(value)+"\t")
		f_paper.close()
		print "paper "+str(var)
	PT.write("\n")
	f_topic.close()
PT.close()
RT.close()



"""
f = open("1")
line_f = f.readlines()
ff = open("7")
line_ff = ff.readlines()

print cos(line_f,line_ff)
f.close()
ff.close()
"""
