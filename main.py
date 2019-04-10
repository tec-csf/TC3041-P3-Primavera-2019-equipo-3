from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=None)


def main(tx):
    print("Bienvenido a Twitter")
    while True:
        print("¿Qué desea hacer?")
        print("1. ¿A quiénes sigues?")
        print("2. ¿A cuántos usuarios sigue Justin Bieber?")
        print("3. ¿Los 5 usuarios con más seguidores?")
        print("4. Salir")
        n = int(input("Escoge un número: ")) 
        if n == 4:
            break 
        else:
            if n==1:
                for record in tx.run("MATCH (a:Node {nodeID: 460282402})"
                                    "MATCH(m)"
                                    "MATCH (a)-[r:SIGUE_A]->(m)"
                                    "RETURN m.nodeID" ):
                    print(record["m.nodeID"])
                

            elif n==2:
                for record in tx.run("MATCH (n:Node {nodeID: 285312927})"
                                        "MATCH(m)"
                                        "MATCH (n)-[r:SIGUE_A]->(m)"
                                        "RETURN count(r) "):
                    print("Seguidores: ",record["count(r)"],'\n')

            elif n==3:
                for record in tx.run("MATCH ()-[r:SIGUE_A]->(u:Node)" "RETURN u.nodeID,count(r) Order By count(r) DESC Limit 5"):
                    print("Usuario: ",record["u.nodeID"],"\tSeguidores: ",record["count(r)"])    

with driver.session() as session:
    session.read_transaction(main) 



