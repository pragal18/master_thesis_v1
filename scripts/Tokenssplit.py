#performing tokenization for all the files in a folder
import os
import nltk
from rdflib import Graph,term,Literal,XSD
from rdflib.namespace import RDFS,RDF, FOAF, NamespaceManager
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import WhitespaceTokenizer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import string
import sys
import rdflib
tknzer=TweetTokenizer()
data = sys.argv[1]
for arg in sys.argv:
	lang = arg
track=0
nif=rdflib.Namespace("http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#")

def spans(txt):
    tokens=tknzer.tokenize(txt)
    offset = 0
    for token in tokens:
        offset = txt.find(token, offset)
        yield token, offset, offset+len(token)
        offset += len(token)
        
for filename in os.listdir('Files/Input'+lang+'/'):
	if(track < int(data)):
		#print(filename)
		graph2=rdflib.Graph()
		graph2.parse('Files/Input'+lang+'/'+filename,format='nt')
		g=Graph()
		name=filename.split(".")[0]
		s=graph2.serialize(format="nt")
		for s,p,o in graph2:
			if type(o)==rdflib.term.Literal and nif.isString in p:
				sentences = nltk.sent_tokenize(o)
				for i in range(len(sentences)):
					count=0
					try:
						BII=o.find(sentences[i])
						for token in spans(sentences[i]):
							assert token[0]==sentences[i][token[1]:token[2]]
							BI=BII+token[1]
							EI=BII+token[2]
							if token[0] not in string.punctuation:
								g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),RDF.type,nif.Word])
								g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.beginIndex,rdflib.term.Literal(str(BI))])
								g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.endIndex,	rdflib.term.Literal(str(EI))])
								g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.anchorOf,rdflib.term.Literal(token[0])])
								g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.referenceContext,rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=context")])       
					except:
						pass       
		g.bind("nif",nif)        
		#print(g.serialize(format="turtle"))
		g.serialize(destination='Files/Tokens/'+filename,format="turtle")
		track=track+1
print("Please check the Tokens folder for output files")