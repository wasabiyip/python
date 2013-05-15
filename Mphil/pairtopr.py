'''
input:
coi1.txt
coi12.txt
allcoi.txt

output:
reviewer*paper
all_coi
coi_1
coi_12
'''
#f1=open("indcoi1.txt")
#f12=open("indcoi12.txt")
f_all=open("indallcoi.txt")

f_author_paper=open("authorpaper_m")

f_all_out=open("all_coi","w")
#fout1=open("coi_1","w")
#fout12=open("coi_12","w")

#########1###########author dictionary
dic_ap={}
temp=[]
for lines in f_author_paper.readlines():
	temp=lines[:-2].split("\t")
	dic_ap[temp[0]]=temp[1:]


##########2#############coi1
dic1={}
temp2=[]
for line in f_all.readlines():#
	temp=line[:-1].split("\t")
	if(dic_ap.has_key(temp[1])):
		if (dic1.has_key(temp[0])):
			temp2=dic1[temp[0]]
			#print "1",temp2				
			temp2=temp2+dic_ap[temp[1]]
			dic1[temp[0]]=temp2
			#print "2",temp2	
			#print dic_ap[temp[1]]
		else:
			dic1[temp[0]]=dic_ap[temp[1]]
#dic1 :reviewerid paperid

###########3#############print paper_reviewer
paper_reviewer=[[0 for col in range(550)] for row in range(496)]

for key in dic1.iterkeys():
	temp=dic1[key]
	for ll in range(0,len(temp)-1):
		paper_reviewer[int(temp[ll])-1][int(key)-1]=1


#############4##########output
for i in range(496):
	for l in range(550):
		f_all_out.write( str(paper_reviewer[i][l])+"\t")#
	f_all_out.write("\n")#

"""
#coi_12
for line in f12.readlines():
	temp=dic.split("\t")
	


#all
for line in f_all.readlines():
	temp=dic.split("\t")
	

"""

f_all.close()
#f1.close()
#f12.close()

f_author_paper.close()


f_all_out.close()
#fout1.close()
#fout12.close()



