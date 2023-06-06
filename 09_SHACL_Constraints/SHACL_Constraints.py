from pyshacl import validate
from rdflib import Graph

data_graph = Graph()
turtle_data = '''@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix ex: <http://example.org/> .

ex:Donald_Trump
    a ex:President .
 
ex:Paul_Manafort 
    a ex:PersonUnderInvestigation ;
    foaf:name 
        "Paul Manafort"@en ;  
    ex:hasBusinessPartner ex:Rick_Gates .

ex:Rick_Gates 
    a ex:PersonUnderInvestigation ;
    foaf:name 
        "Rick Gates"@en ;  
    skos:altLabel 
        "Richard William Gates III"@en ;  
    ex:chargedWith 
        ex:ForeignLobbying ,  
        ex:MoneyLaundering ,
        ex:TaxEvasion ;
    ex:pleadedGuilty 
        ex:Conspiracy, [
                a ex:Lying ;
                ex:wasLyingTo ex:FBI 
            ] .

ex:ForeignLobbying a ex:Offense .  
ex:MoneyLaundering a ex:Offense .  
ex:TaxEvasion a ex:Offense .

ex:investigation_162 a ex:Indictment ;
    ex:american "true" ;
    ex:cp_date "2018-02-23"^^xsd:date ;
    ex:cp_days 282 ;
    ex:indictment_days 166 ;
    ex:investigation ex:russia ;
    ex:investigation_days 659 ;
    ex:investigation_end "unknown" ;
    ex:investigation_start "2017-05-17"^^xsd:date ;
    foaf:name "Rick Gates" ;
    ex:investigatedPerson ex:Rick_Gates ;
    ex:outcome ex:guilty_plea ;
    ex:overturned false ;
    ex:pardoned false ;
    ex:president ex:Donald_Trump .'''

data_graph.parse(data=turtle_data, format='ttl')

shacl_graph = Graph()
shacl_graph.parse(
    "../09_SHACL_Constraints/shacl.ttl", format="ttl"
)

results = validate(
    data_graph,
    shacl_graph=shacl_graph,
    inference='both'
)

(conforms, results_graph, results_text) = results

print(results_text)
print(results_graph)
print(conforms)
