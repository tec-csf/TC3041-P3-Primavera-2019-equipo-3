sudo docker run --name=neo4j -m=4g --publish=7474:7474 --publish=7687:7687 --volume=$HOME/neo4j/data:/data --env=NEO4J_AUTH=none neo4j

docker cp nodeID.csv neo4j:/var/lib/neo4j/import/nodeID.csv
docker cp twitter_combined.csv neo4j:/var/lib/neo4j/import/twitter_combined.csv

//Importamos los datos a neo4j
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:/nodeID.csv" AS row
CREATE (:Node {nodeID: toInt(row.nodeId)});

CREATE INDEX ON :Node(nodeID);

USING PERIODIC COMMIT 
LOAD CSV WITH HEADERS FROM "file:/twitter_combined.csv" AS row
MATCH (start:Node {nodeID: toInt(row.StartId)})
MATCH (end:Node {nodeID: toInt(row.EndId)})
MERGE (start)-[:SIGUE_A]->(end);