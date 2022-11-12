from ConexSql import *
from Clasess import Catalogo,Pelicula
from time import sleep
def Agregar_Peli():
   salir=True
   nombre=input("Ingrese Nombre de la Pelicula: ")
   while salir:
     duracion=input("Ingrese minutos de duracion: ")
     if duracion.isdigit()==True:
         salir=False
     else:
        print("----Debe Ingresar Solo Digitos----")
   salir=True
   while salir:
      try:
          genero=int(input("""     Ingrese Genero
        [1] Ciencia Ficcion    [4] Terror
        [2] Drama              [5] Suspenso  
        [3] Accion             [6] Aventura   :"""))
          if genero<=6 and genero>=1:
              salir=False
          else:
             print("Debe Ingresar Una Opcion Valida (1,2...6)")
      except Exception as er:
        print("---Debe Ingresar solo Digitos---")
   addPeli=Pelicula(nombre, duracion,genero)
   Anadir_Peli(addPeli)

def ver_todo():
    peliculas=obtenerCatalogo()
    #print(peliculas)
    cata = Catalogo("Catalogoo Completo")
    for tuplapeli in peliculas:
      guardarPeli=Pelicula(tuplapeli[0],tuplapeli[1],tuplapeli[2])
      cata.lis_peli.append(guardarPeli)
    print(f"{cata.nombreCata}".center(30,"-"))
    cata.mostrar()

def ver_por_genero(genero,listaPelis):
     cata=Catalogo(genero)
     listadePeli=listaPelis
     for PeliTupla in listadePeli:
         ObjPeli=Pelicula(PeliTupla[0],PeliTupla[2],PeliTupla[1])
         cata.lis_peli.append(ObjPeli)
     print(f"{cata.nombreCata}".center(30,"-"))
     cata.mostrar()

def filtrar():
  Salir=True
  print("Seleccione Un Genero".center(30,"-"))
  while Salir:
     try:
          opcionGen=int(input("""[1] Ciencia Ficcion
[2] Drama
[3] Accion
[4] Terror
[5] Suspenso
[6] Aventura
[7] Regresar
            :"""))
          if opcionGen==1:
              pelisgenero = obtenerPeliGenero(opcionGen)
              ver_por_genero(CF,pelisgenero)
          elif opcionGen==2:
              pelisgenero = obtenerPeliGenero(opcionGen)
              ver_por_genero(D, pelisgenero)
          elif opcionGen==3:
              pelisgenero = obtenerPeliGenero(opcionGen)
              ver_por_genero(Acc, pelisgenero)
          elif opcionGen==4:
              pelisgenero = obtenerPeliGenero(opcionGen)
              ver_por_genero(Tr, pelisgenero)
          elif opcionGen==5:
              pelisgenero = obtenerPeliGenero(opcionGen)
              ver_por_genero(Susp, pelisgenero)
          elif opcionGen==6:
              pelisgenero = obtenerPeliGenero(opcionGen)
              ver_por_genero(Ave, pelisgenero)
          elif opcionGen==7:
              Salir=False
          else:
              cont=3
              print("Debe seleccionar un digito (1,2,..7)",end="")
              while cont:
                print(".",end="")
                sleep(retardo)
                cont-=1
     except Exception as er:
       print("Selecciones Una Opcion Valida")

def menu_peli():
    Salir=True
    while Salir:
       try:
         opcion=int(input("""[1] Ver Todo
[2] Filtrar
[3] Regresar
             : """))
         if opcion==1:
            ver_todo()
         elif opcion==2:
            filtrar()
         elif opcion==3:
            Salir=False
       except Exception as er:
           print("Debe Seleccionar una Opcion Valida(1-3)")


#Agregar_Peli()
#ver_todo()
#filtrar()