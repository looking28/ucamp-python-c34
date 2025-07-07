# ucamp-python-c34
Descripción del Programa de la Calculadora del Índice de Masa Corporal (IMC)

El programa fue generado para calcular el Índice de Masa Corporal (IMC), este tiene como objetivo principal recibir los datos del usuario como su nombre, apellido paterno, apellido materno, edad, peso y estatura, desplegarlos en pantalla junto con su Índice de Masa Corporal (IMC) y ofrecer una clasificación en función de su resultado.

A continuación, te explico detalladamente los pasos de cómo se llevó a cabo este proyecto.

1. Captura de Datos del Usuario
La primera parte del programa consiste en obtener los datos necesarios para calcular el IMC: el peso y la altura. Para esto, se utiliza la función input(), que permite capturar información desde el teclado.

nombre = input("Ingrese su Nombre: ") #Se solicita el nombre
apellido_p = input("Ingrese su Apellido Paterno: ") #Se solicita el apellido paterno 
apellido_m = input("Ingrese tu Apellido Materno: ") #Se solicita  el apellido Materno
edad = int(input("Ingrese su edad en años por favor: ")) #Se solicita que ingrese su edad
altura = float(input ("Ingrese su estatura en metros por favor: ")) #Aqui se solicita la estatura en metros
masa = float (input("Ingrese su peso en kilogramos por favor :")) #Aqui se solicita el peso en kilogramos

2. Cálculo del IMC
El cálculo del IMC se realiza con la fórmula estándar:
Calculo del IMC, masa (En kilogramos) entre la estatura (En metros) elevada al cuadrado
​IMC = masa / altura**2
 
Una vez que tenemos el peso y la altura validados, el cálculo se hace simplemente dividiendo el peso por el cuadrado de la altura. Este valor se devuelve como resultado de la función.

3. Salida de Datos y Clasificación del IMC
El resultado del IMC se imprime de manera clara para que el usuario vea el cálculo realizado, junto con los datos que ingresó.

completo = nombre + " " + apellido_p + " " + apellido_m
print(completo)


if(edad < 18):
        print("Usted es menor de edad")
else:
        print("Usted es mayor de edad")
print("IMC: " + str(IMC) )

#Hacemos las distintas validaciones contemplando la fuente del ISSTE
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


Reflexiones sobre el Proyecto
Validación de Entradas:
Uno de los aprendizajes más importantes en este proyecto es la importancia de la validación de datos. Si bien el cálculo del IMC es simple, los usuarios pueden ingresar datos erróneos de forma accidental. Implementar un manejo adecuado de errores no solo hace que el programa sea más robusto, sino que también mejora la experiencia del usuario.

Interacción con el Usuario:
El uso de mensajes claros e instrucciones facilita la interacción con el programa. En lugar de esperar que el usuario entienda el proceso o los errores, el sistema guía al usuario paso a paso, lo cual es esencial para la usabilidad del software.

Importancia de las Condiciones y Clasificación:
Mostrar al usuario una interpretación de su IMC es una parte importante del valor del programa. No solo le damos el número, sino que también le decimos lo que ese número significa en términos de su salud, lo cual es más informativo que simplemente hacer un cálculo.

Simplicidad y Funcionalidad:
Este proyecto es un ejemplo de cómo un problema matemático relativamente simple puede ser resuelto de manera eficaz con un código sencillo. La clave es tener en cuenta tanto la funcionalidad como la facilidad de uso del programa.

Posibles Mejoras:

Validar los datos para asegurarse de que el usuario introduce solo números (no texto, caracteres especiales, etc.).

Agregar más detalles sobre la salud basada en el IMC, como recomendaciones dietéticas o de ejercicio.

En resumen, este proyecto muestra cómo, con un poco de lógica, podemos transformar una fórmula matemática simple en una herramienta útil para la salud. Además, destaca la importancia de la validación de entradas y de la interacción clara con el usuario, elementos esenciales para cualquier programa que se utilice en la vida real.