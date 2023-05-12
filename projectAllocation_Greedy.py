import random

# Example data

students = ['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6', 'Student7', 'Student8', 'Student9', 'Student10',
            'Student11', 'Student12', 'Student13', 'Student14', 'Student15', 'Student16', 'Student17', 'Student18', 'Student19', 'Student20']
projects = ['Project1', 'Project2', 'Project3', 'Project4', 'Project5']
capacities = {'Project1': 1, 'Project2': 5, 'Project3': 3, 'Project4': 10, 'Project5': 4}
preferences = {
    'Student1': ['Project1', 'Project3', 'Project2', 'Project4', 'Project5'],
    'Student2': ['Project1', 'Project2', 'Project3', 'Project4', 'Project5'],
    'Student3': ['Project3', 'Project1', 'Project2', 'Project4', 'Project5'],
    'Student4': ['Project4', 'Project5', 'Project1', 'Project2', 'Project3'],
    'Student5': ['Project5', 'Project4', 'Project3', 'Project2', 'Project1'],
    'Student6': ['Project1', 'Project2', 'Project3', 'Project4', 'Project5'],
    'Student7': ['Project2', 'Project1', 'Project3', 'Project4', 'Project5'],
    'Student8': ['Project3', 'Project1', 'Project2', 'Project4', 'Project5'],
    'Student9': ['Project4', 'Project5', 'Project1', 'Project2', 'Project3'],
    'Student10': ['Project5', 'Project4', 'Project3', 'Project2', 'Project1'],
    'Student11': ['Project1', 'Project3', 'Project2', 'Project4', 'Project5'],
    'Student12': ['Project1', 'Project2', 'Project3', 'Project4', 'Project5'],
    'Student13': ['Project3', 'Project1', 'Project2', 'Project4', 'Project5'],
    'Student14': ['Project4', 'Project5', 'Project1', 'Project2', 'Project3'],
    'Student15': ['Project5', 'Project4', 'Project3', 'Project2', 'Project1'],
    'Student16': ['Project1', 'Project2', 'Project3', 'Project4', 'Project5'],
    'Student17': ['Project2', 'Project1', 'Project3', 'Project4', 'Project5'],
    'Student18': ['Project3', 'Project1', 'Project2', 'Project4', 'Project5'],
    'Student19': ['Project4', 'Project5', 'Project1', 'Project2', 'Project3'],
    'Student20': ['Project5', 'Project4', 'Project3', 'Project2', 'Project1']
}
supervisors = {
    'Project1': 'Supervisor1',
    'Project2': 'Supervisor2',
    'Project3': 'Supervisor2',
    'Project4': 'Supervisor3',
    'Project5': 'Supervisor3'
}
max_load = {
    'Supervisor1': 8,
    'Supervisor2': 11,
    'Supervisor3': 9
}


allocation = {}
workload = {supervisor: 0 for supervisor in max_load}

# Shuffle the student order
random.shuffle(students)

# Allocate projects to students
for student in students:
    for project in preferences[student]:
        if capacities[project] > 0:
            supervisor = supervisors[project]
            if workload[supervisor] < max_load[supervisor]:
                allocation[student] = project
                capacities[project] -= 1
                workload[supervisor] += 1
                break

# Print the allocation
for student, project in allocation.items():
    print(f"{student}: {project}")