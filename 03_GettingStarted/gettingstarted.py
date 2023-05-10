from rdflib import Namespace, Graph
from functions import get_image

ex = Namespace("http://example.org/")
G = Graph()
G.bind("ex", ex)

donaldTrump = ex.Donald_Trump
paulManafort = ex.Paul_Manafort
rickGates = ex.Rick_Gates
georgePapadopoulos = ex.Goeorge_Papadopoulos
michaelFlynn = ex.Michael_Flynn
michaelCohen = ex.Michael_Cohen
rogerStone = ex.Roger_Stone

G.add((paulManafort, ex.businessPartner, rickGates))
G.add((paulManafort, ex.campaignChairman, donaldTrump))
G.add((paulManafort, ex.chargedWith, ex.MoneyLaundering))
G.add((paulManafort, ex.chargedWith, ex.TaxEvasion))
G.add((paulManafort, ex.chargedWith, ex.ForeignLobbying))
G.add((paulManafort, ex.convictedFor, ex.BankFraud))
G.add((paulManafort, ex.convictedFor, ex.TaxFraud))
G.add((paulManafort, ex.pleadGuilty, ex.Conspiracy))
G.add((paulManafort, ex.sentencedTo, ex.Prison))
G.add((paulManafort, ex.negotiated, ex.PleaAgreement))

G.add((rickGates, ex.pleadGuilty, ex.Conspiracy))
G.add((rickGates, ex.pleadGuilty, ex.LyingToFBI))

# Print different graph formats:
# print(G.serialize(format='ttl'))
# print(G.serialize(format='nt'))
# print(G.serialize(format='json-ld'))
# print(G.serialize(format='xml'))

# Lab2:
G.add((michaelCohen, ex.attorneyFor, donaldTrump))
G.add((michaelCohen, ex.pleadGuilty, ex.Lying_to_congress))
G.add((michaelFlynn, ex.adviser, donaldTrump))
G.add((michaelFlynn, ex.pleadGuilty, ex.Lying_to_FBI))
G.add((michaelFlynn, ex.negotiated, ex.Plea_agreement))


# Partial result of this lab:
G.serialize(destination="../data/lab_1.ttl", format="ttl")

# Total graph:
G.serialize(destination="../data/trumpInvestigation.ttl", format="ttl")

get_image(G)