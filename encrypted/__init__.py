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
from murcielago import Encode_M, Decode_M
from binario import cipher_encrypt, cipher_decrypt

mydb=mysql.connector.connect(host="localhost",user="root",passwd="admin")
mycursor=mydb.cursor()
mycursor.execute("USE encrypted")
mycursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS message (id INT AUTO_INCREMENT PRIMARY KEY, message VARCHAR(255), encrypted VARCHAR(255), type VARCHAR(255), email VARCHAR(255))")

Cant_usuarios = 0
tipo= " "
usuarios = [[]]
decipher=""

def registro_datos():
    os.system('cls') # NOTA para windows tienes que cambiar cls por cls
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
    os.system('cls') # NOTA para windows tienes que cambiar cls por cls
    mycursor.execute("SELECT * FROM users")
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
    input("\n******* Presione cualquier tecla para continuar *******")
    main()

def consulta_bd_message():
    os.system('cls') # NOTA para windows tienes que cambiar cls por cls
    mycursor.execute("SELECT * FROM message")
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
    input("\n******* Presione cualquier tecla para continuar *******")
    main()

def encryptedOption():
    os.system('cls') # NOTA para windows tienes que cambiar cls por cls
    print("******* SELECCIONA EL TIPO DE ENCRIPTADO QUE DESEAS UTILIZAR ******* \n")
    print("Por favor, digite el número de su elección: \n")
    print("\t [1] MORSE")
    print("\t [2] MURCIELAGO")
    print("\t [3] BINARIO")
    print("\t [0] REGRESAR  \n")
    opcionMenu = input("Seleccione una opción >> ")
    if opcionMenu == "1":
      encryptedMorse()
    elif opcionMenu == "2":
      encryptedMurcielago()
    elif opcionMenu == "3":
      encryptedBinario()
    else:
       main()

def encryptedMurcielago():
    os.system('cls') # NOTA para windows tienes que cambiar cls por cls
    tipo= "MURCIELAGO"
    print("******* ¿Qué deseas realzar? ******* \n")
    print("Por favor, digite el número de su elección: \n")
    print("\t [1] ENCRIPTAR")
    print("\t [2] DESENCRIPTAR")
    print("\t [3] CONSULTAR")
    print("\t [0] REGRESAR  \n")
    opcionMenu = input("Selecciona la opción >> ")
    if opcionMenu == "1":      
      print("******* ENCRIPTADO MURCIELAGO ******* \n")
      message_m = input("Ingrese el mensaje que desea encriptar >> ")
      cipher_m = Encode_M(message_m)
      print("\nMensaje ingresado: " + message_m)
      print("\nMensaje encriptado: " + cipher_m)
      opcionGuardar = input("\n¿Deseas guardar la información en la base de datos? S: Si, N: No:")
      if opcionGuardar == 'S' or opcionGuardar == 's':
       opcionEmail = input("\nIngresa tu Email")
       sql = "INSERT INTO message (message, encrypted, type, email) VALUES (%s, %s, %s, %s)"
       val = (message_m, cipher_m, tipo, opcionEmail)
       mycursor.execute(sql, val)
       mydb.commit()
       print(mycursor.rowcount, "Mensaje Ingresado con el usuario: ", opcionEmail)
       input("\n******* Presione cualquier tecla para continuar *******")
       encryptedMurcielago()
    elif opcionMenu == "2":
        consultaEmail(tipo)
    elif opcionMenu == "3":
        consultaEncrypted(tipo)
    else:
       main()

def encryptedBinario():
    os.system('cls') # NOTA para windows tienes que cambiar cls por cls
    tipo= "BINARIO"
    print("******* ¿Qué deseas realzar? ******* \n")
    print("Por favor, digite el número de su elección: \n")
    print("\t [1] ENCRIPTAR")
    print("\t [2] DESENCRIPTAR")
    print("\t [3] CONSULTAR")
    print("\t [0] REGRESAR  \n")
    opcionMenu = input("Selecciona la opción >> ")
    if opcionMenu == "1":      
      print("******* ENCRIPTADO BINARIO ******* \n")
      message_b = input("Ingrese el mensaje que desea encriptar >> ")
      cipher_b = cipher_encrypt(message_b, 3)
      print("\nMensaje ingresado: " + message_b)
      print("\nMensaje encriptado: " + cipher_b)
      opcionGuardar = input("\n¿Deseas guardar la información en la base de datos? S: Si, N: No:")
      if opcionGuardar == 'S' or opcionGuardar == 's':
       opcionEmail = input("\nIngresa tu Email: ")
       sql = "INSERT INTO message (message, encrypted, type, email) VALUES (%s, %s, %s, %s)"
       val = (message_b, cipher_b, tipo, opcionEmail)
       mycursor.execute(sql, val)
       mydb.commit()
       print(mycursor.rowcount, "Mensaje Ingresado con el usuario: ", opcionEmail)
       input("\n******* Presione cualquier tecla para continuar *******")
       encryptedBinario()
    elif opcionMenu == "2":
       consultaEmail(tipo)
    elif opcionMenu == "3":
       consultaEncrypted(tipo)
    else:
       main()

def consultaEmail(types):
    os.system('cls') # NOTA para windows tienes que cambiar cls por cls
    emailDecryp = input("\nIngresa tu Email para consultar tus registros realizados: ")
    query = "SELECT * FROM message WHERE email=%s"
    mycursor.execute(query,(emailDecryp, ))
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
    num_message = input("\nIngresa el numero del mensaje a desencriptar >> ")
    sql = "SELECT encrypted FROM message WHERE id=%s and type=%s"
    mycursor.execute(sql,(num_message, types,))
    myresultII = mycursor.fetchall()
    if types == "MORSE":
      decipher = decrypt(myresultII[0][0])
      print("\nMensaje descifrado: ", decipher)
      input("\n******* Presione cualquier tecla para continuar *******")
      encryptedMorse()
    elif types == "MURCIELAGO":
      decipher = Decode_M(myresultII[0][0])
      print("\nMensaje descifrado: ", decipher)
      input("\n******* Presione cualquier tecla para continuar *******")
      encryptedMurcielago()
    elif types == "BINARIO":
      decipherb = cipher_decrypt(myresultII[0][0], 3)
      print("\nMensaje descifrado: ", decipherb)
      input("\n******* Presione cualquier tecla para continuar *******")
      encryptedBinario()
    


def encryptedMorse():
    os.system('cls') # NOTA para windows tienes que cambiar cls por cls
    tipo= "MORSE"
    print("******* ¿Qué deseas realzar? ******* \n")
    print("Por favor, digite el número de su elección: \n")
    print("\t [1] ENCRIPTAR")
    print("\t [2] DESENCRIPTAR")
    print("\t [3] CONSULTAR")
    print("\t [0] REGRESAR  \n")
    opcionMenu = input("Selecciona la opción >> ")
    if opcionMenu == "1":      
      print("******* ENCRIPTADO MORSE ******* \n")
      message = input("Ingrese el mensaje que desea encriptar >> ")
      cipher = encrypt(message)
      print("\nMensaje ingresado: " + message)
      print("\nMensaje encriptado: " + cipher)
      opcionGuardar = input("\n¿Deseas guardar la información en la base de datos? S: Si, N: No:")
      if opcionGuardar == 'S' or opcionGuardar == 's':
       opcionEmail = input("\nIngresa tu Email")
       sql = "INSERT INTO message (message, encrypted, type, email) VALUES (%s, %s, %s, %s)"
       val = (message, cipher, tipo, opcionEmail)
       mycursor.execute(sql, val)
       mydb.commit()
       print(mycursor.rowcount, "Mensaje Ingresado con el usuario: ", opcionEmail)
       input("\n******* Presione cualquier tecla para continuar *******")
       encryptedMorse()
    elif opcionMenu == "2":
        consultaEmail(tipo)
    elif opcionMenu == "3":
        consultaEncrypted(tipo)
    else:
       main()


def consultaEncrypted(tipo):
    os.system('cls') # NOTA para windows tienes que cambiar cls por cls
    sql = "SELECT * FROM message WHERE type=%s"
    mycursor.execute(sql,(tipo, ))
    myresultII = mycursor.fetchall()
    for x in myresultII:
      print(x)
    input("\n******* Presione cualquier tecla para continuar *******")
    if tipo == "MORSE":
      encryptedMorse()
    elif tipo == "MURCIELAGO":
      encryptedMurcielago()
    elif tipo == "BINARIO":
      encryptedBinario()


def main():
  os.system('cls') # NOTA para windows tienes que cambiar cls por cls

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
		os.system('cls')
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar ")
		main()

if __name__ == '__main__':
    main()