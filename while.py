
numero = 10

while numero >= 1:
    print(numero)
    numero -=1


intentos = 0
CONTRASENA_CORRECTA = "1234"


while intentos < 3:
     contrasena = input("Introduce la contraseña: ")
     if contrasena != CONTRASENA_CORRECTA:
        intentos += 1
        print(f"Contraseña incorrecta. Intento {intentos}. Te quedan {3 - intentos} intentos.")
     else:
        print("Acceso concedido")
        break

else:
    print("Acceso denegado")