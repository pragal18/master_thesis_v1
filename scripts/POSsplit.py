#Performing Part-of-speech tagging on all files in the Context folder
import rdflib
import nltk
from rdflib import Graph,term,Literal,XSD
from rdflib.namespace import RDFS,RDF, FOAF, NamespaceManager
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import WhitespaceTokenizer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import string
import os
import numpy as np
import pandas as pd
import sys
tknzr2 = RegexpTokenizer(r'\w+')
nif=rdflib.Namespace("http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#")
tknzer=TweetTokenizer()
take = sys.argv[1]
for arg in sys.argv:
	lang = arg
track=0

def spans(txt):
    tokens=nltk.word_tokenize(txt)
    offset = 0
    for token in tokens:
        offset = txt.find(token, offset)
        yield token, offset, offset+len(token)
        offset += len(token)
    
data=pd.read_excel("pos-mapping2.xlsx")
for filename in os.listdir('Files/Input'+lang+'/'):
	if(track < int(take)):
		#print(filename)
		name=filename.split(".")[0]
		graph2=rdflib.Graph()
		graph2.parse("Files/Input"+lang+"/"+filename,format='nt')
		g=Graph()
		for s,p,o in graph2:
			if type(o)==rdflib.term.Literal and nif.isString in p:
				sentences = nltk.sent_tokenize(o)
				tokens = [nltk.word_tokenize(sent) for sent in sentences]
				tagged = [nltk.pos_tag(sent) for sent in tokens] 
				for i in range(len(sentences)):
					count=0
					try:
						BII=o.find(sentences[i])
						for token in spans(sentences[i]):
							assert token[0]==sentences[i][token[1]:token[2]]
							BI=BII+token[1]
							EI=BII+token[2]
							#print(token[0]+" "+tagged[i][count][1])
							val=data.posfullform1[data.posshortcut1==tagged[i][count][1]]
							for jumbo in val:
								posfullform=jumbo
							hello="http://purl.org/olia/olia.owl#"+ posfullform
							value=data.posfullformtype1[data.posshortcut1==tagged[i][count][1]]
							for jumbos in value:
								posfullformtype=jumbos
							hell="http://purl.org/olia/olia.owl#"+ posfullformtype
							if token[0] not in string.punctuation:
								g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),RDF.type,nif.Word])
								g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.beginIndex,rdflib.term.Literal(str(BI))])
								g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.endIndex,rdflib.term.Literal(str(EI))])
								g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.anchorOf,rdflib.term.Literal(token[0])])
								g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.referenceContext,rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=context")])       
								g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.oliaLink,rdflib.term.URIRef("http://purl.org/olia/penn.owl#"+tagged[i][count][1])])
								g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.oliaCategory,term.URIRef(hello)])                         
								g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.oliaCategory,term.URIRef(hell)])
							count=count+1
					except:
						pass
                               
		g.bind("nif",nif)        
		#print(g.serialize(format="turtle"))
		g.serialize(destination="Files/POS/"+filename,format="turtle")
		track=track+1
print("Please Check the POS folder for output files")
