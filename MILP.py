from docplex.mp.model import Model

milp = Model(name = 'MILP')

x = {(i): milp.integer_var(name = f'x{i}') for i in range(1,6)}
y = milp.continuous_var(name = 'y')

milp.add_constraint(milp.sum(x[i] for i in range(1,6)) + y <= 20)
milp.add_constraint(milp.sum(i * x[i] for i in range(1,6)) >= 10)
milp.add_constraint(x[5] + 2*y >= 30)
for i in range(1,6):
    milp.add_constraint(x[i] + y >= 15)
    milp.add_constraint(x[i] >= 0)
milp.add_constraint(y >= 0)

milp.minimize(milp.sum(x[i] for i in range(1,6)) + y)

milp.print_information()
# Model: MILP
#  - number of variables: 6
#    - binary=0, integer=5, continuous=1
#  - number of constraints: 14
#    - linear=14
#  - parameters: defaults
#  - objective: minimize
#  - problem type is: MILP


milp.solve()
milp.print_solution()
# objective: 17.000
#   x5=2
#   y=15.000