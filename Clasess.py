
class Pelicula:
    def __init__(self,nombre,duracion,genero):
        self.nombrep=nombre
        self.duracionp=duracion
        self.generop=genero

class Catalogo:
    def __init__(self, nombre):
      self.nombreCata=nombre
      self.lis_peli=[]

    def mostrar(self):
        for pelis in self.lis_peli:
            print(f"""
     Nombre: {pelis.nombrep}
     Duracion: {pelis.duracionp}
     Genero: {pelis.generop} """)