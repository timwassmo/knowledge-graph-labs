from rdflib import Graph, Namespace, BNode, Literal, XSD, RDF



g = Graph()
g.parse(source="../data/lab_1.ttl")
ex = Namespace("http://example.org/")
g.bind("ex", ex)

# Removing old lies
g.remove((ex.Rick_Gates, ex.pleadGuilty, ex.LyingToFBI))
g.remove((ex.Michael_Flynn, ex.pleadGuilty, ex.LyingToFBI))
g.remove((ex.Michael_Cohen, ex.pleadGuilty, ex.LyingToCongress))

MichaelCohenLying = BNode()
MichaelFlynnLying = BNode()
RickGatesLying = BNode()

g.add((ex.Rick_Gates, ex.pleadGuilty, RickGatesLying))
g.add((ex.Michael_Flynn, ex.pleadGuilty, MichaelFlynnLying))
g.add((ex.Michael_Cohen, ex.pleadGuilty, MichaelCohenLying))

g.add((MichaelCohenLying, ex.liedTo, ex.Congress))
g.add((MichaelCohenLying, ex.liedAbout, Literal("President Trump’s former attorney pleaded guilty to lying to Congress about a Trump real estate deal in Moscow he had worked on before the 2016 presidential election. Prosecutors allege that in an August 2017 letter Cohen sent to congressional committees investigating Russian election interference, he falsely stated that the project ended in January 2016. Mueller’s investigators also allege that Cohen falsely stated that he had never agreed to travel to Russia for the real estate deal and that he did not recall any contact with the Russian government about the project. He pleaded guilty Nov. 29, 2018.", datatype=XSD.string)))

g.add((MichaelFlynnLying, ex.liedTo, ex.FBI))
g.add((MichaelFlynnLying, ex.negotiated, ex.pleaAgreement))

# Add addresses of Donald Trump
DonaldTrumpAddresses = BNode()
 # Mar-a-Lago as Blank node
MaraLago = BNode()
g.add((MaraLago, ex.name, Literal("Mar-a-Lago Club")))
g.add((MaraLago, ex.address, Literal("1100 S Ocean Blvd, Palm Beach, FL 33480, United States")))

g.add((DonaldTrumpAddresses, RDF.type, RDF.Seq))
g.add((DonaldTrumpAddresses, RDF._1, MaraLago))
g.add((DonaldTrumpAddresses, RDF._2, Literal("The White House, 1600 Pennsylvania Ave., NW Washington, DC 20500, United States, phone: 1-202-456-1414")))

g.add((ex.Donald_Trump, ex.lives_at, DonaldTrumpAddresses))
g.print()

g.parse(source="extend_graph.ttl")
# Save progress
g.serialize(destination="../data/lab_2.ttl", format="ttl")
g.serialize(destination="../data/trumpInvestigation.ttl", format="ttl")


# Extra (Ikke fullført):
for s,p,o in g.triples((None, None, None)):
    if s == ex.Donald_Trump:
        if isinstance(o, BNode):
            o = o.toPython()

        print(f'{s}\n'
              f'  ==> {p} {o}')
        print(s,p,o)
    elif o == ex.Donald_Trump:
        print(o)
