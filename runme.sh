
#$ tr -d '\r' <q.sh >q-new.sh
#$ mv q-new.sh q.sh
#sed -i 's/\r//' run.sh
#!/bin/sh


while getopts "n:t:s:l:p" opt
do
   case "$opt" in
      n) parameterA="$OPTARG" ;;
      t) parameterB="$OPTARG" ;;
      s) parameterC="$OPTARG" ;;
	  l) parameterD="$OPTARG" ;;
	  p) parameterE="$OPTARG" ;;
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

# Begin script in case all parameters are correct
#run appropriate scripts based on input - first segregation based on the language
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

fi

	
