# The code will simulate a prey-predators enviroment

CONST_A = 0.1
CONST_B = 0.01
CONST_C = 0.01
CONST_D = 0.00002

initial_preys = 1000
initial_predators = 20

iterations = 10 # one iteration is equal to one year

for i in range(iterations):
    preys = initial_preys * (1 + CONST_A - (CONST_B * initial_predators))
    predators = initial_predators * (1 - CONST_C + (CONST_D * initial_preys))
    initial_preys = preys
    initial_predators = predators
print("After ", iterations, " years, there are ", int(predators), " predators...")
print("After ", iterations, " years, there are ", int(preys), " preys...")
