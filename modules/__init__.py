def dir_estadisticas(jugadores,goles_favor,goles_evitados,asistencias):
    estadisticas = {}
    for jugador, goles_favor, goles_evitados, asistencias in zip(jugadores, goles_favor, goles_evitados, asistencias):

        estadisticas[jugador] = (goles_favor, goles_evitados, asistencias)
    return estadisticas

def max_goleadores(jugadores):
    goals_max = max(map(lambda x: x[0], jugadores.values()))
    top_scorer = next(jugador for jugador, goles in jugadores.items() if goles[0] == goals_max)

    return goals_max,top_scorer   



def jugador_influyente(jugadores):

    max_puntos = max(map(lambda x: x[0]*1.5 + x[1]*1.25 + x[2], jugadores.values()))

    top_player = next(jugador for jugador, goles in jugadores.items() if goles[0]*1.5 + goles[1]*1.25 + goles[2] == max_puntos)
    return max_puntos, top_player


def goal_average(goals_scored):    
    average = (sum(goals_scored))/25   
    return average

def top_scorer_average(goles):
    return goles/25