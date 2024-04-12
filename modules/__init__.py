def dir_estadisticas(jugadores,goles_favor,goles_evitados,asistencias):

    estadisticas={}
    for i,jugador in enumerate(jugadores):
        estadisticas[jugador]=(goles_favor[i],goles_evitados[i],asistencias[i])
    return estadisticas
