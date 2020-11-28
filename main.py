#listar paises de los que queremos horas
import datetime
import os
now = None
zone = None
especifico= None

def tiempoactual(pais):
  global now
  now=datetime.datetime.now(zone)
  now=now.strftime("%X")
  print("La hora en " +pais+ " es: " +now)
  print()

 
def tiempoespecifico(pais):
  now2=datetime.datetime.now()
  #global now
  #hora=input("Indica la hora en formato hh:mm:ss: ")
  now=datetime.datetime.strptime(input("Indica la hora en formato hh:mm:ss: "),"%X")

  #now=datetime.datetime.strptime(hora,"%X")

  #now=now(zone)
  now=now.strftime("%X")


  #now2=now2.strftime("%x")
  #print(now2)


  print("La hora en " +pais+ " es: " +now)
  print()

def zona(zona):
  global zone
  zone= datetime.timezone(datetime.timedelta(hours=zona))

def inicio():
  global especifico
  while True:
  #os.system ("clear")
    print("Selecciona una opcion")
    print("1. Hora Actual")
    print("2. Especifica Hora")
    print("3. Salir")
    try:
      operacion = int(input("Indique la opcion: "))
    except ValueError:
      print("El valor introducido es erroneo")
    else:
      if operacion== 1:
        especifico=1
        segundo()
      elif operacion== 2:
        especifico=2
        segundo()
      elif operacion== 3:
        break
  os.system ("clear")   

def segundo():
  while True:
    #os.system ("clear")
    print("Estas son las operaciones que puedes realizar")
    print("1. Hora de España")
    print("2. Hora de Lima")
    print("3. Hora de Hongkong")
    print("4. Todas las horas")
    print("5. Salir")
    try:
      operacion = int(input("Indique la opcion: "))
    except ValueError:
      print("El valor introducido es erroneo")
    else:
      if operacion== 1:
        zona(1)
        if especifico==1:
          tiempoactual("Spain")
        else:
            tiempoespecifico("Spain")
      elif operacion== 2:
        zona(-5)
        if especifico==1:
          tiempoactual("Lima")
        else:
            tiempoespecifico("Lima")
      elif operacion== 3:
        zona(8)
        if especifico==1:
          tiempoactual("Hong Kong")
        else:
            tiempoespecifico("Hong Kong")
      elif operacion== 4:
        tiempoactual(1)
      elif operacion== 5:
        break
  os.system ("clear") 
  salir()

def salir():
  print("Gracias por usar nuestra app")

# O usar lista_articulos = list[]
print("---------------------------------------------")
print("---------------------------------------------")
print("------  BIENVENIDO AL RELOJ DEL MUNDO    ----")
print("---------------------------------------------")
print("---------------------------------------------")
inicio()

