user = "BCC-2215"
password = "225125"
#iniciamos el ciclo while
while True:
    print("ingrese su usuario tiene 3 intentos: ")
    usuario=input()
    print("ingrese su contraseña: ")
    passw=input()
     #verificamos si el usuario y la contraseña son correctas
    if user == usuario and password == passw: 
        print("contraseña y usuario correcto, puede ingresar")
        print("ingrese lo que quiera realizar")
        print("1. retirar")
        print("2. Depositar")
        print("3. Transferencia")
        print("4. Estado de cuenta")
        print("5. Salir")
        option = int(input()) #guardamos el numero en una variable para ejecutarlo despues
    if option == 1:  #ponemos una concicion para que diga si la seleccion es la correcta
        print("eliga una opcion de retiro")
        print("1. efectivo")
        print("2. cheque")
        print("3. tarjeta")
        print("4. transferencia")
        print("5. salir")
        op = int(input())  #almacenams los datos en una avriable
    if op == 1:
        retiro = int(input())
        print(retiro)
        break #rompemos es ciclo por
    else:
        print("vuelve a intentar") 

