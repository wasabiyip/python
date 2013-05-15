import sys

f_map=open('name_id')
dic={}
templine=[]
for line in f_map:
	templine=line[:-1].split("\t")
	dic[templine[0]]=templine[1]


f_map.close()

f_number=open(sys.argv[1],"w")

f_file=open('deltacoauthor.txt')
temparray=[]
for l in f_file.readlines():
	temparray=[]
	temparray=l[:-2].split("\t")	
	
	for i in range(0,len(temparray)):
		if i==0:
			f_number.write(temparray[i]+"\t")		
		else:
			print i
			if dic.has_key(temparray[i]):
				f_number.write(dic[temparray[i]]+"\t")
			else:
				print temparray[i]
	f_number.write("\n")

f_number.close()
f_file.close()
