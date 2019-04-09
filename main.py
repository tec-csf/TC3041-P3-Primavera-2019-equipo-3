

from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=None)


def main(tx):
    n=1
    if n == 1:
        for record in tx.run("MATCH (a:Node {nodeID: '285312927'})"
                            "MATCH(m)"
                            "MATCH (a)-[r:RELATION]->(m)"
                            "RETURN m" ):
            print("hey",record["m"])

    elif n == 2:
        for record in tx.run("MATCH (n:Node {nodeID: '285312927'})"
                                "MATCH(m)"
                                "MATCH (n)-[r:RELATION]->(m)"
                                "RETURN count(r) "):
            print(record["count(r)"])

    elif n == 3:
        for record in tx.run("MATCH ()<-[r:RELATION]-(u:Node)"
                                "With u,count(r) as seguidores"
                                "Return u.nodeID,seguidores"
                                "Order By seguidores DESC"
                                "Limit 5 "
                                ):
            print(record["u.nodeID"])

with driver.session() as session:
    session.read_transaction(main)
