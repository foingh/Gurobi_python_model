from gurobipy import *

# create model
m = Model("IntergerProblem")

# create variables
x = m.addVar(vtype=GRB.INTEGER, name="x")
y = m.addVar(vtype=GRB.INTEGER, name="y")
z = m.addVar(vtype=GRB.INTEGER, name="z")

# set objective function
m.setObjective(3*x+5*y+4*z, GRB.MAXIMIZE)

# add constraints
m.addConstr(2*x+3*y<=15, name="c0")
m.addConstr(2*y+4*z<=8, name="c1")
m.addConstr(3*x+2*y+5*z>=2, name="c2")

# write the mdoel
m.write('IntergerProblem.lp')

# solve the model
m.optimize()

allvars = m.getVars()
for v in allvars:
    print(v.VarName, v.X)