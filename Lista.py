class Lista:
    def __init__(self,datos=[]):
       self.lista = datos
        
    def push(self,dato):
        self.lista.append(dato)
        
    def pop(self):
        dato = self.lista.pop()
        return dato
    
    def eleminarElemento(self,pos):
        if pos < 0 or pos >= len(self.lista):
           return None
        else:    
           self.lista = self.lista[0:pos] + self.lista[pos+1:]
        
numeros = Lista()
numeros.push("Erick")
numeros.push("Kevin")
numeros.push("Rene")
numeros.push("Simom")
numeros.push("Julio")


numeros.eleminarElemento(1)



print(numeros.lista)