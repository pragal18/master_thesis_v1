#storing the result of tokenization in triples for an individual file named Animalia_(book)
#Please refer the Animalia_(book)-tokenization.ttl for the output
import rdflib
import nltk
from rdflib import Graph,term,Literal,XSD
from rdflib.namespace import RDFS,RDF, FOAF, NamespaceManager
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import WhitespaceTokenizer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import string
import sys
tknzr2 = RegexpTokenizer(r'\w+')
nif=rdflib.Namespace("http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#")
tknzer=TweetTokenizer()
graph2=rdflib.Graph()
name=sys.argv[1]
for arg in sys.argv:
	lang = arg
graph2.parse('Files/Input'+lang+'/'+name+'.ttl',format='nt')
g=Graph()
s=graph2.serialize(format="nt")
def spans(txt):
    tokens=nltk.word_tokenize(txt)
    offset = 0
    for token in tokens:
        offset = txt.find(token, offset)
        yield token, offset, offset+len(token)
        offset += len(token)
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
                        g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),RDF.type,nif.Word])
                        g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.beginIndex,rdflib.term.Literal(str(BI))])
                        g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.endIndex,rdflib.term.Literal(str(EI))])
                        g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.anchorOf,rdflib.term.Literal(token[0])])
                        g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.referenceContext,rdflib.term.URIRef("http://dbpedia.org/resource/Animalia_(book)?dbpv=2016-10&nif=context")])       
                        count=count+1
                except:
                    pass
g.bind("nif",nif)        
g.serialize(destination='Files/Search/'+name+"-tokenization.ttl",format="turtle") 