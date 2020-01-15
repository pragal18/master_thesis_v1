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
  usage: ./run.sh [-n NUMBER] [-l LANGUAGE] [-t TASK] [-e METHOD/LIBRARY] [-s SEARCH]

  Compute PageRank on Wikipedia.

  positional arguments:
    wikilang              
    
    

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

