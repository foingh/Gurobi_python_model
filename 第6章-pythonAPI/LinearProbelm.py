from gurobipy import *

try:
    # create a new model
    m = Model("LinearProblem")

    # Create variables
    x = m.addVar(vtype=GRB.CONTINUOUS, name="x")
    y = m.addVar(vtype=GRB.CONTINUOUS, name="y")
    z = m.addVar(vtype=GRB.CONTINUOUS, name="z")

    # set objective function
    m.setObjective(3*x+5*y+4*z, GRB.MAXIMIZE)

    # add constraint
    m.addConstr(2*x+3*y<=15, name="c0")
    m.addConstr(2*y+4*z<=8, name="c1")
    m.addConstr(3*x+2*y+5*z>=2, name="c2")

    # write the model
    m.write("LinearProblem.lp")

    # solve the problem
    m.optimize()



    print("optimal solution = ", end=" ")
    for i in m.getVars():
        print("%s = %g" % (i.VarName, i.X), end="  ")

except GurobiError as e:
    print('error code ' + str(e.errno) + ":" + str(e))