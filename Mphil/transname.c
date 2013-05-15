#include <stdlib.h>
#include <stdio.h>
typedef char line[10000];
line name_array, file_name_array;
char map_char(char x) {
	if (isalnum(x))
		return x;
	/*if (x==' ')
		return '_';
	else if (x =='\0')
		return '';
	else 
		return '=';*/
	return (x == ' ') ? '_' : '=';
}
int is_hidden_suffix(char *x) {
	if (x == NULL) return 0;
	if (!isdigit(x[0]) || !isdigit(x[1]) || !isdigit(x[2]) || !isdigit(x[3]))
		return 0;
	return x[4] == '\0';
}
char *make_file_name(char *name){
int i =0 ;
char c, *lname,*fname,*help;
strcpy(name_array,name);
lname =strrchr(name_array,' ');
if (lname){
	fname = name_array;
	*lname++ = '\0';
	if(strcmp(lname,"Jr.")==0||strcmp(lname,"II") ==0 || strcmp(lname,"III")==0 || strcmp(lname,"IV")==0 || is_hidden_suffix(lname))
	{
		help = strrchr(fname,' ');
		if (help) {
			--lname; *lname = ' ';
			*help = '\0';
			lname = help+1;
		}
	}
}else{
	fname = strrchr (name_array,'\0');
	lname = name_array;
}
if(lname)
	while(c = *lname ++)
		file_name_array[i++]= map_char(c);
file_name_array[i++]=':';
if(fname)
	while (c = *fname++)
		file_name_array[i++]=map_char(c);
file_name_array[i++] = '\0';
return file_name_array;
}

void print_keys_url(char *name){
char *s =make_file_name(name);
//printf("http://dblp.nui-trier.de"
//	   "/rec/pers/%c/%s/xk\n",tolower(*s),s);
printf("http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/%c/%s.html\n",tolower(*s),s);

}
main(int argc,char *argv[]){


printf("%s",argv[1]);
static const char filename[] ;//=&argv[1]; // this is the file name !!!!!!!!!!!!!!!!!!!!!
strcpy(filename, argv[1]);


FILE *file = fopen ( filename, "r" );


if ( file != NULL )
{
char line [ 128 ]; /* or other suitable maximum line size */
char dest[128];
while ( fgets ( line, sizeof line, file ) != NULL ) /* read a line */
{
char *s =make_file_name(line);
print_keys_url(line);
/*int i=0;
int k=0;
for (;line[i]!='\0';i++,k++)
{
	 if (line[i] == '\r' || line[i] == '\n') {
		i++;
		continue;
	}
	dest[k]=line[i];
	

}
dest[k]='\0';

dest = line;
while (*dest != '\0') {
   if (*dest == '\r' || *dest == '\n') {
     dest++;
     continue;
    }
    *result++ = *dest++;
}
fputs ( dest, stdout );*/
 /* write the line */

}
fclose ( file );
}
else
{
perror ( filename ); /* why didn't the file open? */
}
return 0;

//after get the link, you still need to replace the '=:' by ':'

//char *tt ="Chris H. Q. Ding";
//print_keys_url(tt);
}
