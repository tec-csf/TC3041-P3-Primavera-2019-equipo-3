//El id del usuario y sus seguidores de los 5 usuarios con más seguidores.

MATCH ()<-[r:SIGUE_A]-(u:Usuario)
With u,count(r) as seguidores
Return u.id,seguidores
Order By seguidores DESC
Limit 5