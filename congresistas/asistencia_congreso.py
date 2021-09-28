# -*- coding: utf-8 -*-
"""
Created on Thu May  6 20:40:58 2021

@author: Sofia
"""

import csv


def  cargar_datos(archivo:str)->list:
    lista_congresistas = list()

    with open(archivo, encoding='utf-8') as archivo:
        reader = csv.DictReader(archivo)
        for fila in reader:
            diccionario_asistencia = dict()
            diccionario_congresista = dict()
            diccionario_congresista["nombre"] = fila["congresista"]
            diccionario_congresista["movimiento"] = fila["movimiento"] 
            diccionario_congresista["circunscripcion"] = fila["circunscripcion"]
            llave = fila["fecha"]
            diccionario_asistencia[llave] = fila["dato_asistencia"]
            diccionario_congresista["asistencia"] = diccionario_asistencia
            lista_congresistas.append(diccionario_congresista)

    return lista_congresistas
        
a = cargar_datos('asistencia_congreso_v2.csv')
def mas_inasistencias(asistencias:list)->str:
    mayor_inasistencias = 0
    nombre = ''
    for congresista in asistencias:
        nombre_nuevo = congresista['nombre']
        asistencia = congresista['asistencia']
        if nombre != nombre_nuevo:
            inasistencias = 0
        asistio=list(asistencia.values())[0]
        
        
        if asistio == 'SIN EXCUSA':
            inasistencias = inasistencias + 1
            if inasistencias > mayor_inasistencias:
                mayor_inasistencias = inasistencias
                nombre_mayor_inasistencias = congresista['nombre']
        nombre = congresista['nombre']
    return (nombre_mayor_inasistencias, mayor_inasistencias)


def mas_asistencias(asistencias:list)->str:
    nombre = ''
    dic_asistencias = dict()
    for fila in asistencias:
        nombre = fila['nombre']
        asistencia = fila['asistencia']
        asistio=list(asistencia.values())[0]
        if asistio == 'ASISTIÓ':
            dic_asistencias[nombre] = dic_asistencias.get(nombre,0)+1
 
    mas_asistencia = max(dic_asistencias, key = dic_asistencias.get)
    asitio = dic_asistencias[mas_asistencia]
    return(mas_asistencia, asitio)
def porcentaje_asistencias(asistencias:list)->list:
    lista = list()
    dic_sesiones = dict()
    dic_asistencias = dict()
    for fila in asistencias:
        nombre = fila['nombre']
        dic_sesiones[nombre] = dic_sesiones.get(nombre,0)+1 
        asistencia = fila['asistencia']
        asistio=list(asistencia.values())[0]
        if asistio == 'ASISTIÓ':
            dic_asistencias[nombre] = dic_asistencias.get(nombre,0)+1 
    for keys in dic_asistencias.keys():
        dic_porcentajes = dict()
        dic_porcentajes[keys] = round((dic_asistencias[keys] / dic_sesiones[keys]),2)
        lista.append(dic_porcentajes)    
    return lista

def circunscripcion_mas_inasistencias(asistencias:list)->str:
    circunscripcion = ''
    dic_fallas = dict()
    for fila in asistencias:
        circunscripcion = fila['circunscripcion']
        asistencia = fila['asistencia']
        asistio = list(asistencia.values())[0]
        if asistio != 'ASISTIÓ':
            dic_fallas[circunscripcion] = dic_fallas.get(circunscripcion,0)+1
 
    mas_fallas = max(dic_fallas, key = dic_fallas.get)
    circunscripcion = dic_fallas[mas_fallas]
    print( "La circunscripción {} acumuló {} fallas".format(mas_fallas, circunscripcion))
    
    
def mas_inasistencias_excusa(asistencias:list)->str:
    nombre = ''
    dic_asistencias = dict()
    for fila in asistencias:
        nombre = fila['nombre']
        asistencia = fila['asistencia']
        asistio = list(asistencia.values())[0]
        if asistio == 'EX. MÉDICA':
            dic_asistencias[nombre] = dic_asistencias.get(nombre,0)+1
 
    mas_excusa = max(dic_asistencias, key = dic_asistencias.get)
    excusa = dic_asistencias[mas_excusa]
    return(mas_excusa,excusa)
    
    
def mas_X_inasistencias(asistencias:list, numero:int)->dict:
    dic_mas = dict()
    dic_asistencias = dict()
    for fila in asistencias:
        nombre = fila['nombre']
         
        asistencia = fila['asistencia']
        asistio = list(asistencia.values())[0]
        if asistio != 'ASISTIÓ' and asistio != 'SUSPENSIÓN' and asistio != ' SILLA VACÍA':
            dic_asistencias[nombre] = dic_asistencias.get(nombre,0)+1 
            
    for k ,v in dic_asistencias.items():
        if v >= numero:
            dic_mas[k] = v
            
        
    return dic_mas

def asistencias_partido(asistencias:list)->dict:
    dic_sesiones = dict()
    dic_asistencias = dict()
    dic_porcentajes = dict()
    for fila in asistencias:
        movimiento = fila['movimiento']
        dic_sesiones[movimiento] = dic_sesiones.get(movimiento,0)+1 
        asistencia = fila['asistencia']
        asistio = list(asistencia.values())[0]
        if asistio == 'ASISTIÓ':
            dic_asistencias[movimiento] = dic_asistencias.get(movimiento,0)+1 
    for keys in dic_asistencias.keys():
        
        dic_porcentajes[keys] = round((dic_asistencias[keys] / dic_sesiones[keys]),2)
   
    return dic_porcentajes

def fecha_mas_inasistencias(asistencias:list)->str:
    dic_inasistencias = dict()
    for fila in asistencias:
        
        asistencia = fila['asistencia']
        fecha = list(asistencia.keys())[0]
        asistio = list(asistencia.values())[0]
        if asistio != 'ASISTIÓ':
            dic_inasistencias[fecha] = dic_inasistencias.get(fecha,0)+1
 
    fecha_inasistencia = max(dic_inasistencias, key = dic_inasistencias.get)
    cantidad = dic_inasistencias[fecha_inasistencia]
    print ('En la fecha {} hubo {} fallas'.format(fecha_inasistencia,cantidad))
    
    
def mes_mayor_sesiones(asistencias:list)->str:
    dic_sesiones = dict()
    for fila in asistencias:        
        asistencia = fila['asistencia']
        fecha = list(asistencia.keys())[0][3:]
        dic_sesiones[fecha] = dic_sesiones.get(fecha,0)+1  
        
    mes_mayor = max(dic_sesiones, key = dic_sesiones.get)
    cantidad = dic_sesiones[mes_mayor]

    return(mes_mayor,cantidad)


def asistio_fecha(asistencias:list)->bool:
    fecha = input('Ingrese la fecha: ')
    nombre = input('Ingrese el nombre: ')
    for fila in asistencias:
        asistencia = fila['asistencia']
        if fecha == list(asistencia.keys())[0]:
            if asistencia[fecha] == 'ASISTIÓ' and nombre == fila['nombre']:
                return True
            else:
                return False
        else: return False
        
def asistencia_circunscripcion_fecha(asistencia:list)->dict():
    fecha = input('Ingrese el mes y año: ')
    dic_sesiones = dict()
    for fila in asistencia:
        circunscripcion = fila['circunscripcion']
        asistencia = fila['asistencia']
        fecha_fila = list(asistencia.keys())[0][3:]
        if fecha == fecha_fila:
            dic_sesiones[circunscripcion] = dic_sesiones.get(circunscripcion,0)+1
    return dic_sesiones
            
    

