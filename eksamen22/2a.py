from rdflib import Graph, Namespace, OWL, RDF, RDFS, XSD, Literal

g = Graph()
ex = Namespace("http://ex.org#")
g.bind('ex', ex)
a = RDF.type

g.add((ex.Agent, RDF.type, OWL.Class))
g.add((ex.Publication, RDF.type, OWL.Class))
for agent in [ex.Author, ex.Organization, ex.Country]:
    g.add((agent, RDFS.subClassOf, ex.Agent))

# Properties
g.add((ex.name, RDFS.domain, ex.Agent))
g.add((ex.name, RDFS.range, XSD.string))

g.add((ex.country, RDFS.domain, ex.Author))
g.add((ex.country, RDFS.range, ex.Country))

g.add((ex.affiliation, RDFS.domain, ex.Author))
g.add((ex.affiliation, RDFS.range, ex.Organization))

g.add((ex.publisher, RDFS.domain, ex.Publication))
g.add((ex.publisher, RDFS.range, ex.Organization))

g.add((ex.author, RDFS.domain, ex.Publication))
g.add((ex.author, RDFS.range, ex.Author))

g.add((ex.title, RDFS.domain, ex.Publication))
g.add((ex.title, RDFS.range, XSD.string))

g.add((ex.year, RDFS.domain, ex.Publication))
g.add((ex.year, RDFS.range, XSD.integer))

g.add((ex.publication, RDFS.domain, ex.Paper))
g.add((ex.publication, RDFS.range, ex.Publication))

g.add((ex.Paper, RDFS.subClassOf, ex.Publication))



# 2b:
#1:
g.add((ex.The_semantic_web, a, ex.Paper))
g.add((ex.The_semantic_web, ex.author, ex.Tim_Berners_Lee))
g.add((ex.The_semantic_web, ex.author, ex.James_Hendler))
g.add((ex.The_semantic_web, ex.publication, ex.Scientific_American))
g.add((ex.The_semantic_web, ex.publisher, ex.Springer_Nature))
g.add((ex.The_semantic_web, ex.year, Literal(2001)))
g.add((ex.The_semantic_web, ex.title, Literal("The Semantic Web")))
g.add((ex.The_sumantic_web, a, ex.Paper))
g.add((ex.The_sumantic_web, ex.author, ex.Tim_Berners_Lee))
g.add((ex.The_semantic_web, ex.year, Literal(2020)))
g.add((ex.The_sumasntic_web, ex.author, ex.Tim_Berners_Lee))
g.add((ex.The_semasntic_web, ex.year, Literal(2010)))
#2:

g.add((ex.Tim_Berners_Lee, a, ex.Author))
g.add((ex.Tim_Berners_Lee, ex.name, Literal("Tim Berners Lee")))
g.add((ex.Tim_Berners_Lee, ex.affiliation, ex.Massachusets_Institute_of_Technology))
g.add((ex.Tim_Berners_Lee, ex.country, ex.United_States))



result = g.query("""
PREFIX ex: <http://ex.org#>
construct {?author ?affiliation ?county}
where {
    ?author 
}
""")

for row in result:
    print(row[0])

# g.print()
