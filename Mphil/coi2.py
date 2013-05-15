f= open("source1.TXT")
fcon=open("COI2","w")
temp=""

dic={}
dic_use={}

for line in f.readlines():
	temp=line.split("\t")
	dic_use[temp[0]]=temp[1:]
#temp[0] id
	#print temp[0]
	for i in range(0,12):
		if (temp[i*5+1]==""):
			continue
		else:
			if(dic.has_key(temp[i*5+1])):
				a=dic[temp[i*5+1]]
				a.append(temp[0])
				a.append(i)
			else:
				a=[temp[0],i]
				dic[temp[i*5+1]]=a

# temp [i*5+1:i*5+6]
#print dic_use
#print dic
for key in dic.iterkeys():	
	a=dic[key]
	l=0
#	print a
	Id=[]
	start=[]
	grad=[]
    	for i in range(0,len(a)/2):
		ID=a[l]
		Id.append(ID)
		pos=a[l+1]
#		print ID,pos,"#"
#		print ID,dic_use[ID]
		b=dic_use[ID]
		time = b[pos*5+1:pos*5+5] 
		#print i
#start
		if(len(b[pos*5+2])==1):
			year=int(b[pos*5+1])*100+int(b[pos*5+2])
			start.append(year)
			#print start[i]
		elif(len(b[pos*5+2])==0 and len(b[pos*5+1])>1):
			year=int(b[pos*5+1])*100
			start.append(year)
			#print start[i]
		elif(len(b[pos*5+2])==2):
			year=int(b[pos*5+1])*100+int(b[pos*5+2])
			start.append(year)
			#print start[i]
		else:
			year=0
			start.append(year)
#graduate
		if(len(b[pos*5+4])==1 and b[pos*5+4]!="\n"):
			year=int(b[pos*5+3])*100+int(b[pos*5+4])	
			grad.append(year)
		elif(len(b[pos*5+4])==0 and len(b[pos*5+3])>1):
			year=int(b[pos*5+3])*100
			grad.append(year)
		elif(len(b[pos*5+4])=="\n" and len(b[pos*5+3])>1):
			year=int(b[pos*5+3])*100
			grad.append(year)
		elif(len(b[pos*5+4])==2):
			year=int(b[pos*5+3])*100+int(b[pos*5+4])
			grad.append(year)
		else:
			year=0
			grad.append(year)

		l+=2
		k=0
#	print start
#	print grad
#	print Id
	for t in range(0,len(Id)):
		for tt in range(t,len(Id)):
			if (start[t]<=grad[tt] and grad[t]>=start[tt]):
				if (Id[t]!=Id[tt]and start[t]!=0):
					fcon.write(Id[t]+"\t"+Id[tt]+"\n")
					print Id[t]+"\t"+Id[tt]+"\t"+str(start[t])+"\t"+str(grad[t])+"\t\t"+str(start[tt])+"\t"+str(grad[tt])


	#run an comparation
	


f.close()
fcon.close()
