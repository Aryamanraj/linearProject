from pulp import *

# Example data
students = ['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6', 'Student7', 'Student8', 'Student9',
            'Student10', 'Student11', 'Student12']
projects = ['Project1', 'Project2', 'Project3', 'Project4', 'Project5', 'Project6', 'Project7', 'Project8', 'Project9',
            'Project10']
capacities = {'Project1': 2, 'Project2': 3, 'Project3': 2, 'Project4': 2, 'Project5': 1, 'Project6': 1, 'Project7': 3,
              'Project8': 2, 'Project9': 1, 'Project10': 2}
preferences = {
    'Student1': ['Project2', 'Project3', 'Project1', 'Project4', 'Project5', 'Project6', 'Project7', 'Project8',
                 'Project9', 'Project10'],
    'Student2': ['Project1', 'Project2', 'Project3', 'Project4', 'Project5', 'Project6', 'Project7', 'Project8',
                 'Project9', 'Project10'],
    'Student3': ['Project9', 'Project5', 'Project1', 'Project2', 'Project4', 'Project6', 'Project7', 'Project8',
                 'Project3', 'Project10'],
    'Student4': ['Project4', 'Project5', 'Project1', 'Project2', 'Project3', 'Project6', 'Project7', 'Project8',
                 'Project9', 'Project10'],
    'Student5': ['Project5', 'Project4', 'Project3', 'Project2', 'Project1', 'Project6', 'Project7', 'Project8',
                 'Project9', 'Project10'],
    'Student6': ['Project6', 'Project7', 'Project8', 'Project9', 'Project10', 'Project1', 'Project2', 'Project3',
                 'Project4', 'Project5'],
    'Student7': ['Project7', 'Project6', 'Project5', 'Project4', 'Project3', 'Project2', 'Project1', 'Project8',
                 'Project9', 'Project10'],
    'Student8': ['Project8', 'Project9', 'Project10', 'Project1', 'Project2', 'Project3', 'Project4', 'Project5',
                 'Project6', 'Project7'],
    'Student9': ['Project9', 'Project10', 'Project1', 'Project2', 'Project3', 'Project4', 'Project5', 'Project6',
                 'Project7', 'Project8'],
    'Student10': ['Project10', 'Project9', 'Project8', 'Project7', 'Project6', 'Project5', 'Project4', 'Project3',
                  'Project2', 'Project1'],
    'Student11': ['Project10', 'Project9', 'Project8', 'Project7', 'Project6', 'Project5', 'Project4', 'Project3',
                  'Project2', 'Project1'],
    'Student12': ['Project1', 'Project2', 'Project3', 'Project4', 'Project5', 'Project6', 'Project7', 'Project8',
                  'Project9', 'Project10']
}

supervisors = {
    'Project1': 'Supervisor1',
    'Project2': 'Supervisor2',
    'Project3': 'Supervisor3',
    'Project4': 'Supervisor4',
    'Project5': 'Supervisor5',
    'Project6': 'Supervisor6',
    'Project7': 'Supervisor7',
    'Project8': 'Supervisor8',
    'Project9': 'Supervisor9',
    'Project10': 'Supervisor10'
}


max_load = {
    'Supervisor1': 3,
    'Supervisor2': 4,
    'Supervisor3': 3,
    'Supervisor4': 4,
    'Supervisor5': 3,
    'Supervisor6': 4,
    'Supervisor7': 3,
    'Supervisor8': 4,
    'Supervisor9': 3,
    'Supervisor10': 4
}



# Create the model
model = LpProblem("Student Project Allocation", LpMinimize)

# Create decision variables


x = LpVariable.dicts("x", [(i, j) for i in students for j in projects], cat='Binary')
y = LpVariable.dicts("y", [(i, j) for i in students for j in projects], cat='Binary')
z = LpVariable.dicts("z", [(i, j) for i in students for j in projects], cat='Binary')

# Set up the objective function
# Set up the objective function
penalty_1 = lpSum(x[i, j] for i in students for j in projects if j == preferences[i][0])
penalty_2 = lpSum(x[i, j] for i in students for j in projects if j == preferences[i][1])
penalty_3 = lpSum(x[i, j] for i in students for j in projects if j == preferences[i][2])
penalty_4 = lpSum(x[i, j] for i in students for j in projects if j == preferences[i][3])
penalty_5 = lpSum(x[i, j] for i in students for j in projects if j == preferences[i][4])
penalty_6 = lpSum(x[i, j] for i in students for j in projects if j == preferences[i][5])
penalty_7 = lpSum(x[i, j] for i in students for j in projects if j == preferences[i][6])
penalty_8 = lpSum(x[i, j] for i in students for j in projects if j == preferences[i][7])
penalty_9 = lpSum(x[i, j] for i in students for j in projects if j == preferences[i][8])
penalty_10 = lpSum(x[i, j] for i in students for j in projects if j == preferences[i][9])

model += 1 * penalty_2 + 3 * penalty_3 + 10 * penalty_4 + 10 * penalty_5 + 10 * penalty_6 + 10 * penalty_7 + 10 * penalty_8 + 10 * penalty_9 + 10 * penalty_10, "Total_Penalty"

# Set up the constraints
for i in students:
    model += lpSum(x[i, j] for j in projects) == 1, f"Assignment Constraint ({i})"

for j in projects:
    model += lpSum(x[i, j] for i in students) <= capacities[j], f"Capacity Constraint ({j})"
for i in students:
    for j in projects:
        model += z[i, j] >= x[i, j] - y[i, j], f"Preference Constraint ({i}, {j})"
for i in students:
    model += lpSum(x[i, j] for j in projects) == 1, f"Exactly_One_Project_Constraint ({i})"



constraint_counter = {}
for s in supervisors.values():
    if s not in constraint_counter:
        constraint_counter[s] = 1
    else:
        constraint_counter[s] += 1
    constraint_name = f"Supervisor_Load_Constraint_{s.replace(' ', '')}{constraint_counter[s]}"
    model += lpSum(x[i, j] for i in students for j in projects if supervisors[j] == s) <= max_load[s], constraint_name

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