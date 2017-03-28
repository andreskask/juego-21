import random

def inicio(): #ejecutable del programa
	print "iniciando"
	mostrarCartas(True, [], [])
	continuar()

def suma(cartas): #suma las cartas teniendo en cuenta la J, Q , K, y los A solo cuentan como 11 si no se pasa de 21
	if len(cartas) == 0:
		return 0
	else:
		if (cartas[len(cartas) - 1])[0] == "A":
			if suma(cartas[:-1]) > 10:
				return suma(cartas[:-1]) + 1
			else:
				return suma(cartas[:-1]) + 11
		elif (cartas[len(cartas) - 1])[0] == "J" or (cartas[len(cartas) - 1])[0] == "Q" or (cartas[len(cartas) - 1])[0] == "K" or (cartas[len(cartas) - 1])[0] == "1" or (cartas[len(cartas) - 1])[1] == "0":
			return suma(cartas[:-1]) + 10
		else:
			return suma(cartas[:-1]) + int((cartas[len(cartas) - 1])[0])

def mostrar(mazo): #retorna una cadena de texto de una lista de cadenas en linea
	if len(mazo) == 1:
		return mazo[0]
	else:
		return mazo[0] + ", " + mostrar(mazo[1:])
		
def cartaCasa(condicion, cartasC): #devuelve una carta o 2 dependiendo de la condicion para la casa
	cartasC.append(darCarta(cartasC))
	if condicion:
		cartasC.append(darCarta(cartasC))
	return cartasC
	
def cartaJugador(condicion, cartasJ): #devuelve una carta o 2 dependiendo de la condicion para el jugador
	cartasJ.append(darCarta(cartasJ))
	if condicion:
		cartasJ.append(darCarta(cartasJ))
	return cartasJ

def darCarta(cartas): #elije una carta aleatoria y la declara como usada. luego retorna esa carta
	return mazo(1, [])[cartaUsada(random.randint(0, 52), cartas)]
	
def cartaUsada(carta, cartas): #recibe un numero y en el arreglo de cartas usadas anade esa carta
	if len(cartas) > 0:
		if mazo(1, [])[carta] in cartas:
			return cartaUsada(random.randint(0, 52), cartas)
		else:
			return carta
	else:
		return carta

def mazo(n, cartas): #inicializa el arreglo de cartas creando todo el mazo
    if n == 1:
        cartas.append("A de corazones")
        return mazo(n + 1, cartas)
    elif n == 14:
        cartas.append("A de diamante")
        return mazo(n + 1, cartas)
    elif n == 27:
        cartas.append("A de picas")
        return mazo(n + 1, cartas)
    elif n == 40:
        cartas.append("A de trebol")
        return mazo(n + 1, cartas)
    elif n == 11:
        cartas.append("J de corazones")
        return mazo(n + 1, cartas)
    elif n == 24:
        cartas.append("J de diamante")
        return mazo(n + 1, cartas)
    elif n == 37:
        cartas.append("J de picas")
        return mazo(n + 1, cartas)
    elif n == 50:
        cartas.append("J de trebol")
        return mazo(n + 1, cartas)
    elif n == 12:
        cartas.append("Q de corazones")
        return mazo(n + 1, cartas)
    elif n == 25:
        cartas.append("Q de diamante")
        return mazo(n + 1, cartas)
    elif n == 38:
        cartas.append("Q de picas")
        return mazo(n + 1, cartas)
    elif n == 51:
        cartas.append("Q de trebol")
        return mazo(n + 1, cartas)
    elif n == 13:
        cartas.append("K de corazones")
        return mazo(n + 1, cartas)
    elif n == 26:
        cartas.append("K de diamante")
        return mazo(n + 1, cartas)
    elif n == 39:
        cartas.append("K de picas")
        return mazo(n + 1, cartas)
    elif n == 52:
        cartas.append("K de trebol")
        return mazo(n + 1, cartas)
    elif n > 1 and n < 11:
        cartas.append(str(n) + " de corazones")
        return mazo(n + 1, cartas)
    elif n > 14 and n <= 23:
        cartas.append(str(n - 13) + " de diamante")
        return mazo(n + 1, cartas)
    elif n > 26 and n <= 36:
        cartas.append(str(n - 26) + " de picas")
        return mazo(n + 1, cartas)
    elif n > 39 and n <= 49:
        cartas.append(str(n - 39) + " de trebol")
        return mazo(n + 1, cartas)
    else:
        return cartas

def heuristicaCasa(cartasCasa, cartasJugador):
	if suma(cartasCasa) < 21:
		cartaCasa(False, cartasCasa)
		heuristicaCasa(cartasCasa, cartasJugador)
	else:
		finalizacion(cartasCasa, cartasJugador)
		comparar(suma(cartasCasa), suma(cartasJugador))

def solicitarCarta(): #es el metodo que pregunta al jugador si desea pedir carta, retorna true si quiere carta
	if raw_input("desea solicitar carta?\ns = si\nn = no\n") == "s":
		return True
	else:
		return False

def finalizacion(cartasCasa, cartasJugador):
	print "cartas de la casa: [ " + mostrar(cartasCasa) + "]"
	print "el total de la casa es: " + str(suma(cartasCasa))
	print "cartas del jugador: [ " + mostrar(cartasJugador) + "]"
	print "el total del jugador es: " + str(suma(cartasJugador))

def comparar(casa, jugador):
	if jugador > casa:
		print "felicidades, usted gano"
	elif casa > jugador and casa <= 21:
		print "lo siento, usted perdio"
	elif casa == jugador:
		print "ha sido un empate, pero la casa gana"
	else:
		print "felicidades, usted gano"

def continuar():
	if raw_input("\ndesea jugar de nuevo?:\ns = si\nn = no\n") == "s":
		inicio()
	else:
		raw_input("el juego ha terminado, enter para salir")
		

def mostrarCartas(cartaAdicional, cartasTayador, cartasJugador): #maneja todo lo que se muestra en la consola
	print "cartas de la casa: [ " + cartaCasa(cartaAdicional, cartasTayador)[0] + ", * ]"
	print "cartas del jugador: [ " + mostrar(cartaJugador(cartaAdicional, cartasJugador)) + " ]"
	print "la suma de sus cartas es: " + str(suma(cartasJugador))
	if suma(cartasJugador) < 21:
		if solicitarCarta():
			mostrarCartas(False, cartasTayador, cartasJugador)
		else:
			heuristicaCasa(cartasTayador, cartasJugador)
	elif suma(cartasJugador) == 21:
		heuristicaCasa(cartasTayador, cartasJugador)
	else:
		print "lo siento, la suma de sus cartas es mayor que 21\nusted pierde"

inicio()