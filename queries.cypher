//El id del usuario y el # de seguidores de los 5 usuarios con más seguidores.

MATCH ()-[r:SIGUE_A]->(u:Node)
With u,count(r) as seguidores
Return u.nodeID,seguidores
Order By seguidores DESC
Limit 5

//Dado un usuario checar los usuarios que el sigue pero no le dieron followback.

MATCH (u:Node {nodeID:18581803})-[r:SIGUE_A]->(u2:Node)
Where NOT (u2)-[:SIGUE_A]->(u)
Return u2.nodeID
Limit 10

//