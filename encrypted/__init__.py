# -*- coding: utf-8 -*-
# -- coding: utf-8 --
# Juliana Henao - Igor Ariza - Santiago Gutierrez.
# Profesor: Andres Mauricio Valencia Restrepo
import os
import pandas as pd
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="admin")
mycursor=mydb.cursor()
#mycursor.execute("create database encrypted")

Cant_usuarios = 0
usuarios = [[]]

def registro_datos():
    #Entradas
    print("******* REGISTRO DE USUARIO ******* \n")
    nombre_usuario = input("Nombres: ")
    email_usuario = input("Email :")
    contin_dat = input("Seguro de tus datos digitados? S: Si, N: No: ")
    if contin_dat == 'S' or contin_dat == 's':
       usuario = [nombre_usuario, email_usuario]
       usuarios[Cant_usuarios].append(usuario)
       Cant_usuarios + 1
    else:
       registro_datos()

def listado_usuarios():

  df = pd.DataFrame(usuarios)
  print(df)

"""   for num in usuarios:
         print (num) """

def consulta_bd():
    listado_usuarios()

def encrypted():
    print("******* SELECCIONA EL TIPO DE ENCRIPTADO QUE DESEAS UTILIZAR ******* \n")
    print("Por favor, digite el número de su elección: \n")
    print("\t [1] MORSE")
    print("\t [2] MUCIELAGO")
    print("\t [3] ")
    print("\t [0] REGRESAR  \n")
    input("---")


def main():
  os.system('clear') # NOTA para windows tienes que cambiar clear por cls

  print("******* BIENVENIDO AL SISTEMA DE ENCRYPTACIÓN DE PYTHON ******* \n")
  print('\t 1 - Registro de usuario')
  print('\t 2 - Listado usuarios')
  print('\t 3 - Consultar registros por usuario (email)')
  print('\t 4 - Usar encrytpación')
  print('\t 9 - salir')

while True:
	# Mostramos el menu
	main()
	# solicituamos una opción al usuario
	opcionMenu = input("Seleccione una opción >> ")
          
	if opcionMenu == "1":
		print ("")
		registro_datos()
	elif opcionMenu == "2":
		listado_usuarios()
		input("")
	elif opcionMenu == "3":  
		email=input("Ingresa el email del usuario a consultar... pulsa una tecla para consutar todos los registros en la base de datos")
		consulta_bd()
	elif opcionMenu=="4":
		encrypted()
	elif opcionMenu=="9":
		os.system('clear')
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

if __name__ == '__main__':
    main()