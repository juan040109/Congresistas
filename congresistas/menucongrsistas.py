import asistencia_congreso as mod

def iniciar_aplicacion():
    continuar = True
    asistencia = None
    while continuar == True:
        mostrar_menu()
        opcion_selecionada = input('digite una opcioin ')
        if opcion_selecionada == '0':
            continuar = False
        elif opcion_selecionada == '1':
            asistencia = mod.cargar_datos()
        elif opcion_selecionada == '2':
            mod.congrasitas_asistencias(asistencia)
        elif opcion_selecionada == '3':
            mod.congrasitas_sin_excusa(asistencia)
        elif opcion_selecionada == '4':
            mod.promedio(asistencia)
        elif opcion_selecionada == '5':
            mod.fallas_circunscripcion(asistencia)
        elif opcion_selecionada == '6':
            mod.congrasitas_excusa_medica(asistencia)
        elif opcion_selecionada == '7':
            mod.fecha_fallas(asistencia)
        elif opcion_selecionada == '8':
            mod.mes_seciones(asistencia)
def mostrar_menu():
    print('0-salir del programa')
    print('1-cargar archico')
    print('2-congrsistas con mas asistencias')
    print('3-congrsistas con mas fallas injustificadas')
    print('4-promedio')
    print('5-circunscripcion fallas')
    print('6-mayor numero de excusas medicas')
    print('7-mayor numero de in asitencia por fecha')
    print('8-mes con mas asistencias')

iniciar_aplicacion()

