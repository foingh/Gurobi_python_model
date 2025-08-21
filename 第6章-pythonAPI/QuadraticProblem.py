from gurobipy import *

# create model
m = Model("QuadraticProblem")

# create variables
x = m.addVar(vtype=GRB.CONTINUOUS, name="x")
y = m.addVar(vtype=GRB.CONTINUOUS, name="y")

# set objective function
# m.setObjective(-2*x-6*y+(x*x-2*x*y+2*y*y)/2, GRB.MINIMIZE)
# another way to set objective function
obj = QuadExpr(0)
obj.addTerms(0.5, x, x)
obj.addTerms(1, y, y)
obj.addTerms(-1, x, y)
obj.addTerms(-2, x)
obj.addTerms(-6, y)
m.setObjective(obj, GRB.MINIMIZE)

# add constraints
m.addConstr(-x+2*y<=2, name="c0")
m.addConstr(x+y<=2, name="c1")
m.addConstr(2*x+y<=3, name="c2")

# write the mdoel
m.write('QuadraticProblem.lp')

# solve the model
m.optimize()

allvars = m.getVars()
for v in allvars:
    print(v.VarName, v.X)