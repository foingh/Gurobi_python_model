from gurobipy import *

# create model
m = Model("SOCP")

# create variables
x = m.addVar(vtype=GRB.CONTINUOUS, name="x")
y = m.addVar(vtype=GRB.CONTINUOUS, name="y")
z = m.addVar(vtype=GRB.CONTINUOUS, name="z")

# set objective function
m.setObjective(x+y, GRB.MAXIMIZE)

# add constraints
m.addConstr(x + y + z <= 2, name="c0")
m.addConstr(x * x + y * y <= z * z, name="c1")
# m.addConstr(0.5*y+x*x<=2, name="c2")

# write the mdoel
m.write('SOCP.lp')

# solve the model
m.optimize()

allvars = m.getVars()
for v in allvars:
    print(v.VarName, v.X)
