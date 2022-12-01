##1.Definir la siguiente clases con sus métodos iniciales y su método __str__

class Alumno:
    ciclo=""
    def __init__(self,name,carrera,codigo) :
        self.name=name
        self.carrera=carrera
        self.codigo=codigo

    def Callciclo(self,ciclo):
        self.ciclo=ciclo

    def Calluniversity(self,universidad):
        self.universidad=universidad
        #print(self.universidad)
    def __str__(self):
        return f"Datos del alumno \nNombre: \t{self.name}\nCarrera: \t{self.carrera} \nCódigo: \t{self.codigo}\nY se encuentra en el {self.ciclo} ciclo de la {self.universidad}"

alu1=Alumno("Sebastian","Ing Sistemas","1615215339")
alu1.Callciclo("octavo")
alu1.Calluniversity("UNAC")
print(alu1)