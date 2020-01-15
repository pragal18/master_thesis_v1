Enrichment of DBpedia NIF Dataset
Enrichment of DBpedia NIF Dataset is a compilation of Bash and Python3 scripts that enables to perform various Natural Language Processing tasks on Wikipedia on normal off-the-shelf hardware (e.g., a quad-core CPU, 8 GB of main memory, and 250 GB hard disk storage). 

INPUT 1) Language - "en" for english, "fr" for French, "de" for German, "ja" for Japanese, "es" for spanish
		 Default language is English if the language parameter is not specified. 
		 For new language to be used - Download the NIF Context file for that language from https://wiki.dbpedia.org/downloads-2016-10 , in the TTL format
		 Store the output on Files/Input<Language-short-form> . Even if you have your own text file, store it under this location and all the tasks could be performed.
      2) NLP task - "SEN" for sentence splitting
					"TOK" for Tokenisation
					"POS" for Part of speech tagging
					"ADL" for enrichment of additional links
	  3) Instance size - specify the number of wikipedia articles the operation should be performed on.
	  4) Article name specify a particular article name for which the operation has to be performed.
	  5) Tool name - "NLTK" for Using Natural Language Tool Kit package from Python3 , "GEN" for using Gensim and "SIO" for using Spacy IO .
					 Default is NLTK is none of it is specified.	
PROCESSING We downloads the required DBpedia NIF files from https://wiki.dbpedia.org/downloads-2016-10 , separate into individual articles , perform NLP tasks on various languages with a variety of tools. 
OUTPUT

Requirements
python>=3.4
NLTK >= 3.0
GENSIM>=3.4
SPACY>=2.0
rdflib>=4.0
numpy>=1.16.3 
Usage
  usage: ./run.sh [-h] [-p PROJECT] [-i ITERATIONS] [-d DAMPING] [-s START]
                     [-b] [-l]
                     wikilang

  Compute PageRank on Wikipedia.

  positional arguments:
    wikilang              Wikipedia language edition, e.g. "en". "ALL" for
                          computing PageRank over all languages available in a
                          project.

  optional arguments:
    -h, --help            show this help message and exit
    -p PROJECT, --project PROJECT
                          Wiki project, currently supported [wiki, books,
                          source, versity, news]. (default: wiki)
    -i ITERATIONS, --iterations ITERATIONS
                          PageRank number of iterations. (default: 40)
    -d DAMPING, --damping DAMPING
                          PageRank damping factor. (default: 0.85)
    -s START, --start START
                          PageRank starting value. (default: 0.1)
    -b, --bigmem          PageRank big memory flag. (default: False)
    -l, --links           Only extract links (skip PageRank). (default: False)
Examples
Compute PageRank on the current dump of English Wikipedia:

$ ./danker.sh en
$ ./danker.sh en --bigmem
Compute PageRank on the union of all language editions:

$ ./danker.sh ALL
$ ./danker.sh ALL --bigmem    # caution, you will need some main memory for that
Compute PageRank for each Wikipedia language edition separately:

$ for i in $(./script/get_languages.sh); do ./danker.sh "$i"; done
$ for i in $(./script/get_languages.sh); do ./danker.sh "$i" -b; done
Compute PageRank on the English version of Wikibooks:

$ ./danker.sh en --project books
$ ./danker.sh en --bigmem --project books
Compute PageRank on any other graph

Download
Output of ./danker.sh ALL on bi-weekly Wikipedia dumps.

2019-10-29
https://danker.s3.amazonaws.com/2019-10-29.allwiki.links.stats.txt
https://danker.s3.amazonaws.com/2019-10-29.allwiki.links.rank.bz2
2019-10-09
https://danker.s3.amazonaws.com/2019-10-09.allwiki.links.stats.txt
https://danker.s3.amazonaws.com/2019-10-09.allwiki.links.rank.bz2
2019-09-28
https://danker.s3.amazonaws.com/2019-09-28.all.links.stats.txt
https://danker.s3.amazonaws.com/2019-09-28.all.links.rank.bz2
2019-09-12
https://danker.s3.amazonaws.com/2019-09-12.all.links.stats.txt
https://danker.s3.amazonaws.com/2019-09-12.all.links.rank.bz2
2019-08-21
https://danker.s3.amazonaws.com/2019-08-21.all.links.stats.txt
https://danker.s3.amazonaws.com/2019-08-21.all.links.rank.bz2
2019-08-15
https://danker.s3.amazonaws.com/2019-08-15.all.links.stats.txt
https://danker.s3.amazonaws.com/2019-08-15.all.links.rank.bz2
2019-07-28
https://danker.s3.amazonaws.com/2019-07-28.all.links.stats.txt
https://danker.s3.amazonaws.com/2019-07-28.all.links.rank.bz2
2019-07-08
https://danker.s3.amazonaws.com/2019-07-08.all.links.stats.txt
https://danker.s3.amazonaws.com/2019-07-08.all.links.rank.bz2
2019-06-28
https://danker.s3.amazonaws.com/2019-06-28.all.links.stats.txt
https://danker.s3.amazonaws.com/2019-06-28.all.links.rank.bz2
2019-06-07
https://danker.s3.amazonaws.com/2019-06-07.all.links.stats.txt
https://danker.s3.amazonaws.com/2019-06-07.all.links.rank.bz2
2019-05-28
https://danker.s3.amazonaws.com/2019-05-28.all.links.stats.txt
https://danker.s3.amazonaws.com/2019-05-28.all.links.rank.bz2
Previous work
Before danker, I performed a number of experiments with DBpedia "page links" datasets most of which are documented at https://web.archive.org/web/20180222182923/https://people.aifb.kit.edu/ath/.

Test
The unit tests assure correctness and compare the results of danker to the PageRank implementation of NetworkX. The tests need the numpy and networkx libraries installed.

Execute the unit tests as follows:

python3 -m unittest test/danker_test.py

In the directory test is a small graph with which you can try out the PageRank core of danker.

$ ./danker/danker.py ./test/graphs/test.links 0.85 40 1
1.2.3.4.5.6.7.8.9.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.
Computation of PageRank on './test/graphs/test.links' with danker took 0.00 seconds.
C	3.1828140590777672
B	3.5642607869667629
A	0.30410528185693986
D	0.3626006631927996
F	0.3626006631927996
E	0.75035528185693967
G	0.15000000000000002
H	0.15000000000000002
I	0.15000000000000002
K	0.15000000000000002
L	0.15000000000000002
$ ./danker/danker.py ./test/graphs/test.links ./test/graphs/test.links.right 0.85 40 1
1.2.3.4.5.6.7.8.9.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.
Computation of PageRank on './test/graphs/test.links' with danker took 0.01 seconds.
A	0.30410528185693986
B	3.5642607869667629
C	3.1828140590777672
D	0.3626006631927996
E	0.75035528185693967
F	0.3626006631927996
G	0.15000000000000002
L	0.15000000000000002
K	0.15000000000000002
I	0.15000000000000002
H	0.15000000000000002
If you normalize the output values (divide each by 11) the values compare well to https://commons.wikimedia.org/wiki/File:PageRank-Beispiel.png or, if you compute percentages (division by the sum), they are similar to https://commons.wikimedia.org/wiki/File:PageRanks-Example.svg (same graph).