Readme
-------------
The program is used to generate the similarity matrix of topic-paper and topic-reviewer.

The data is generated by following steps:
1. Remove the stop words 
	Command
	========
	>./tfidf_remove_stop_words/runstem
    The data will be saved in 'tfidf_remove_stop_words/after'.

2. Calculate the tfidf matrix.
	Command
	========
	>python mytf.py
    The data will be saved in 'tfidf' folder.

3. Calculate the similarity.
	Command
	========
	>python similarity.py
   The data will be saved in 'similarity' folder.

Input/Output Data
-------------
-Input: The raw input data is collected by script from DBLP, citeseer, etc. We stored all the information about one paper or topic or reviewer in one file. The original data is stored in the 'paper', 'topic' and 'profile' folders under the 'tfidf remove stop words' folder.

-Output: The final outcome data is stored in PT and RT which are under the 'similarity' folder.


There are three scripts and three folders in the package here:
Scripts:
-----------
1. tfidf.py: Calculate the tfidf weight per term in the data. This script will be called in the 'mytf' script.

2. mytf.py: Print the tfidf matrix in certain format. The outcome will be stored in the corresponding folder which are under 'tfidf' folder.

3. similarity.py: Calculate the cosine similarity between topic and papers/reviewers. The outcome will be stored in 'similarity' folder.

Folders:
-----------
1. 'tfidf_remove_stop_words' contains three files and four folders:
   -Files:
   -----------
   -stopword: the stopword list from web which will be used in 'stem' script
   -stem: python script to remove the stop words from public web resource
   -runstem: a bash script to run the stem script
   
   -Folders:
   -----------
   -'paper' folder: the collected corpus for papers 
   -'topic' folder: the collected corpus for topics
   -'profile' folder:  the collected corpus for profiles (reviewers)
   -'after' folder: The 'stem' script will store the processed data under this folder.

2. 'tfidf' includes three folders holding tfidf weight matrix:
   -'paper' folder: Each file represents one paper. 
   -'topic' folder: Each file represents one topic.
   -'profile' folder: Each file represents one reviewer.
   The data (word_id tfidf_weight) in each file is sorted in terms of word_id.
	Example: in File topic/1
	======
	word_id 	tfidf_weight)
	1	5.12458572891
	2	0.631174153864
	3	0.86332286012
	4	1.67768628316
	5	0.79637607049

3. 'similarity' include two files:
   -PT: similarity matrix of topic-paper (49 topics * 496 papers)
   -RT: similarity matrix of topic-reviewer (49 topics * 550 reviewers)

P.S.
The main python source of tfidf is download from web and I wrote another script to call the tfidf according to our requirement. http://code.google.com/p/tfidf/

If you want to use another corpus to generate the data, you may need to modify the 'mytf' since I hard code the input source file name there.

You also can try to change another 'stopword' for the protetial improvement.

