from rdflib import Graph
from pprint import pprint
update_str = """
    
"""
g = Graph()
g.parse(source = "../data/Russia_investigation_kg.ttl")

# result1 = g.query("""
#     PREFIX ex: <http://example.org/>
#     PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#     PREFIX schema: <https://schema.org/>
#
#     SELECT ?p
#     WHERE {
#         ?s?p?o
#     }""")

presidents = {}
result3 = g.query(f"""
PREFIX ex: <http://example.org#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <https://schema.org/>

select ?name ?president
where {{
    ?indictment a ex:Indictment ;
                ex:name ?name ;
                ex:president ?president .
                
}}
""")
presidents = {row[1]: [] for row in result3}

for row in result3:
    if row[0] not in row[1]:
        presidents[row[1]].append(row[0])


# pprint([r for r in pardons])
# pprint(presidents)




