import time
n = 10000
def obtener_elemento(lista):
    return lista[0]
lista = list(range(10000))
#Algoritmos 2

def algoritmo_2(n):
    for i in range(n):
        pass

def algoritmo_3(n):
    for i in range(n):
        for j in range(n):
            pass


inicio = time.time()
obtener_elemento(lista)
fin = time.time()
print("Algoritmo 1:", fin - inicio, "segundos")

inicio = time.time()
algoritmo_2(n)
fin = time.time()
print("Algoritmo 2:", fin - inicio, "segundos")

inicio = time.time()
algoritmo_3(n)
fin = time.time()
print("Algoritmo 3:", fin - inicio, "segundos")


#PRIMERA PARTE
# 1.)el algoritmo que crece mas rapido es el O(n²) 
# 2). O(1) es el que casi no cambia ya que su comportamiento es constante
# 3). por que lo que hace es potencia los datos a la 2 por ejemplo si tiene 9.000 datos a la 2 serian 81.000 lo que hace que sea un comportamiento ineficiente 

#SEGUNDA PARTE
# 1.) El primer algoritmo es el mas sencillo  por que solo devuelve un elemento el nivel de algortimos seria un O(1)
# 2.) El segundo algoritmo es un O(n) ya que solo recorre la lista en un ritmo consntante y dependera del tamaño de la lista por eso es un  O(n)
# 3.) El tercer algoritmo es el que mas se demora por su dificultad ya que recorre dos veces n  en su dificultad seria un O(n²))  donde n = 1.000 a la 2 seria 100.000 recorridos 

  
