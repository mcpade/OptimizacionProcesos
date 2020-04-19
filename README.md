# Optimización de Procesos - Q-Learning. Ecuación de Bellman

## Caso práctico IA: Optimización de tareas en un almacén de comercio electrónico.

El problema a resolver será optimizar los flujos dentro del siguiente almácen:

![Almacen](https://raw.githubusercontent.com/mcpade/OptimizacionProcesos/master/Almacen.png)

El almacén pertenece a una empresa online minorista que vende productos a una variedad de clientes. 
Dentro de este almacén, los productos se almacenan en 12 ubicaciones diferentes, etiquetadas con letras de la A a la L.
A medida que los clientes hacen los pedidos online, un robot de almacén autónomo se mueve por el almacén 
para recoger los productos para futuras entregas.
Las 12 ubicaciones están conectadas a un sistema informático, que clasifica en tiempo real las prioridades de recolección de productos para estas 12 ubicaciones.

Un robot de almacén autónomo debe moverse a la ubicación de destino por la ruta más corta, dependiendo de dónde se encuentre.  Nuestro objetivo es construir una IA que devuelva esa ruta más corta, donde sea que esté el robot. Además se implementa una opción para que nuestro Robot de almacén autónomo pase por una ubicación intermedia antes de llegar a su ubicación final.

La solución de IA que resolverá el problema descrito anteriormente es un modelo de Q-Learning. 





