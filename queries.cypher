//El id del usuario y sus seguidores de los 5 usuarios con más seguidores.

MATCH ()<-[r:SIGUE_A]-(u:Node)
With u,count(r) as seguidores
Return u.nodeID,seguidores
Order By seguidores DESC
Limit 5