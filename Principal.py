from Funciones import *

while True:
    try:
       opcion=int(input("""[1] Añadir Pelicula
[2] Ver Catalogo Peliculas
[0] Salir
        :"""))

       if opcion==1:
           Agregar_Peli()
       elif opcion==2:
           menu_peli()
       elif opcion==0:
            exit()
    except Exception as er:
        print("Por favor Ingrese Una Opcion Valida".center(50,'!'))