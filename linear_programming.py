import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory
import sys

model  = pyo.ConcreteModel()

model.x = pyo.Var(bounds=(0,10))
model.y = pyo.Var(bounds=(0,10))

#variables
x = model.x
y = model.y

# constrains
model.C1 = pyo.Constraint(expr= -x+2*y<=8)
model.C2 = pyo.Constraint(expr= 2*x+y<=14)
model.C3 = pyo.Constraint(expr = 2*x-y<=10)

# function objective
model.obj = pyo.Objective(expr = x+y, sense=maximize)

#model resolve
solvername='glpk'


solver=SolverFactory(solvername)
solver.solve(model)

#visualize results
model.pprint()

x_value = pyo.value(x)
y_value = pyo.value(y)

print('x=',x_value)
print('y=',y_value)
