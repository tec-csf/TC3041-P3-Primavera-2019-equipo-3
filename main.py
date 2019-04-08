

from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=None)


def main(tx):
    for record in tx.run("MATCH (a:Node {nodeID: 285312927})"
                         "MATCH(m)"
                        "MATCH (a)-[r:SIGUE_A]->(m)"
                         "RETURN m" ):
        print("hey",record["m"])

    for record in tx.run("MATCH (n:Node {nodeID: 285312927})"
                            "MATCH(m)"
                            "MATCH (n)-[r:SIGUE_A]->(m)"
                            "RETURN count(r) "):
        print(record["count(r)"])

    
    for record in tx.run("MATCH ()<-[r:SIGUE_A]-(u:Node)"
                            "With u,count(r) as seguidores"
                            "RETURN u.nodeID, seguidores"
                            "Order By seguidores DESC"
                            "Limit 5 "
                            ):
        print(record["u.nodeID"])
        
with driver.session() as session:
    session.read_transaction(main)
