import random
import time

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

puntaje = 0

iniciar_trivia = True
intentos = 0

print(BLUE + "Bienvenido a mi trivia sobre museos Lambayecanos" + RESET)

print("Pondremos a prueba cuánto sabes")

nombre = input(MAGENTA + "Ingresa tu nombre: " + RESET)

print("\n Hola" + BLUE,nombre ,RESET +"responde las siguientes preguntas escribiendo y presionando 'Enter' para enviar tu respuesta\n")

print("Tienes"+ BLUE, puntaje, RESET + "puntos \n")

#for numero_carga in range(5,0,-1):
  #print(numero_carga)
  #time.sleep(1)

while iniciar_trivia == True:
  intentos += 1
  puntaje = 0

  print( "\nIntento numero: ", intentos)
  input("Presiona Enter para continuar")

  print(BLUE + "1) Quien fue el descubridor del Señor de Sipán?" + RESET)
  print("a) Walter Alva")
  print("b) Ruth Shady")
  print("c) Julio C. Tello")
  print("d) Luis Lumbreras")

  respuesta_1 = input(MAGENTA + "\n Tu respuesta: "+ RESET)

  while respuesta_1 not in ("a","b", "c","d", "z"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_1 == "b":
    puntaje -= 5
    print("Incorrecto")
  elif respuesta_1 == "c":
    puntaje += 5
    print("...")
  elif respuesta_1 == "d":
    puntaje / 2
    print("Totalmente incorrecto")
  elif respuesta_1 == "z":
    puntaje += 1000
    print("Esta respuesta es secreta obtuviste un super puntaje")
  else:
    puntaje * 2
    print(BLUE + "Correcto" , MAGENTA + "Walter Alva"+ RESET, "es el descubridor del Señor de Sipán")
  
  print("\n Gracias" + BLUE, nombre, RESET + "por jugar mi trivia, alcanzaste" + BLUE, puntaje, RESET +"puntos\n")

  time.sleep(2)
  print("Jugando...")
  time.sleep(1)

  print(BLUE + "2) Cual es la fecha de fundacion del Museo de Tucume?" + RESET)
  print("a) 15 de agosto 1994")
  print("b) 20 de agosto 1992")
  print("c) 24 de diciembre 2000")
  print("d) 01 de junio de 1990")

  respuesta_2 = input(MAGENTA + "\n Tu respuesta: " + RESET)

  while respuesta_2 not in ("a","b", "c","d", "ñ"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    
  if respuesta_2 == "a":
    puntaje -= 5
    print("...")
  elif respuesta_2 == "c":
    puntaje / 2
    print("Totalmente incorrecto")
  elif respuesta_2 == "d":
    puntaje -= 10
    print("Incorrecto")
  elif respuesta_2 == "ñ":
    puntaje += 1000
    print("Esta respuesta es secreta obtuviste un super puntaje")
  else:
    puntaje * 2
    print(BLUE + "Correcto" + RESET, "La fecha de fundacion es ", MAGENTA +"20 de agosto 1992" + RESET)
  
  print("\n Gracias"+ BLUE, nombre, RESET + "por jugar mi trivia, alcanzaste" + BLUE, puntaje, RESET + "puntos\n")
  
  time.sleep(2)
  print("Jugando...")
  time.sleep(1)
  
  print(BLUE + "3) Donde fue descubierta la tumba del Señor de Sicán?" + RESET)
  print("a) Huaca de la Pava Aliblanca")
  print("b) Huaca del Oro")
  print("c) Huaca de barro")
  print("d) Huaca de la Luna")
  
  respuesta_3 = input("\n Tu respuesta: ")
  
  while respuesta_3 not in ("a","b", "c","d", "h"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_3 == "a":
    puntaje / 2
    print("Totalmente incorrecto")
  elif respuesta_3 == "c":
    puntaje += 5
    print("Incorrecto")
  elif respuesta_3 == "d":
    puntaje -= 5
    print("...")
  elif respuesta_3 == "h":
    puntaje += 1000
    print("Esta respuesta es secreta obtuviste un super puntaje")
  else:
    puntaje * 2
    print(BLUE + "Correcto", RESET + "La tumba del Señor de Sican fue descubierto en ", MAGENTA + "Huaca del Oro" + RESET)
  
  time.sleep(2)
  print("Jugando...")
  time.sleep(1)
  
  puntajeFinal = random.randint(0,1000)
  
  print("\n Gracias"+ BLUE, nombre, RESET + "por jugar mi trivia, en total alcanzaste"+ BLUE, puntajeFinal, RESET+"puntos\n")
    #time.sleep(1)

  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si":  # != significa "distinto"
   print("\nEspero", nombre, "que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.


