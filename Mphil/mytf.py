#!/usr/bin/env python

import math
import tfidf
import unittest

paper="paper/"
profile="profile/"
topic="topic/"
#after="after/"
after="tfidf_remove_stop_words/after/"

tfidf_="tfidf/"
DEFAULT_IDF_UNITTEST = 1.0

my_tfidf_PT = tfidf.TfIdf(DEFAULT_IDF = DEFAULT_IDF_UNITTEST)
#my_tfidf_RT = tfidf.TfIdf(DEFAULT_IDF = DEFAULT_IDF_UNITTEST)
"""
f= open("test1")
for line1 in f:
	line1 +=f.readline()
my_tfidf.add_input_document(line1)
f.close()

f= open("test2")
for line1 in f:
	line1 +=f.readline()
my_tfidf.add_input_document(line1)
f.close()

f= open("test3")
for line1 in f:
	line1 +=f.readline()
my_tfidf.add_input_document(line1)
f.close()

f= open("test4")
for line1 in f:
	line1 +=f.readline()
my_tfidf.add_input_document(line1)
f.close()
"""
line=""



 
for var in range(1,50):
	f=open (after+topic+str(var))
	for line in f:
		line+=f.readline()
	my_tfidf_PT.add_input_document(line)
#	my_tfidf_RT.add_input_document(line)
	f.close()


for var in range(1,551):#profile RT
	f=open(after+profile+str(var))
	for line in f:
		line+=f.readline()
	my_tfidf_PT.add_input_document(line)
	f.close()

for var in range(1,497):#paper PT
	f=open(after+paper+str(var))
	for line in f:
		line+=f.readline()
	my_tfidf_PT.add_input_document(line)
	f.close()


###


for var in range(1,50):
	f=open (after+topic+str(var))
	fw_p=open(tfidf_+"topic/"+str(var),'w')
	#fw_r=open(tfidf_+"RT/topic_R/"+str(var),'w')
	for line in f:
		line+=f.readline()
	a=my_tfidf_PT.get_doc_keywords(line)
	for i in range(0,len(a)):
		fw_p.write(str(a[i][0])+"\t")
		fw_p.write(str(a[i][1])+"\n")
	print "topic"+str(var)	
	fw_p.close()
	#fw_r.close()
	f.close()
"""	for i in range(0,len(my_tfidf_PT.get_doc_keywords(line))):	
		fw_p.write(my_tfidf_PT.get_doc_keywords(line)[i][0]+"\t")
		fw_p.write(str(my_tfidf_PT.get_doc_keywords(line)[i][1])+"\n")
"""
	

for var in range(1,551):#profile RT
	f=open(after+profile+str(var))
	fw_p=open(tfidf_+"profile/"+str(var),'w')
	for line in f:
		line+=f.readline()
	a=my_tfidf_PT.get_doc_keywords(line)
	for i in range(0,len(a)):
		fw_p.write(str(a[i][0])+"\t")
		fw_p.write(str(a[i][1])+"\n")
	print "profile"+str(var)
	fw_p.close()
	f.close()
	
"""	
for i in range(0,len(my_tfidf_RT.get_doc_keywords(line))):	
		fw_r.write(my_tfidf_RT.get_doc_keywords(line)[i][0]+"\t")
		fw_r.write(str(my_tfidf_RT.get_doc_keywords(line)[i][1])+"\n")
"""
	
for var in range(1,497):#paper PT
	f=open(after+paper+str(var))
	fw_p=open(tfidf_+"paper/"+str(var),'w')
	for line in f:
		line+=f.readline()
	a=my_tfidf_PT.get_doc_keywords(line)
	for i in range(0,len(a)):
		fw_p.write(str(a[i][0])+"\t")
		fw_p.write(str(a[i][1])+"\n")	
	print "paper"+str(var)
	fw_p.close()
	f.close()

"""
	for i in range(0,len(my_tfidf_PT.get_doc_keywords(line))):
		fw_p.write(my_tfidf_PT.get_doc_keywords(line)[i][0]+"\t")
		fw_p.write(str(my_tfidf_PT.get_doc_keywords(line)[i][1])+"\n")
"""





 
#a=my_tfidf.get_doc_keywords(line1)
#print a[0]
#print my_tfidf.get_doc_keywords("1")

