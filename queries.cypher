//El id del usuario y sus seguidores de los 5 usuarios con más seguidores.

MATCH ()<-[r:SIGUE_A]-(u:Node)
With u,count(r) as seguidores
Return u.id,seguidores
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