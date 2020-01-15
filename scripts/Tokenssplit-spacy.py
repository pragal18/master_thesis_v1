#performing tokenization for all the files in a folder
import os
from rdflib import Graph,term,Literal,XSD
from rdflib.namespace import RDFS,RDF, FOAF, NamespaceManager
import string
import sys
import rdflib
import spacy
import re
nlp = spacy.load('en_core_web_sm')
data = sys.argv[1]
for arg in sys.argv:
	lang = arg
track=0
nif=rdflib.Namespace("http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#")

def spans(txt):
    print(txt)
    doc=nlp(txt.encode().decode('utf-8'))
    offset = 0
    for ing in doc:
	    print(ing.text)
	    offset = txt.find(token,offset)
	    yield ing.text , offset, offset+len(ing.text)
	    offset = offset + len(ing.text)
		
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
				sentences = nlp(o.encode().decode('utf-8'))
				for i in sentences.sents:
					#print("entered for:")
					#print(i.text.encode(sys.stdout.encoding, errors='replace'))
					try:
						#print("entered try")
						BII=o.encode(sys.stdout.encoding, errors='replace').index(i.text.encode(sys.stdout.encoding, errors='replace'))
						#print(BII)
						EII=o.encode(sys.stdout.encoding, errors='replace').index(i.text.encode(sys.stdout.encoding, errors='replace'))+len(i.text.encode(sys.
						stdout.encoding, errors='replace'))
						#print(EII)
						#print(i.text.encode(sys.stdout.encoding, errors='replace'))
						inner=nlp(i.text.encode().decode('utf-8'))
						offset=0
						for ing in inner:
						    #print(ing.text.encode().decode('utf-8'))
						    #offset=i.text.encode().decode('utf-8').find(ing.text.encode().decode('utf-8'),offset)
						    offset = i.text.encode().decode('utf-8').index(ing.text.encode().decode('utf-8'),offset)
						    BI= offset+ BII
						    EI=BI +len(ing.text.encode().decode('utf-8'))
						    #print(EI)
						    if ing.text.encode().decode('utf-8') not in string.punctuation:
							    g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),RDF.type,nif.Word])
							    g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.beginIndex,rdflib.term.Literal(str(BI))])
							    g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.endIndex,	rdflib.term.Literal(str(EI))])
							    g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.anchorOf,rdflib.term.Literal(ing.text.encode().decode('utf-8'))])
							    g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.referenceContext,rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=context")])  
					except:
					    pass
		g.bind("nif",nif)        
		#print(g.serialize(format="turtle"))
		g.serialize(destination='Files/Tokens/'+filename,format="turtle")
		track=track+1
print("Your Output is stored in Tokens Folder via spacyio")