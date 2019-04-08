#sudo docker run --name=neo4j -m=4g --publish=7474:7474 --publish=7687:7687 --volume=$HOME/neo4j/data:/data --env=NEO4J_AUTH=none neo4j

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