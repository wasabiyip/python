import sys
from string import atof
#f_map_others=open('numberresult.txt')
f_map_=open('numberresult.txt')
dic_={}
templine_=[]
for line_ in f_map_:
	templine_=line_[:-1].split("\t")
	dic_[templine_[0]]=set(templine_[1:-1])
#	print dic_[templine_[0]]
f_map_.close()



f_result=open(sys.argv[1],'w')

f_map_550=open('coauthor_num.txt')
dic={}
templine=[]
for line in f_map_550:
	templine=line[:-1].split("\t")
	dic[templine[0]]=set(templine[1:-1])
#	print dic[templine[0]]
#	for ii in range(0,len(templine)-2):
#		dic[templine[0]].intersection()
	f_result.write(templine[0]+"\t")
	for i in dic[templine[0]]:
		a=[]
		if i!= 'null':
			a=dic[templine[0]].intersection(dic_[i])
			f_result.write( str(len(a))+"\t")
	f_result.write("\n")
			
#		else:	
f_map_550.close()
f_result.close()

f=open(sys.argv[1])#statcom
f2=open(sys.argv[2],'w')#resulttemp
f3=open('finaldelta','w')
delta=0
for l in f.readlines():
	templ_=[]
	templ_=l[:-1].split("\t")
	f2.write(templ_[0]+"\t")
	f3.write(templ_[0]+"\t")
	a=0
	for i in range(1,len(templ_)-1):
		a += atof(templ_[i]) 
	f2.write(str(a)+"\n")
	temp=a/(len(templ_)-1)
	f3.write(str(temp )+"\n")
	delta+=temp
#	print delta,temp
f3.write("average is "+str(delta/550))
f.close()
f2.close()
f3.close()
