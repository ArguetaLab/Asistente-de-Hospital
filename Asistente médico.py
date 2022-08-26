import math

#ARRIBA DE TODO VA A HABER UN WHILE PARA QUE SE REPITA EL CÓDIGO DE FORMA INFINITA HASTA QUE EL USUARIO CIERRE SESIÓN
#Bienvenida
print("\n")
print("============================================================")
print("¡Bienvenidos! Me llamo Asis y seré tu asistente médico")
print("============================================================")
print("\n")
print("Antes de poder hacerte una conclusión de la posible enfermedad que tengas")
print("Necesitamos que pongas algunos datos:")

# Entradas
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("Por favor introduce tu Edad: "))
oxigenacion = float(input("Por favor introduce tu Oxigenacion: "))
temperatura = float(input("Por favor introduce tu Temperatura: "))
estatura = float(input("Por favor introduce tu Estatura (Metros, usa decimales porfa :D): "))
presion = float(input("Por favor introduce tu Presión: "))
peso = float(input("Por favor introduce tu Peso (Kg): "))

#Aquí va a haber una lista con todos los posibles sintomas y vas a tener que ir selaccionando de acuerdo a los que aparezcan. Tambien con enfermedades pasadas
#Aquí van a if las condiconales para ir descartando enfermedades
#Aquí van a ir los resultados:

print("\n")
print("============================================================")
print("Resultados del Diagnóstico")
print("============================================================ \n")

peso_ideal = peso/(math.pow(estatura, 2))
frecuencia_cardiaca = 220 - edad
FC60 = (frecuencia_cardiaca) * 0.6
FC60 = round(FC60, 2)
FC70 = (frecuencia_cardiaca) * 0.7
FC70 = round(FC70, 2)

#aquí va a ir el numero de peso ideal y tambien si está bien, pero para eso necesito condicionales
peso_ideal2 = "ta bueno"


print("Tu peso ideal es de: %.2f  " % (peso_ideal))
print("Eso quiere decir que su peso es: ", peso_ideal2)
print("Tu Frecuencia Cardiaca es de ", frecuencia_cardiaca)
print("Tu Frecuencia en los porcentajes de 60% sería: ", FC60, "y en el porcentaje de 70% sería: ", FC70)



