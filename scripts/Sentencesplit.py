#Performing sentence splitting for all the files in the Input folder
import os
import sys
import rdflib
import nltk
from rdflib import Graph,term,Literal,XSD
from rdflib.namespace import RDFS,RDF, FOAF, NamespaceManager
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import WhitespaceTokenizer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import string
tknzer=TweetTokenizer()
print("NLTK")
nif=rdflib.Namespace("http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#")
data=sys.argv[1]
for arg in sys.argv:
	lang = arg
count=0
for filename in os.listdir('Files/Input'+lang+'/'):
	if (count < int(data)):
		#print(filename)
		graph2=rdflib.Graph()
		graph2.parse('Files/Input'+lang+'/'+filename,format='nt')
		g=Graph()
		name=filename.split(".")[0]
		s=graph2.serialize(format="nt")
		for s,p,o in graph2:
			if type(o)==rdflib.term.Literal and nif.isString in p:
				sentences = nltk.sent_tokenize(o)
				for i in sentences:
					try:
						BI=o.index(i)
						EI=o.index(i)+len(i)
						g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=sentence_"+str(BI)+"_"+str(EI)),RDF.type,nif.Sentence])
						g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=sentence_"+str(BI)+"_"+str(EI)),nif.beginIndex,rdflib.term.Literal(str(BI))])
						g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=sentence_"+str(BI)+"_"+str(EI)),nif.endIndex,rdflib.term.Literal(str(EI))])
						g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=sentence_"+str(BI)+"_"+str(EI)),nif.anchorOf,rdflib.term.Literal(i)])
						g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=sentence_"+str(BI)+"_"+str(EI)),nif.referenceContext,rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=context")])     
					except:
						pass
		g.bind("nif",nif)        
		#print(g.serialize(format="turtle"))
		g.serialize(destination='Files/Sentence/'+filename,format="turtle")
		count=count+1
print("Your Output is stored in Sentence Folder")
