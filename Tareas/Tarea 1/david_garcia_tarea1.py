# -*- coding: utf-8 -*-
"""David Garcia - Tarea1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tm3dAepruj-iU91h7WikduP-pdH9HwkO

# CC3001 Otoño 2023 Tarea 1 [David Garcia]

# Pilas de arena abelianas

### Profesores
Sección 1 Iván Sipirán •
Sección 2 Patricio Poblete •
Sección 3 Nelson Baloian

# Introducción
El objetivo de esta tarea es estudiar un problema inspirado en un fenómeno físico, a través de un modelo matemático, el cual si bien es sencillo, produce resultados que presentan una estructura muy interesante.

<img src="https://ivan-sipiran.com/downloads/arena.png" alt= “” width="200">

La idea es que si uno va formando una pila de arena, llega un momento en que se produce un derrumbe, y la arena de esa pila se derrama hacia los lugares vecinos, estos a su vez se pueden derrumbar, y el proceso continúa hasta que finalmente se estabiliza.

Para estudiar este proceso, usaremos un modelo ultra simplificado. Supondremos que la arena se deposita sobre una superficie plana, la cual está dividida en pequeñas celdas cuadradas, las cuales forman un tablero como se muestra en la siguiente figura:

<img src="https://ivan-sipiran.com/downloads/tablero.png" alt= “” width="100">

El modelo supone que si se apilan demasiados granos de arena en una celda, se produce un derrumbe. En particular, la regla es que **si en una celda hay 4 o más granos, se le quitan 4 granos, que se reparten equitativamente hacia las celdas vecinas en los cuatro puntos cardinales**.

Para simular este proceso, supondremos que cada celda almacena un número entero, que es la cantidad de granos almacenados en su interior. Aplicando la regla antes descrita (y suponiendo que las **celdas que aparecen vacías tienen cero granos**), desde la configuración

<img src="https://ivan-sipiran.com/downloads/tablero1.png" alt= “” width="100">

se pasaría a

<img src="https://ivan-sipiran.com/downloads/tablero2.png" alt= “” width="100">

Cuando hay más de una casilla con exceso de granos de arena, **la regla se puede aplicar a ellas en cualquier orden** y el resultado final es el mismo. Esta propiedad es la que hace que estas pilas de arena se llamen abelianas.

La idea es partir desde una configuración inicial, y luego aplicar esta regla en todos los casilleros que se pueda, hasta que no quede ninguno que tenga 4 o más granos de arena. Esa **configuración final la vamos a visualizar asignando un color distinto a cada número de granos**.

En particular, nos va a interesar **estudiar** lo que ocurre cuando la **configuración inicial tiene todas las celdas vacías, excepto la del centro, en la cual hay $N$ granos de arena** (donde $N$ es un parámetro del problema).

Note que en teoría el tablero es infinito en el sentido que siempre hay espacio para colocar los granos de arena que se van distribuyendo. Para su simulación, usted debe calcular un tamaño del tablero lo suficientemente grande como para estar seguro que ningún grano de arena se salga hacia afuera de los bordes (calcule la máxima área que se puede cubrir con $N$ granos de arena, y después calcule cuan grande debe ser el tablero  para poder contener esa área).

# Tarea

## Parte 1
Usted debe escribir una función en Python llamada ``arena``, tal que dado un valor de $N$, simule el proceso anteriormente descrito hasta que se estabilice. El programa debe **contar e imprimir el número total de veces que se aplicó la regla que distribuye granos de arena hacia los vecinos. Además, debe visualizar en la pantalla el tablero resultante**, usando los métodos que se describen más adelante.

Por ejemplo, al simular con $N=10000$, la figura que resulta es

<img src="https://ivan-sipiran.com/downloads/tablero3.png" alt= “” width="250">

La idea va a ser ejecutar la función con un valor de $N$ dado por el profesor ($N=128$) y luego con valores crecientes de $N$, hasta el mayor número que pueda alcanzar dentro de un tiempo de ejecución razonable.

Escriba a continuación la definición de su función:
"""

def revisamatriz(mat,tamano):

  #i=0
  #j=0
  bandera=False #Iniciamos con condicion falsa
  for i in range(0,tamano):
      for j in range(0,tamano):
        if mat[i][j]>=4:
          bandera=True #Encuentra casilla con valor >=4 entonces detiene la busqueda y le dice a arena() que continue distribuyendo
          return bandera
  return bandera #No encuentra casilla con valor para seguir distribuyendo, por lo tanto termina la distribución

import numpy as np
import matplotlib.pyplot as plt
import math

def arena(N):
  # escriba su código aquí

  #Definimos el tamaño del tablero-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  if N<32: #Caso N<32
    if N%2==0:
      m=N-1 #si es par necesito sacarle 1 para tener matriz imparXimpar
    else:
      m=N
  else:    #Caso N>32 con area de circulo
    m=int(int(math.sqrt(N/math.pi))+(math.sqrt(N/math.pi)*0.8))

  mat = np.zeros((m,m))

  #Procesamos los granos de arena-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  #Ya que todas las celdas vacias de la matriz son representadas por valor 0, y necesitamos matrices de tamaño impar para tener un lugar central para los granos de arena
  #eso nos lleva a pensar que tomando división entera del tamaño de la matriz nos permite colocar la arena al medio (EJ: 5x5 tomamos 5//2 y nos coloca los granos de arena en [2][2] que sería el centro de esa matriz)
  mat[m//2][m//2]=N

  #Recorremos toda la matriz partiendo desde arriba, ie, [0][0]
  #i=0
  #j=0
  cont=0 #Para contar numero de veces que se aplica la regla

  while revisamatriz(mat,m): #Modificada luego de feedback tarea #Funcion auxiliar que recorre la matriz y dice si hay valor 4 en alguna parte asi no cambie nada

    for i in range(0,m):
      for j in range(0,m):
        if mat[i][j]>=4:

          mat[i-1][j]+=1 #Agrega grano arriba
          mat[i][j-1]+=1 #Agrega grano izquierda
          mat[i+1][j]+=1 #Agrega grano abajo
          mat[i][j+1]+=1 #Agrega grano derecha

          mat[i][j]-=4 #le quitamos 4 granos de arena
          cont+=1


  print("Aplicaciones de la regla: ",cont) #printeamos numero de veces que se aplico la regla de distribución
  #Dibuja
  plt.matshow(mat)
  plt.show()
  return cont

"""**Explique aquí cómo calculó el tamaño que necesita tener el tablero.**

Inicialmente trate de buscar ciertas cotas para encontrar el tamaño adecuado del tablero y a su vez ver algunas iteraciones para entender mejor como podía pasar a algoritmo/código el problema de distribución de arena, como se puede ver en la siguiente imagen linkeada:

<img src="https://drive.google.com/file/d/1jDOmmm472fyHPiN-QtxYjW81XjuuPJtF/view?usp=share_link" alt= “” width="250">

https://drive.google.com/file/d/1jDOmmm472fyHPiN-QtxYjW81XjuuPJtF/view?usp=share_link

Viendo que estaba gastando más tiempo de lo recomendado por el cuerpo docente en el tablero, aproveche la recomendación del profe de pensar en el area de un circulo, así que lo hice de esta forma: $$ \pi * r * r = N $$

Luego sumandole un factor de tolerancia, sirviendo para obtener un tablero con un margen de casillas desocupadas aceptable, es importante acotar que para ***N*** muy pequeño (<32) no funciona este acotamiento y lo hice de forma más manual.

Ahora ejecute la función para $N=128$:
"""

arena(128)

"""
A continuación ejecute la función para el valor más grande de $N$ que consiga alcanzar en un tiempo razonable:"""

arena(20000) # reemplace N por el valor máximo que alcanzó a procesar

"""## Parte 2
Observe que cuando en una celda hay un número grande de granos de arena, es muy ineficiente ir quitándole de 4 en 4, y sería **mejor quitar de una sola vez lo más que se pueda**. Podemos mejorar nuestro programa si cambiamos la regla de distribución, y decimos que si en una celda hay un número de granos de arena **mayor o igual a 4, le quitamos de una sola vez el mayor múltiplo de 4 posible, y todos esos granos lo repartimos equitativamente entre los vecinos de los cuatro puntos cardinales**. Escriba una versión modificada de su función de acuerdo a esta nueva regla.


"""

def revisamatriz(mat,tamano):

  #i=0
  #j=0
  bandera=False #Iniciamos con condicion falsa
  for i in range(0,tamano):
      for j in range(0,tamano):
        if mat[i][j]>=4:
          bandera=True #Encuentra casilla con valor >=4 entonces detiene la busqueda y le dice a arena() que continue distribuyendo
          return bandera
  return bandera #No encuentra casilla con valor para seguir distribuyendo, por lo tanto termina la distribución

def maximomultiplo4(num):
    #i=0
    for i in range(0,num+1): #Num +1 pues necesito considerar el valor real del numero de granos de la casilla
      if i%4==0:             #Si es multiplo de 4 lo guardo temporalmente
        multiplo= i
    return multiplo          #retornando así el mayor multiplo de 4 encontrado

assert maximomultiplo4(12)==12
assert maximomultiplo4(9)==8

import numpy as np
import matplotlib.pyplot as plt
import math

def arena2(N):
  # escriba su código aquí

  #Definimos el tamaño del tablero------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  if N<32: #Caso N<32
    if N%2==0:
      m=N-1 #si es par necesito sacarle 1 para tener matriz imparXimpar
    else:
      m=N
  else:    #Caso N>32 con area de circulo
    m=int(int(math.sqrt(N/math.pi))+(math.sqrt(N/math.pi)*0.8))
  mat = np.zeros((m,m))

  #Procesamos los granos de arena-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  #Ya que todas las celdas vacias de la matriz son representadas por valor 0, y necesitamos matrices de tamaño impar para tener un lugar central para los granos de arena
  #eso nos lleva a pensar que tomando división entera del tamaño de la matriz nos permite colocar la arena al medio (EJ: 5x5 tomamos 5//2 y nos coloca los granos de arena en [2][2] que sería el centro de esa matriz)
  mat[m//2][m//2]=N

  #Recorremos toda la matriz partiendo desde arriba, ie, [0][0]
  #i=0
  #j=0
  cont=0 #Para contar numero de veces que se aplica la regla

  while revisamatriz(mat,m): #modificada luego de feedback tarea #Funcion auxiliar que recorre la matriz y dice si hay valor 4 en alguna parte asi no cambie nada

    for i in range(0,m):
      for j in range(0,m):
        if mat[i][j]>=4:
          multiplo=maximomultiplo4(int(mat[i][j])) #necesite ponerle int() porque si no daba error np.float64 cuando igualmente le estoy pasando un valor entero...
          mat[i-1][j]+=multiplo/4 #Agrega la cantidad de granos arriba (de acuerdo al multiplo equitativamente)
          mat[i][j-1]+=multiplo/4 #Agrega la cantidad de granos izquierda
          mat[i+1][j]+=multiplo/4 #Agrega la cantidad de granos abajo
          mat[i][j+1]+=multiplo/4 #Agrega la cantidad de granos derecha

          mat[i][j]-=multiplo #le quitamos la cantidad de granos de arena (de acuerdo al multiplo)
          cont+=1


  print("Aplicaciones de la regla: ",cont) #printeamos numero de veces que se aplico la regla de distribución
  #Dibuja
  plt.matshow(mat)
  plt.show()
  return cont

"""Ahora ejecute la función para $N=128$:"""

arena2(500)

"""A continuación ejecute la función para el valor más grande de  𝑁  que consiga alcanzar en un tiempo razonable. Note que éste número no necesariamente es el mismo que para la función anterior:"""

arena2(20000) # reemplace N por el valor máximo que alcanzó a procesar

"""## Parte 3
Compare a través de una tabla y un gráfico el número de aplicaciones de la regla que hace el programa en la Parte 1 y el de la Parte 2, para los distintos valores de $N$ que usted haya calculado.

Discuta si valió la pena la optimización y discuta también (pero no implemente) otras posibles optimizaciones que se le ocurran.
"""

import matplotlib.pyplot as plt
import numpy as np

x=np.array([64,128,500,1000,2500,5000,10000]) #Arreglo que simboliza los granos N de arena

#Se guarda en un arreglo el contador de aplicaciones de la regla de acuerdo a arena(N)
print('Aplicaciones de distribución arena según metodo arena(N)')
y=np.array([arena(64),arena(128),arena(500),arena(1000),arena(2500),arena(5000),arena(10000)]) #De igual dimensión que X pues si no da error matplotlib

#Se guarda en un arreglo el contador de aplicaciones de la regla de acuerdo a arena2(N)
print('Aplicaciones de distribución arena según metodo arena2(N)')
y2=np.array([arena2(64),arena2(128),arena2(500),arena2(1000),arena2(2500),arena2(5000),arena2(10000)])

fig = plt.figure(figsize=(10,8))

#graficamos N en eje X y arena(N) eje Y
plt.title('Aplicaciones de distribución de granos de arena N Parte 1 vs Parte2')
plt.xlabel("N granos de arena")
plt.ylabel("Aplicaciones regla de arena (N)")
plt.plot(x,y,'y--')
plt.plot(x,y2,'r--')
plt.legend(('arena(N)','arena2(N)'), prop = {'size' : 10}, loc = 'upper right')
plt.grid()

plt.show()

"""Tabla comparativa de aplicaciones de la regla arena1() y arena2() respectivamente:

![image.png](data:image/png;base64,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)

Cabe destacar que consulte con auxiliares si era posible adjuntar tabla de comparaciones hecha en excel, y me dijeron que sin ningún problema (La graficación si que está hecha en python)

Gracias a todo lo anterior, en efecto valio la pena la optimización pues acorta el numero de aplicaciones de la regla --> tiempo de ejecución. Una posible optimización que se me ocurre, es en vez de ir viendo casilla a casilla de la matriz, ir barriendo por columnas de forma de aplicar la regla en cada casilla de la columna 0, luego en cada casilla de la columna 1 y así sucesivamente, pasando si al menos 2 veces por todo el tablero ya que con 1 pasada no es suficiente, esto además se puede combinar con descontar por mayor multiplo de 4
"""