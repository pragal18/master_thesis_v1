import rdflib
import nltk
import sys
from rdflib import Graph,term
from rdflib.namespace import RDFS,RDF, FOAF, NamespaceManager
nif=rdflib.Namespace("http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#")
graph2=rdflib.Graph()
name=sys.argv[1]
for arg in sys.argv:
	lang = arg
graph2.parse('Files/Input'+lang+'/'+name+'.ttl',format='nt')
g=Graph()
s=graph2.serialize(format="nt")
count=0
namespace_manager = NamespaceManager(Graph())
namespace_manager.bind('ns1', nif, override=True)

for s,p,o in graph2:
    if type(o)==rdflib.term.Literal and nif.isString in p:
        sentences = nltk.sent_tokenize(o)
        tokens = [nltk.word_tokenize(sent) for sent in sentences]
        tokens2= nltk.word_tokenize(o)
        for i in sentences:
            try:
                BI=o.index(i)
                EI=o.index(i)+len(i)
            except:
                pass
            g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=sentence_"+str(BI)+"_"+str(EI)),RDF.type,nif.Sentence])
            g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=sentence_"+str(BI)+"_"+str(EI)),nif.beginIndex,rdflib.term.Literal(str(BI))])
            g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=sentence_"+str(BI)+"_"+str(EI)),nif.endIndex,rdflib.term.Literal(str(EI))])
            g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=sentence_"+str(BI)+"_"+str(EI)),nif.anchorOf,rdflib.term.Literal(i)])
            g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=sentence_"+str(BI)+"_"+str(EI)),nif.referenceContext,rdflib.term.URIRef("http://dbpedia.org/resource/Animalia_(book)?dbpv=2016-10&nif=context")])
    
g.bind("nif",nif)  
#print(g.serialize(format="turtle"))
g.serialize(destination="Files/Search/"+ name+'-sentence.ttl',format="turtle")

