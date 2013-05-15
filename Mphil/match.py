import sys
f_o=open("name_id")
f_t=open("name")

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
	

for a in f_o.readlines():
	o=a[:-1]
	
	if (dic.has_key(o)):
		sys.stdout.write( o+"\t"+dic[o])
	else:
		sys.stdout.write( o+"\n")


f_o.close()
f_t.close()
