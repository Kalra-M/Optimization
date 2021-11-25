import numpy as np
import pickle

n_facility = 10
n_demand = 19

data = np.random.randint(0 , 2, size = (n_facility, n_demand))

indices = np.where(data != 0)

problem_dict = dict()

for node in list(zip(indices[0], indices[1])):
    if node[0] not in problem_dict.keys():
        problem_dict[node[0]] = []
    problem_dict[node[0]].append(node[1])    

cost = np.random.randint(20, 50, size = n_facility)

with open('Problem.pkl', 'wb') as file:
    pickle.dump(problem_dict, file)

with open('Cost.pkl', 'wb') as file:
    pickle.dump(cost, file)
