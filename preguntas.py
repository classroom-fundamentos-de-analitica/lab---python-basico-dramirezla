# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 10:29:58 2023

@author: David R.L
"""
"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

import csv

def pregunta_01():
    """
   Retorne la suma de la segunda columna.
   Rta/
   214
   """
    c=[]
    with open('data.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            c.append(int(row[0][2]))
    return sum(c)

def pregunta_02():
    """
   Retorne la cantidad de registros por cada letra de la primera columna como la lista
   de tuplas (letra, cantidad), ordendas alfabéticamente.
   Rta/
   [
       ("A", 8),
       ("B", 7),
       ("C", 5),
       ("D", 6),
       ("E", 14),
   ]
   """
    registros = {}
    with open('data.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            letra = row[0][0]
            if letra in registros:
                registros[letra] += 1
            else:
                registros[letra] = 1
    return sorted(registros.items())

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.
    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]
    """
    sumas = {}
    with open('data.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            letra = row[0][0]
            suma = int(row[0][2])
            if letra in sumas:
                sumas[letra] += suma
            else:
                sumas[letra] = suma
    return sorted(sumas.items())

def pregunta_04():
    """
  La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
  registros por cada mes, tal como se muestra a continuación.
  Rta/
  [
      ("01", 3),
      ("02", 4),
      ("03", 2),
      ("04", 4),
      ("05", 3),
      ("06", 3),
      ("07", 5),
      ("08", 6),
      ("09", 3),
      ("10", 2),
      ("11", 2),
      ("12", 3),
  ]
  """
    meses = {}
    with open('data.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            fecha = row[0][9:11]
            if fecha in meses:
                meses[fecha] += 1
            else:
                meses[fecha] = 1
    return sorted(meses.items())

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.
    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]
    """
    maximos = {}
    minimos = {}
    with open('data.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            letra = row[0][0]
            valor = int(row[0][2])
            if letra in maximos:
                if valor > maximos[letra]:
                    maximos[letra] = valor
                elif valor < minimos[letra]:
                    minimos[letra] = valor
            else:
                maximos[letra] = valor
                minimos[letra] = valor
    resultado = []
    for letra in sorted(maximos.keys()):
        resultado.append((letra, maximos[letra], minimos[letra]))
    return resultado


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """

    dict_valores = {chr(i)+chr(j)+chr(k): [float('inf'), float('-inf')] for i in range(97, 123) for j in range(97, 123) for k in range(97, 123)}
    
    
    with open("data.csv", "r") as archivo:
        next(archivo)  
        for linea in archivo:
            campos = linea.strip().split()
            claves_valores = campos[4].split(",")
            for clave_valor in claves_valores:
                clave, valor = clave_valor.split(":")
                valor = int(valor)
                dict_valores[clave][0] = min(dict_valores[clave][0], valor)
                dict_valores[clave][1] = max(dict_valores[clave][1], valor)

    
    resultado = [(clave, dict_valores[clave][0], dict_valores[clave][1]) for clave in dict_valores if dict_valores[clave][0] != float('inf')]
    resultado.sort()
    
    return resultado

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    result = []
    values = {}
    with open('data.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            value = row[0][2]
            letter = row[0][0]
            if value not in values:
                values[value] = []
            values[value].append(letter)

    for key in sorted(values.keys()):
        result.append((int(key), values[key]))

    return result


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    # Abrir el archivo de datos
    with open("data.csv", "r") as f:
        # Leer las líneas del archivo
        lines = f.readlines()

    # Inicializar un diccionario vacío
    values_dict = {}

    # Recorrer las líneas del archivo
    for line in lines:
        # Separar las columnas de la línea
        columns = line.strip().split(",")
        # Obtener los valores de las columnas 0 y 1
        val_0 = columns[0][0]
        val_1 = int(columns[0][2])
        # Si el valor de la columna 1 no está en el diccionario, agregarlo con una lista vacía
        if val_1 not in values_dict:
            values_dict[val_1] = []
        # Agregar el valor de la columna 0 a la lista correspondiente al valor de la columna 1
        values_dict[val_1].append(val_0)

    # Inicializar una lista vacía para almacenar los resultados
    result_list = []

    # Recorrer los elementos del diccionario, ordenados por la clave
    for key in sorted(values_dict.keys()):
        # Obtener la lista de valores correspondiente a la clave actual
        values_list = values_dict[key]
        # Eliminar elementos duplicados y ordenar la lista
        unique_values = sorted(list(set(values_list)))
        # Agregar la tupla con el resultado a la lista de resultados
        result_list.append((key, unique_values))

    return result_list

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    # Inicializar el diccionario que se va a retornar
    count_dict = {
        "aaa": 0,
        "bbb": 0,
        "ccc": 0,
        "ddd": 0,
        "eee": 0,
        "fff": 0,
        "ggg": 0,
        "hhh": 0,
        "iii": 0,
        "jjj": 0,
    }

    # Abrir el archivo y leer las líneas
    with open("data.csv", "r") as f:
        lines = f.readlines()

    # Recorrer las líneas del archivo, ignorando la primera que es la cabecera
    for row in lines:
        if("aaa" in row):
            count_dict["aaa"]+=1
        if("bbb" in row):
            count_dict["bbb"]+=1
        if("ccc" in row):
            count_dict["ccc"]+=1
        if("ddd" in row):
            count_dict["ddd"]+=1
        if("eee" in row):
            count_dict["eee"]+=1
        if("fff" in row):
            count_dict["fff"]+=1
        if("ggg" in row):
            count_dict["ggg"]+=1
        if("hhh" in row):
            count_dict["hhh"]+=1
        if("iii" in row):
            count_dict["iii"]+=1
        if("jjj" in row):
            count_dict["jjj"]+=1
            
    return count_dict


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]
    """
    # Leer el archivo CSV y guardar los datos en una lista de listas
    with open('data.csv', 'r') as f:
        data = [line.strip().split(',') for line in f]

    # Obtener las columnas 1, 4 y 5
    col1 = [row[1] for row in data]
    col4 = [row[4] for row in data]
    col5 = [row[5] for row in data]

    # Crear un diccionario que almacene la cantidad de elementos de las columnas 4 y 5 para cada letra de la columna 1
    result_dict = {}
    for i, letter in enumerate(col1):
        if letter not in result_dict:
            result_dict[letter] = [0, 0]
        result_dict[letter][0] += len(col4[i])
        result_dict[letter][1] += len(col5[i])

    # Crear una lista de tuplas a partir del diccionario
    result = [(key, value[0], value[1]) for key, value in result_dict.items()]

    # Ordenar la lista por la letra de la columna 1
    result.sort()

    return result


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.
    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }
    """
    diccionario = {}
    with open("data.csv") as archivo:
        for linea in archivo:
            columnas = linea.strip().split(";")
            letra = columnas[0][20]
            valor = int(columnas[0][2])
            if letra in diccionario:
                diccionario[letra] += valor
            else:
                diccionario[letra] = valor
    diccionario_ordenado = dict(sorted(diccionario.items()))
    return diccionario_ordenado


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.
    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }
    """
    diccionario = {}
    with open("data.csv") as archivo:
        for linea in archivo:
            columnas = linea.strip().split(",")
            clave = columnas[0]
            valor = int(columnas[4])
            if clave in diccionario:
                diccionario[clave] += valor
            else:
                diccionario[clave] = valor
    return diccionario

#print(pregunta_06())
#9,10,11,12
