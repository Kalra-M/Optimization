from docplex.mp.model import Model

mdl = Model(name = 'knapsack')

price = [20, 5, 10, 40, 15, 25]
weight = [1, 2, 3, 8, 7, 4]
max_cap = 10
n = 6

x = {(i) : mdl.binary_var(name = f'x{i}') for i in range(n)}

mdl.add_constraint(mdl.sum(weight[i] * x[i] for i in range(n)) <= max_cap)

mdl.maximize(mdl.sum(price[i] * x[i] for i in range(n)))

mdl.print_information()
# Model: knapsack
#  - number of variables: 6
#    - binary=6, integer=0, continuous=0
#  - number of constraints: 1
#    - linear=1
#  - parameters: defaults
#  - objective: maximize
#  - problem type is: MILP

mdl.solve()
mdl.print_solution()
# objective: 60
#   x0=1
#   x3=1