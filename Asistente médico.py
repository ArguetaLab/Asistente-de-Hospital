import math

corre = "si"
while corre == "si":


    def condicionales(oxigenacion, temperatura, estatura, presion, frecuencia_cardiaca, dolores_musculares, peso_ideal, edad, doloresCabeza, infeccion_urinaria, dolor_oido, dormir, oir_bien, dolor, ojos):

        if tos_flema == "si":
            if temperatura >= 40:
                if dolores_musculares == "si":
                    if oxigenacion <= 93:
                        print("Posiblemente tus sintomas sean de alguna de las variantes del COVID 19"
                              "\nTe recomendamos ir a un especialista para asegurar que esta prueba es veridica")
                    elif edad >= 16:
                        print("Lo mas probable es que usted padezca de una Gripe leve"
                              "\nle recomendamos tomar: Los adultos pueden tomar acetaminofén (Tylenol, otros), ibuprofeno (Advil, Motrin IB, otros) o aspirina. "
                              "\nTen precaución cuando les des aspirina a niños o adolescentes.")
                    elif infeccion_urinaria == "si":
                        print("Posiblemente usted padezca Bronquitis"
                              "\nTe recomendamos ir a un especialista para asegurar que esta prueba es veridica")
                    elif edad <= 16:
                        print("Para la Gripe en niños le recomendamos:"
                              "\nEl paracetamol (Tylenol) y el ibuprofeno (Advil, Motrin) ayudan a bajar la fiebre en los niños.")
                    else:
                        print("Lo sentimos, no pudimos detectar el tipo de enfermedad que padece"
                              "\nle sugerimos acudir a un Médico oara un mejro servicio")
                else:
                    print("Lo sentimos, no pudimos detectar el tipo de enfermedad que padece"
                          "\nle sugerimos acudir a un Médico oara un mejor servicio")


        elif peso_ideal >= 25:
            if dolores_musculares == "si":
                if presion >= 80:
                    if frecuencia_cardiaca >= 210:
                        print("De a cuerdo con sus resultados lo mas probable es que usted padezca Obesidad"
                              "\nLe recomendamos ir a un médico especializado con en el campo"
                              "\nNosotros de momento lo que podemso hacer por usted es recomendarle:"
                              "\n   1) Plan de alimentación saludable y de actividad física regular"
                              "\n   2) Cambiar los hábitos"
                              "\n   3) Programas para controlar el peso")
                    elif temperatura >= 40:
                        if doloresCabeza == "si":
                            if tos_flema == "si":
                                print("Lo mas probable es que usted padezca de Influenza"
                                        "\nEl tratamiento recomendado para casos de influenza que no presentan complicaciones"
                                        "\nconsiste en dos dosis por día de oseltamivir oral o zanamivir para inhalar durante 5 días o una dosis de peramivir por vía intravenosa o baloxavir oral durante 1 día.")
                            else:
                                print("Lo sentimos, no pudimos detectar el tipo de enfermedad que padece"
                                      "\nle sugerimos acudir a un Médico oara un mejro servicio")
                        else:
                            print("Lo sentimos, no pudimos detectar el tipo de enfermedad que padece"
                                  "\nle sugerimos acudir a un Médico oara un mejro servicio")

        elif dormir == "si":
            if temperatura >= 38:
                if oir_bien == "no":
                    if dolor_oido == "si":
                        print("Lo mas probable es que usted padezca de una Infección en el oído"
                              "\n le recomendamos acudir a un Otorrinolaringólogo")

            if ojos == "no":
                if dolores_musculares == "si":
                    if doloresCabeza == "si":
                        print("Usted tiene los sintomas físicos de la Depresión"
                                "\nLe recomendamos asistir a un Psicólogo para que lo asista de la mejor forma en este campo"
                                "\nRecuerde, usted no está solo en esto ♡")
                    else:
                        print("Lo mas probables es que usted solamente tenga fatiga"
                                "\nDescanse el día de hoy, si se sigue sintiendo mal mañana"
                                "\nAsista a un médico para que lo antienda")
            else:
                print("Lo mas probable es que usted simplemente tenga problemas para dormir"
                      "\nLe recomendamos que haga esto para mejorar su rutina: "
                      "\n   1) Vaya a dormir a la misma hora cada noche, levántese a la misma hora cada mañana."
                      "\n   2) Evite las siestas después de las 3 p.m."
                      "\n   3) Manténgase alejado de la cafeína y el alcohol por la noche."
                      "\n   4) Evite la nicotina por completo.")

        else:
            print("Al parecer usted no padece ninguna enfermedad, pero le sugerimos acudir a un Médico oara un mejor servicio")


    # =======================================================================================================================

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
    tos_flema = input("¿Tienes tos con flemas? (si/no) ")
    dolores_musculares = input("¿Tienes dolores musculares? (si/no) ")
    doloresCabeza = input("¿Tienes dolores de cabeza? (si/no): ")
    infeccion_urinaria = input("¿Sientes ardor al orinar? ")
    dolor_oido = input("¿Sientes dolor en el oido? ")
    dormir = input("¿Tienes transtornos del sueño (no puedes dormir bien, insomnio, etc)? ")
    oir_bien = input("¿Puedes oír bien? ")
    dolor = input("¿Te sientes mas sensible al dolor físico? ")
    ojos = input("¿Ves bien? ")

    peso_ideal = peso / (math.pow(estatura, 2))
    frecuencia_cardiaca = 220 - edad
    FC60 = (frecuencia_cardiaca) * 0.6
    FC60 = round(FC60, 2)
    FC70 = (frecuencia_cardiaca) * 0.7
    FC70 = round(FC70, 2)

    # =======================================================================================================================

    def resultados():
        peso_ideal2= ""
        print("\n")
        print("============================================================")
        print("Resultados del Diagnóstico")
        print("============================================================ \n")

        print("Nombre del Paciente: ", nombre, " edad ", edad, " años")
        print("Tu IMC (Índice de masa corporal) es de: %.2f  " % (peso_ideal))
        if peso_ideal < 18.5:
            peso_ideal2 = "bajo"
            print("Tu estado de peso es ", peso_ideal2)

        elif peso_ideal >= 18.5 or peso_ideal <= 24.9:
            peso_ideal2 = "normal"
            print("Tu estado de peso es ", peso_ideal2)

        elif peso_ideal >= 25.0 or peso_ideal <= 29.9:
            peso_ideal2 = "sobrepeso"
            print("Tu estado de peso es ", peso_ideal2)

        elif peso_ideal >= 30.0:
            peso_ideal2 = "obesidad"
            print("Tu estado de peso es ", peso_ideal2)


        print("Tu Frecuencia Cardiaca es de ", frecuencia_cardiaca)
        print("Tu Frecuencia en los porcentajes de 60% sería: ", FC60, "y en el porcentaje de 70% sería: ", FC70)
        condicionales(oxigenacion, temperatura, estatura, presion, frecuencia_cardiaca, dolores_musculares, peso_ideal, edad, doloresCabeza, infeccion_urinaria, dolor_oido, dormir, oir_bien, dolor, ojos)


    # =======================================================================================================================

    resultados()
    corre = input("Ya hemos terminado con tu consulta :D ¿Te gustaría seguir probando este Asistente? (si/no): ")
    if corre == "si":
        print("\n=======================================================================================================================")
