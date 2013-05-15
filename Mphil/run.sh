#!/bin/bash

# $1 data directory
# $2 binary file
rm -f FinalRt.csv
for f in `ls $1`
do
        rm -f $1/$f/tmpconfig
	echo "m=10" > $1/$f/tmpconfig
	echo "M=20" >> $1/$f/tmpconfig
	echo "dim=3" >> $1/$f/tmpconfig
	echo "reinsert_p=2" >> $1/$f/tmpconfig
	cat $1/$f/config >> $1/$f/tmpconfig
	echo "$1/$f/data.txt" >> $1/$f/tmpconfig
	echo "$1/$f/attr.txt" >> $1/$f/tmpconfig
	echo "$1/$f" >> $1/$f/tmpconfig
	rm -f $1/$f/FinalTime$f.csv
	rm -f $1/$f/FinalResult$f.csv
	rm -f $1/$f/FinalStat$f.csv
#	rm -f FinalRt.csv
	i=0
	while [ $i -lt 1 ]
	do
		echo "Running $i"
	       	$2 $1/$f/tmpconfig
		cat $1/$f/time.txt >> $1/$f/FinalTime$f.csv
		printf "\n" >> $1/$f/FinalTime$f.csv
	cat $1/$f/stat.txt >> $1/$f/FinalStat$f.csv
		printf "\n" >> $1/$f/FinalStat$f.csv
		cat $1/$f/result.txt >> $1/$f/FinalResult$f.csv
		printf "\n" >> $1/$f/FinalResult$f.csv
		cat $1/$f/result.txt >> FinalRt.csv
                echo ",$f" >> FinalRt.csv
		let i=i+1
	done
done

