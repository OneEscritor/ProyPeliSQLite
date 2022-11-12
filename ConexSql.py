import sqlite3
from Constantes import *

def conexionDB():
    conex= sqlite3.connect(NombreBaseDatos)
    cursor=conex.cursor()
    return conex,cursor

def Anadir_Peli(obj_pelicula):
    conex,cursor= conexionDB()
    tuplapeli=(obj_pelicula.nombrep,obj_pelicula.generop,obj_pelicula.duracionp)
    sql=f"INSERT INTO peli (nombre, tipogenero, duracion) VALUES {tuplapeli};"
    cursor.execute(sql)
    conex.commit()
    conex.close()

def obtenerPeliGenero(tipogenero):
    conex,cursor=conexionDB()
    sql=f"SELECT pe.nombre, gen.nombregenero, pe.duracion  FROM peli pe, genero gen WHERE pe.tipogenero=gen.id AND gen.id={tipogenero}"
    cursor.execute(sql)
    peliPorGenero=cursor.fetchall()
    return peliPorGenero
def obtenerCatalogo():
    conex,cursor=conexionDB()
    sql="SELECT pe.nombre, pe.duracion, gen.nombregenero FROM peli pe, genero gen WHERE pe.tipogenero= gen.id"
    cursor.execute(sql)
    pelis=cursor.fetchall()
    conex.commit()
    conex.close()
    return pelis

#print(obtenerCatalogo())