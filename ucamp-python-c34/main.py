#############################################################################################################
print("""
# ¡Bienvenidos a la calculadora del Índice de Masa Corporal!
# En un momento se le solicitara ingresar información. 
""")

nombre = input("Ingrese su Nombre: ") #Se pide el nombre
apellido_p = input("Ingrese su Apellido Paterno: ") #Se pide el apellido paterno 
apellido_m = input("Ingrese tu Apellido Materno: ") #Se pide el apellido Materno
edad = int(input("Ingrese su edad en años por favor: ")) #Se solicita que ingrese su edad
altura = float(input ("Ingrese su estatura en metros por favor: ")) #Aqui se solicita la estatura en metros
masa = float (input("Ingrese su peso en kilogramos por favor :")) #Aqui se solicita el peso en kilogramos


#Calculo del IMC, masa (En kilogramos) entre la estatura (En metros) elevada al cuadrado
IMC = masa / altura**2

#Se realiza la impresión de los datos del IMC
completo = nombre + " " + apellido_p + " " + apellido_m
print(completo)


if(edad < 18):
        print("Usted es menor de edad")
else:
        print("Usted es mayor de edad")
print("IMC: " + str(IMC) )

    #Hacemos las distintas validaciones
if IMC >= 0 and IMC <= 18.9 :
        print ("Usted tiene peso bajo")
elif IMC >= 18.50 and IMC <= 24.99 :
        print ("Usted esta en un peso normal")
elif IMC >= 25.00 and IMC <= 29.99:
        print ("Usted tiene sobrepeso")
elif IMC >= 30.00 and IMC <= 34.99 :
        print ("Usted tiene obecidad Leve")
elif IMC >= 35.00 and IMC <= 39.99:
        print ("Usted tiene sobrepeso")
elif IMC >= 30.00 and IMC <= 34.99:
        print ("Usted tiene obesidad leve")
elif IMC >= 35.00 and IMC <= 39.99:
        print ("Usted tiene obesidad media")
elif IMC >= 40.00:
        print ("Usted tiene obesidad mórbida")
