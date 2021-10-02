# -*- coding: utf-8 -*-
# -- coding: utf-8 --
# Juliana Henao - Igor Ariza - Santiago Gutierrez.
# Profesor: Andres Mauricio Valencia Restrepo
#Librerias
import os
import pandas as pd
import mysql.connector #Base de datos

#Archivos proyecto
from morse import encrypt, decrypt
from murcielago import encrypt_m, decrypt_m

mydb=mysql.connector.connect(host="localhost",user="root",passwd="admin")
mycursor=mydb.cursor()
mycursor.execute("USE encrypted")
mycursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS message (id INT AUTO_INCREMENT PRIMARY KEY, message VARCHAR(255), encrypted VARCHAR(255), type VARCHAR(255), email VARCHAR(255))")

Cant_usuarios = 0
usuarios = [[]]

def registro_datos():
    os.system('clear') # NOTA para windows tienes que cambiar clear por cls
    #Entradas
    print("******* REGISTRO DE USUARIO ******* \n")
    nombre_usuario = input("Nombres: ")
    email_usuario = input("Email :")
    contin_dat = input("¿Seguro de tus datos digitados? S: Si, N: No: ")
    if contin_dat == 'S' or contin_dat == 's':
      #Almacenamiento local
       usuario = [nombre_usuario, email_usuario]
       usuarios[Cant_usuarios].append(usuario)
      #Almacenamiento Base de datos
       sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
       val = (nombre_usuario, email_usuario)
       mycursor.execute(sql, val)
       mydb.commit()
       print(mycursor.rowcount, "usuario ingresado a la base de datos.") 
       input("******* Presione cualquier tecla para continuar *******")
       #Incremento
       Cant_usuarios + 1
    else:
       main()

def listado_usuarios():
    os.system('clear') # NOTA para windows tienes que cambiar clear por cls
    mycursor.execute("SELECT * FROM users")
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
    input("\n******* Presione cualquier tecla para continuar *******")
    main()

def consulta_bd_message():
    os.system('clear') # NOTA para windows tienes que cambiar clear por cls
    mycursor.execute("SELECT * FROM message")
    myresult = mycursor.fetchall()
    #for x in myresult:
    print("resultados: ", myresult)
    input("\n******* Presione cualquier tecla para continuar *******")
    main()

def encryptedOption():
    os.system('clear') # NOTA para windows tienes que cambiar clear por cls
    print("******* SELECCIONA EL TIPO DE ENCRIPTADO QUE DESEAS UTILIZAR ******* \n")
    print("Por favor, digite el número de su elección: \n")
    print("\t [1] MORSE")
    print("\t [2] MUCIELAGO")
    print("\t [3] BINARIO")
    print("\t [0] REGRESAR  \n")
    opcionMenu = input("Seleccione una opción >> ")
    if opcionMenu == "1":
      encryptedMorse()

def consultaEmail():
    os.system('clear') # NOTA para windows tienes que cambiar clear por cls
    emailDecryp = input("\nIngresa tu Email para consultar tus registros realizados: ")
    query= "SELECT * FROM users WHERE email=%s"
    myresult = mycursor.execute(query,(emailDecryp,))
    #for x in myresult:
    print(myresult, emailDecryp)

    num_message = input("\nIngresa el numero del mensaje a desencriptar >> ")
    sqlII = "SELECT encrypted FROM message WHERE id=%s"
    mycursor.execute(sqlII,num_message)
    myresultII = mycursor.fetchall()
    decipher = decrypt(myresultII)
    print("\nMensaje descifrado: " + decipher)
    encryptedMorse()


def encryptedMorse():
    os.system('clear') # NOTA para windows tienes que cambiar clear por cls
    print("******* ¿Qué deseas realzar? ******* \n")
    print("Por favor, digite el número de su elección: \n")
    print("\t [1] ENCRIPTAR")
    print("\t [2] DESENCRIPTAR")
    print("\t [3] CONSULTAR")
    print("\t [0] REGRESAR  \n")
    opcionMenu = input("Selecciona la opción >> ")
    if opcionMenu == "1":
      type= "MORSE"
      print("******* ENCRIPTADO MORSE ******* \n")
      message = input("Ingrese el mensaje que desea encriptar >> ")
      cipher = encrypt(message)
      print("\nMensaje ingresado: " + message)
      print("\nMensaje encriptado: " + cipher)
      opcionGuardar = input("\n¿Deseas guardar la información en la base de datos? S: Si, N: No:")
      if opcionGuardar == 'S' or opcionGuardar == 's':
       opcionEmail = input("\nIngresa tu Email")
       sql = "INSERT INTO message (message, encrypted, type, email) VALUES (%s, %s, %s, %s)"
       val = (message, cipher, type, opcionEmail)
       mycursor.execute(sql, val)
       mydb.commit()
       print(mycursor.rowcount, "Mensaje Ingresado con el email: ", opcionEmail)
       input("\n******* Presione cualquier tecla para continuar *******")
       encryptedMorse()
    elif opcionMenu == "2":
        consultaEmail()
    else:
       main()



def main():
  os.system('clear') # NOTA para windows tienes que cambiar clear por cls

  print("******* BIENVENIDO AL SISTEMA DE ENCRYPTACIÓN DE PYTHON ******* \n")
  print('\t 1 - Registro de usuario')
  print('\t 2 - Listado usuarios')
  print('\t 3 - Consultar registros')
  print('\t 4 - Usar encryptación')
  print('\t 9 - salir')

while True:
	# Mostramos el menu
	main()
	# solicitamos una opción al usuario
	opcionMenu = input("Seleccione una opción >> ")
          
	if opcionMenu == "1":
		print ("")
		registro_datos()
	elif opcionMenu == "2":
		listado_usuarios()
		input("")
	elif opcionMenu == "3":  
		#email=input("Ingresa el email del usuario a consultar... pulsa una tecla para consutar todos los registros en la base de datos")
		consulta_bd_message()
	elif opcionMenu=="4":
		encryptedOption()
	elif opcionMenu=="9":
		os.system('clear')
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

if __name__ == '__main__':
    main()