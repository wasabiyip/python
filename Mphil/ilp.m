%function [x] = ilp(pq, rq, C, A, B,W)
function ilp(input1,input2,output)

%ilp Summary of this function goes here
%   Detailed explanation goes here
%   Input: pq---the quota per paper
%          rq---the quota per reviewer
%          A----paper nodes n*nk
%          B----reviewer nodes k*nk
%%%%       PT---paper topic weight n*t
%%%%       TR---topic reviewer weight t*k
%          W----weight matrix nk*1
%   Output:x----assignment vector

config=dlmread(strcat(input1,'/config'));
con=dlmread(strcat(input1,'/coi.txt'));
n=config(3);
k=config(4);
pq=config(5);
rq=config(6);
PT=dlmread(strcat(input1,'/PT1.txt'));
PT=PT(:,1:49);
RT=dlmread(strcat(input1,'/RT1.txt'));
RT=RT(:,1:49);
inputdir=strcat(input2,'/PRC.txt')
PRC=dlmread(inputdir);
PRC=PRC(:,1:k);
con=con(:,1:k);
TR=RT';

rol=zeros(n*k,1);
col=zeros(n*k,1);
ct=1;
for i=1:n
    for j=1:n*k
        if (j>(i-1)*k & j<=i*k)
            rol(ct)=i;
            col(ct)=j;
            ct=ct+1;
        end        
    end
end

A=sparse(rol,col,ones(n*k,1));
rol1=zeros(n*k,1);
col1=zeros(n*k,1);
ct=1;
for i=1:k
    for j=1:n
        rol1(ct)=i;
        col1(ct)=(j-1)*k+i;
        ct=ct+1;
    end
end
B=sparse(rol1,col1,ones(n*k,1));
x=zeros(n*k,1);
W=zeros(n*k,1);
T=PT*TR;
for i=1:n
	for j=1:k
		W((i-1)*k+j)=T(i,j);
	end
end
f=-W';
Rq=ones(k,1)*rq;
Pq=ones(n,1)*pq;
lb=zeros(n*k,1);
ub=ones(n*k,1);

COI=zeros(n*k,1);
for i=1:n
    for j=1:k
        COI((i-1)*k+j,1)= con(j,1);
    end
end
ub=ub-COI;
options=optimset('LargeScale','off','Simplex','on');
x0=zeros(n*k,1);
%x=ones(n*k,1);
x=linprog(f,B,Rq,A,Pq,lb,ub,x0,options);
%x=bintprog(f,B,Rq);
r=zeros(n*pq,1);
c=zeros(n*pq,1);
ct=1;
for i=1:n
	for j=1:k
        if(round(x((i-1)*k+j))==1)
            r(ct)=i;
            c(ct)=j;
            ct=ct+1;
        end
	end
end  
R=[r c];
outputdir=strcat(output,'/assign.txt')
dlmwrite(outputdir,R,' ');
        
end

