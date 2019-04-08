#sudo docker run --name=neo4j -m=4g --publish=7474:7474 --publish=7687:7687 --volume=$HOME/neo4j/data:/data --env=NEO4J_AUTH=none neo4j

"""
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:/nodeID.csv" AS row
CREATE (:Node {nodeID: row.nodeId});

CREATE INDEX ON :Node(nodeID);

USING PERIODIC COMMIT 
LOAD CSV WITH HEADERS FROM "file:/twitter_combined.csv" AS row
MATCH (start:Node {nodeID: row.StartId})
MATCH (end:Node {nodeID: row.EndId})
MERGE (start)-[:RELATION]->(end);


MATCH (n:Node {nombre: 'Dianna'})
MATCH(m)
MATCH (n)-[r:CONOCE_A]->(m)
RETURN count(r)


MATCH (a:Node {nodeID: '285312927'})
MATCH(m)
MATCH (a)-[r:RELATION]-(m)
RETURN m
"""
from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=None)

def main(tx):
    for record in tx.run("MATCH (a:Node {nodeID: '285312927'})"
                         "MATCH(m)"
                        "MATCH (a)-[r:RELATION]->(m)"
                         "RETURN m" ):
        print("hey",record["m"])

    for record in tx.run("MATCH (n:Node {nodeID: '285312927'})"
                            "MATCH(m)"
                            "MATCH (n)-[r:RELATION]->(m)"
                            "RETURN count(r) "):
        print(record["count(r)"])


    for record in tx.run("MATCH ()<-[r:RELATION]-(u:Node)"
                            "With u,count(r) as seguidores"
                            "Return u.nodeID,seguidores"
                            "Order By seguidores DESC"
                            "Limit 5 "
                            ):
        print(record["u.nodeID"])

with driver.session() as session:
    session.read_transaction(main)