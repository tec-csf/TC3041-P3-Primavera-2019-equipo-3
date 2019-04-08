//El id del usuario y el # de seguidores de los 5 usuarios con más seguidores.

With u,count(r) as seguidores
Return u.nodeID,seguidores
Order By seguidores DESC
Limit 5


MATCH (a:Node {nodeID: '285312927'})
MATCH(m)
MATCH (a)-[r:RELATION]->(m)
RETURN m


MATCH (n:Node {nodeID: '285312927'})
MATCH(m)
MATCH (n)-[r:RELATION]->(m)
RETURN count(r)
//Dado un usuario checar los usuarios que el sigue pero no le dieron followback.

MATCH (u:Node {nodeID:18581803})-[r:SIGUE_A]->(u2:Node)
Where NOT (u2)-[:SIGUE_A]->(u)
Return u2.nodeID
Limit 10

//# de seguidos y seguidores de un usuario
MATCH (u:Node {nodeID:115485051})-[r:SIGUE_A]->(:Node)
With count(r) as seguidos
MATCH (u:Node {nodeID:115485051})<-[r2:SIGUE_A]-(:Node)
With seguidos,count(r2) as seguidores
Return seguidos,seguidores
