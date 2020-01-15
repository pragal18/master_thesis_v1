#$ tr -d '\r' <q.sh >q-new.sh
#$ mv q-new.sh q.sh
#sed -i 's/\r//' run.sh
#!/bin/sh


while getopts "n:t:s:e:l:" opt
do
   case "$opt" in
      n) parameterA="$OPTARG" ;;
      t) parameterB="$OPTARG" ;;
      s) parameterC="$OPTARG" ;;
	  l) parameterD="$OPTARG" ;;
	  e) parameterE="$OPTARG" ;;
   esac
done

# Print helpFunction in case parameters are empty
if [ -z "$parameterA" ] && [ -z "$parameterB" ] && [ -z "$parameterC" ]
then
   echo "Insufficient arguments to run the script";
fi

if [ -z "$parameterD" ]
then
	parameterD="EN";
fi
echo "$parameterE"
if [ -z "$parameterE" ]
then
    parameterE="NLTK";
fi
# Begin script in case all parameters are correct
#run appropriate scripts based on input - first segregation based on the language
if [ $parameterE == "NLTK" ]
then
if [ -z "$parameterC" ]
then 
	case $parameterB in
		(SEN)    python scripts/Sentencesplit.py $parameterA $parameterD
		;;
		(TOK)    python scripts/Tokenssplit.py $parameterA $parameterD
        ;;
		(POS)    python scripts/POSsplit.py $parameterA $parameterD
        ;;    
	esac

else
	case $parameterB in
    (SEN)    python scripts/Search-sent.py $parameterC $parameterD
        ;;
    (TOK)    python scripts/Search-Token.py $parameterC	$parameterD
        ;;
    (POS)    python scripts/Search-POS.py $parameterC $parameterD
        ;;    
    esac
fi

elif [ $parameterE == "SIO" ]
then
if [ -z "$parameterC" ]
then 
	case $parameterB in
	(SEN)    python scripts/Sentencesplit-spacy.py $parameterA $parameterD
		;;
	(TOK)    python scripts/Tokenssplit-spacy.py $parameterA $parameterD
        ;;
	(POS)    python scripts/POSsplit-spacy.py $parameterA $parameterD
        ;;    
	esac

else
	case $parameterB in
    (SEN)    python scripts/Search-sent.py $parameterC $parameterD
        ;;
    (TOK)    python scripts/Search-Token.py $parameterC	$parameterD
        ;;
    (POS)    python scripts/Search-POS.py $parameterC $parameterD
        ;;    
	esac	
fi
fi