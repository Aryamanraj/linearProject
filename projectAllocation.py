from pulp import *

# Example data
students = ['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6']
projects = ['Project1', 'Project2', 'Project3', 'Project4', 'Project5']
capacities = {'Project1': 1, 'Project2': 1, 'Project3': 1, 'Project4': 2, 'Project5': 1}
preferences = {
    'Student1': ['Project1', 'Project3', 'Project4', 'Project5', 'Project2'],
    'Student2': ['Project1', 'Project2', 'Project3', 'Project4', 'Project5'],
    'Student3': ['Project3', 'Project1', 'Project2', 'Project4', 'Project5'],
    'Student4': ['Project4', 'Project5', 'Project1', 'Project2', 'Project3'],
    'Student5': ['Project5', 'Project4', 'Project3', 'Project2', 'Project1'],
    'Student6': ['Project5', 'Project4', 'Project3', 'Project2', 'Project1']
}
supervisors = {
    'Project1': 'Supervisor1',
    'Project2': 'Supervisor2',
    'Project3': 'Supervisor2',
    'Project4': 'Supervisor3',
    'Project5': 'Supervisor3'
}
max_load = {
    'Supervisor1': 2,
    'Supervisor2': 3,
    'Supervisor3': 3
}

# Create the model
model = LpProblem("Student Project Allocation", LpMinimize)

# Create decision variables
x = LpVariable.dicts("x", [(i, j) for i in students for j in projects], cat='Binary')
y = LpVariable.dicts("y", [(i, j) for i in students for j in projects], cat='Binary')
z = LpVariable.dicts("z", [(i, j) for i in students for j in projects], cat='Binary')

# Set up the objective function
penalty_1 = lpSum(x[i, j] for i in students for j in projects if j != preferences[i][0])
penalty_2 = lpSum(z[i, j] for i in students for j in projects if j == preferences[i][1])
penalty_3 = lpSum(z[i, j] for i in students for j in projects if j == preferences[i][2])
model += 1 * penalty_1 + 2 * penalty_2 + 3 * penalty_3, "Total_Penalty"

# Set up the constraints
for i in students:
    model += lpSum(x[i, j] for j in projects) == 1, f"Minimum Assignment Constraint ({i})"
    for j in projects:
        model += z[i, j] >= x[i, j] - y[i, j], f"Preference Constraint ({i}, {j})"
for j in projects:
    model += lpSum(x[i, j] for i in students) <= capacities[j], f"Capacity Constraint ({j})"
constraint_counter = {}
for s in supervisors.values():
    if s not in constraint_counter:
        constraint_counter[s] = 1
    else:
        constraint_counter[s] += 1
    constraint_name = f"Supervisor_Load_Constraint_{s.replace(' ', '')}{constraint_counter[s]}"
    model += lpSum(x[i, j] for i in students for j in projects if supervisors[j] == s) <= max_load[s], constraint_name

# Solve the model

# Solve the model
model.solve()

# Print the solution status
print("Status:", LpStatus[model.status])

# Print the allocation results
for i in students:
    assigned_project = next((j for j in projects if value(x[i, j]) == 1), None)
    if assigned_project:
        preference = preferences[i].index(assigned_project) + 1
        print(f"{i} is assigned to {assigned_project} as the {preference} preference.")
    else:
        print(f"{i} is not assigned to any project.")

# Print the total penalty
print("Total Penalty:", value(model.objective))