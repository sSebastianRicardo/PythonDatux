##3.Crear una clase Animal ,luego una clase Perro y gato que sean hijos de Animal ,el método
##de Sonido debe ser diferente

class Animal:
    def __init__(self,sexo):
        self.sexo=sexo
    def __str__(self):
         return (f"El sexo de mi mascota es: {self.sexo} ")

class Perro(Animal):
    def __init__(self, sexo,onomatopeya):
        super().__init__(sexo)
        self.onomatopeya=onomatopeya
    def sonido(self):
        return f"Mi mascota emite este sonido: {self.onomatopeya}"
              

class Gato(Animal):
    def __init__(self, sexo,onomatopeya):
        super().__init__(sexo)
        self.onomatopeya=onomatopeya
    def sonido(self):
        return f"Mi mascota emite este sonido: {self.onomatopeya}"

mimascota=Perro("macho","ladrido")
print(mimascota)
print(mimascota.sonido())

