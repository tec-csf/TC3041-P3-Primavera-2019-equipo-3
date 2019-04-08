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
"""
from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=None)

def main(tx):
    for record in tx.run("MATCH (a:Node {nodeID: '285312927'})"
                         "MATCH(m)"
                        "MATCH (a)-[r:RELATION]-(m)"
                         "RETURN m" ):
        print(record["m"])

with driver.session() as session:
    session.read_transaction(main)