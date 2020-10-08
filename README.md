# Process Optimization - Q-Learning. Bellman's equation

## Case study IA: Optimization of tasks in an e-commerce warehouse.

The problem to be solved will be to optimize the flows within the following warehouse:

![Almacen](https://raw.githubusercontent.com/mcpade/OptimizacionProcesos/master/Almacen.png)

The warehouse is owned by an online retail company that sells products to a variety of customers.
Within this warehouse, products are stored in 12 different locations, labeled with letters from A to L.
As customers order online, an autonomous warehouse robot moves around the warehouse
to collect the products for future deliveries.
The 12 locations are connected to a computer system, which classifies in real time the product collection priorities for these 12 locations.

An autonomous warehouse robot must move to the destination location by the shortest route, depending on where it is. Our goal is to build an AI that returns that shortest path, wherever the robot is. In addition, an option is implemented for our autonomous warehouse Robot to go through an intermediate location before reaching its final location.

The AI solution that will solve the problem described above is a Q-Learning model.

### Developing

The python code is in the file **qlearning.py**

The steps followed are:

- Definition of the environment. States, actions, reward matrix
- Building the AI solution with Q-Learning
- Put the model in production





