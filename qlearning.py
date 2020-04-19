#Inteligencia Artificial Aplicada a Negocios y Empresas

#Parte 1 - Optimización de flujos de trabajo en un almacén con Q-Learning


#Importación de las librerías

import numpy as np

#Configuración de los parámetros gamma y alpha para el algoritmo de Q-Learning

gamma = 0.75   #factor de descuento
alpha = 0.9    #learning rate
n_iteraciones = 1000   #número de interaciones, entrenamiento

# PARTE 1 - DEFINICIÓN DEL ENTORNO

# Definción de los estados

location_to_state = {'A':0,
                     'B':1,
                     'C':2,
                     'D':3,
                     'E':4,
                     'F':5,
                     'G':6,
                     'H':7,
                     'I':8,
                     'J':9,
                     'K':10,
                     'L':11}

# Definición de las acciones. Localizaciones a las que se puede ir

actions = [0,1,2,3,4,5,6,7,8,9,10,11]



# Definición de las recompensas. Estado en el que nos encontramos y acción que 
# ejecutamos. Usamos para la represetnación una matriz. Las filas serán las filas
# y las columnas son las acciones
# Necesitamos el mapa del almacén para generar esta matriz
#Columnas:     A,B,C,D,E,F,G,H,I,J,K,L
R = np.array([[0,1,0,0,0,0,0,0,0,0,0,0], #A
              [1,0,1,0,0,1,0,0,0,0,0,0], #B
              [0,1,0,0,0,0,1,0,0,0,0,0], #C
              [0,0,0,0,0,0,0,1,0,0,0,0], #D
              [0,0,0,0,0,0,0,0,1,0,0,0], #E
              [0,1,0,0,0,0,0,0,0,1,0,0], #F
              [0,0,1,0,0,0,0,1,0,0,0,0], #G
              [0,0,0,1,0,0,1,0,0,0,0,1], #H
              [0,0,0,0,1,0,0,0,0,1,0,0], #I
              [0,0,0,0,0,1,0,0,1,0,1,0], #J
              [0,0,0,0,0,0,0,0,0,1,0,1], #K
              [0,0,0,0,0,0,0,1,0,0,1,0]])#L


#Transformación inversa de estados a ubicaciones

state_to_location = {state:location for location,state in location_to_state.items()}
              


# PARTE 2 - CONSTRUCCIÓN DE LA SOLUCIÓN DE LA IA CON Q-LEARNING

#Entrenamiento según el punto final al que queremos ir


def training (ending_location):
    
    #Uso el diccionario para obtener el valor
    ending_state = location_to_state [ending_location]
    
    
    #Modifico la matriz de recompensas R para dar una mayor recompensa
    #al punto al que quiero ir
    R_new = np.copy(R)   #Hago una copia de la matriz R y modifico la copia
    R_new [ending_state,ending_state] = 1000
    
    
    
    

    #Entrenamiento
    
    
    #Inicialización de los Q-values. Inicializamos la matriz Q(s,a) con valores 0
    #Para todas las parejas de estados (s) y acciones (a) los Q-values se inicializan
    #a 0
    
    #Q = np.array(np.zeros([12,12]))
    Q = np.array(np.zeros([len(location_to_state), len(actions)]))
 

    #Implementación del proceso de Q-Learning. Actualizamos los valores Q en base
    #a la ecuación de Bellmann

    #Para cada instante t repetimos un cierto número de veces los siguientes
    #pasos


    for i in range (n_iteraciones):

        #Paso 1: Seleccionamos un estado aleatorio st de nuestros 12 estados posibles
        current_state = np.random.randint (0,len(location_to_state))   #El último valor no se incluye
                                               #randint: número entero
                                               
        #Paso 2: Llevamos a cabo una acción aleatoria at que puede conducir al siguiente
        #estado posible, es decir, de modo que R(st,at)>0                                           
        playable_actions = []    #acciones posibles
    
        a = R_new[current_state,:]   #Estado actual, fila
        for j in range (len(a)): #Me quedo con los índices de esa fila que tenga valores >0
            if a[j]>0:
                playable_actions.append(j) #añado el índice a las playable_actions
    
        action = np.random.choice(playable_actions) #Elijo aleatoriamente ente esos índices
       
        #Paso 3: Llegamos al siguiente estado st+1 y obtenemos la recompensa
        next_state = action  

        #Paso 4: Cálculamos la Diferencia Temporal TD (st, at)   
    
        #TD(a,s) = R(s,a) + gamma * maximo a'(s',a') - Q(s,a)
    
        #argmax devuelve un índice
    
        TD = R_new[current_state,action] + gamma * Q[next_state,np.argmax(Q[next_state,])] - Q[current_state, action]
    
    
        #Paso 5. Actualizamos el valor Q aplicando la euación de Bellman
    
        #Q(s,a) = Qt-1 (s,a) + alpha * TD (s,a)
    
        Q[current_state,action] += alpha*TD

    return Q

# PARTE 3 - PONER EL MODELO EN PRODUCCIÓN

        

#Crear la función final que nos devuelva la ruta óptima

#Nos movemos desde la ubicación inicial a la final por los valores Q más 
#elevados   

def route (starting_location, ending_location):
    
    route =[]
    
    #Compruebo que tanto el comienzo de la ruta como el final de la ruta
    #sean estados conocidos
    
    
       
    #Entrenamiento para obtener los valores Q
    Q = training (ending_location)
        
        
    #inicio de la ruta
    route =[starting_location]
    #iremos añadiendo las localizaciones mientras no lleguemos al punto final
    
    next_location = starting_location
    
    #Buclue mientras no llegamos al final
    while (next_location != ending_location):  
            
            #Estando en el estado actual, (fila de la matriz Q) tengo que escoger
            #la acción correspondiente al mayor valor Q, es decir el mayor valor
            #que haya en las columnas
            
            #Uso el diccionario para pasar a valor numérico
            starting_state = location_to_state[starting_location]
            
            #Busco la acción máxima en esa fila
            next_state = np.argmax (Q[starting_state,])
            #next_state = max_con_prioridad (Q[starting_state,])
            
            #Transformación inversa del diccionario para tener la letra
            next_location = state_to_location [next_state]
            
            route.append(next_location)
            
            starting_location = next_location

    
    return route



def route_with_interim (starting_location, interim_location, ending_location):
    
    route1 = route (starting_location,interim_location)
    route2 = route (interim_location,ending_location)
    
    #uno ambas rutas, en la segunda ruta no añado el primer elemento para que no 
    #salgan dos veces el punto intermedio   
    result_route = route1+route2[1:]
    
    return (result_route)
    
    

    
def Print_Route (starting_location, interim_location, ending_location):
    if (starting_location in location_to_state) and (ending_location in location_to_state)and (interim_location in location_to_state):
        print ("Ruta elegida: ")
        ruta = route_with_interim(starting_location, interim_location, ending_location)
        print (ruta)
    else:
        print ("El punto de inicio, intermedio o final no es válido")
 
    
#Imprimir la ruta final (punto inicial, intermedio y final)    

Print_Route ('E','K','G')    
   
    
    
    


