# TC3041-P3-Primavera-2019
Orientaciones para la Práctica 3. Graph databases

## 0. Pre-requisitos
* Tener instalado `docker`. Mas información se encuentra disponible en [Docker](https://www.docker.com/community-edition).
* Acceso a Internet.
* Clonar este repositorio.

## 1. Levantar un contenedor con neo4j
`docker run --name=neo4j -m=4g --publish=7474:7474 --publish=7687:7687 --volume=$HOME/neo4j/data:/data --env=NEO4J_AUTH=none neo4j`

## 2. Copiar los datos al contenedor
1. Cámbiese a la carpeta de Data.
2. `docker cp nodeID.csv neo4j:/var/lib/neo4j/import/nodeID.csv`
3. `docker cp twitter_combined.csv neo4j:/var/lib/neo4j/import/twitter_combined.csv`

## 3. Importar los datos a la base de datos.
1. Acceda a la interfaz web de la aplicación en un browser en la URL:

[http://localhost:7474](http://localhost:7474)

2. `USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:/nodeID.csv" AS row
CREATE (:Node {nodeID: toInt(row.nodeId)});`

3. `CREATE INDEX ON :Node(nodeID);`

4. `USING PERIODIC COMMIT 
LOAD CSV WITH HEADERS FROM "file:/twitter_combined.csv" AS row
MATCH (start:Node {nodeID: toInt(row.StartId)})
MATCH (end:Node {nodeID: toInt(row.EndId)})
MERGE (start)-[:SIGUE_A]->(end);`



