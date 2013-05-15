import sys
#f_o=open("name_id")
f_t=open("reviewers.txt")

o=""
dic={}
temp1=""
temp2=""
for b in f_t.readlines():
	temp=b.split("\t")
	temp1=temp[0]
	temp2=temp[1]
	dic[temp1]=temp2
	#print dic[temp1]
	
f_sta=open("newexpertid/state","w")
f_sta.write("topic_id\texpert_number\n")
last=-1
for l in range(1,52):
	f_o=open("expertname/"+str(l))
	f_save=open("newexpertid/"+str(l),"w")
	f_back=open("backupid/"+str(l),"w")
	
	i=0
	for a in f_o.readlines():
		if a.count("\n")>0:
			o=a[:-1]
		else:
			o=a
#and int(dic[0])<=550)
		if (dic.has_key(o)and int(dic[o])<=550 and int(dic[o])!=last):
			f_back.write( o+"\t"+dic[o])
			f_save.write(dic[o])
			i+=1
			last=int(dic[o])
		else:
			
			f_back.write( o+"\n")

	f_sta.write(str(l)+"\t"+str(i)+"\n")
	f_back.close()
	f_o.close()
	f_save.close()
f_t.close()
