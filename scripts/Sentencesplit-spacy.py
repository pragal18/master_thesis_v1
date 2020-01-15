#Performing sentence splitting for all the files in the Input folder
import os
import sys
import rdflib
from rdflib import Graph,term,Literal,XSD
from rdflib.namespace import RDFS,RDF, FOAF, NamespaceManager
import string
import spacy
nif=rdflib.Namespace("http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#")
import re
nlp = spacy.load('en_core_web_sm')
data=sys.argv[1]
#print(data)
for arg in sys.argv:
	lang = arg
count=0
print("spacy")
if lang != "EN" :
    nlp = spacy.load(''+lang+'_core_news_sm')

    
for filename in os.listdir('Files/Input'+lang+'/'):
	if (count < int(data)):
		#print(filename)
		graph2=rdflib.Graph()
		graph2.parse('Files/Input'+lang+'/'+filename,format='nt')
		g=Graph()
		name=filename.split(".")[0]
		#print(name)
		s=graph2.serialize(format="nt")
		for s,p,o in graph2:
			#print("inside graph")
			#print(o.encode('utf-8'))
			if type(o)==rdflib.term.Literal and nif.isString in p:
				#print("entered if")
				sentences = nlp(o.encode().decode('utf-8'))
				for i in sentences.sents:
					#print("entered for:")
					#print(i.text.encode(sys.stdout.encoding, errors='replace'))
					try:
						#print("entered try")
						BI=o.encode(sys.stdout.encoding, errors='replace').index(i.text.encode(sys.stdout.encoding, errors='replace'))
						#print(BI)
						EI=o.encode(sys.stdout.encoding, errors='replace').index(i.text.encode(sys.stdout.encoding, errors='replace'))+len(i.text.encode(sys.stdout.encoding, errors='replace'))
						#print(EI)
						#print("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=sentence_"+str(BI)+"_"+str(EI))
						#print(RDF.type)
						#print(nif.Sentence)
						g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=sentence_"+str(BI)+"_"+str(EI)),RDF.type,nif.Sentence])
						#print("1")
						g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=sentence_"+str(BI)+"_"+str(EI)),nif.beginIndex,rdflib.term.Literal(str(BI))])
						#print("2")
						g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=sentence_"+str(BI)+"_"+str(EI)),nif.endIndex,rdflib.term.Literal(str(EI))])
						#print("3")
						g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=sentence_"+str(BI)+"_"+str(EI)),nif.anchorOf,rdflib.term.Literal(i.text)])
						#print("4")
						g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=sentence_"+str(BI)+"_"+str(EI)),nif.referenceContext,rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=context")])    
						#print("one triplet is set in the overall situation right now")
					except:
						pass
		g.bind("nif",nif)        
		#print(g.serialize(format="turtle"))
		g.serialize(destination='Files/Sentence/'+filename,format="turtle")
		count=count+1
print("Your Output is stored in Sentence Folder via spacy")
