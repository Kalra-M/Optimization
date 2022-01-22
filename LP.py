from docplex.mp.model import Model

lp = Model(name = 'LP')

x = lp.continuous_var(name = 'x')
y = lp.continuous_var(name = 'y')

lp.add_constraint(x + y <= 4)
lp.add_constraint(x - y <= 2)
lp.add_constraint(x >= 0)
lp.add_constraint(y >= 0)

lp.maximize(3*x + 2*y)

lp.print_information()
# Model: LP
#  - number of variables: 2
#    - binary=0, integer=0, continuous=2
#  - number of constraints: 4
#    - linear=4
#  - parameters: defaults
#  - objective: maximize
#  - problem type is: LP

lp.solve()
lp.print_solution()
# objective: 11.000
#   x=3.000
#   y=1.000