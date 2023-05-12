'''
>The function allocate_projects takes input parameters num_students, num_projects, capacities, preferences, and supervisors.
>It initializes two lists, projects and allocation, with initial values. 
>Projects tracks the number of students allocated to each project, and allocation represents the current allocation of projects to students.

'''

def allocate_projects(num_students, num_projects, capacities, preferences, supervisors):
    projects = [0] * num_projects # Track the number of students allocated to each project
    allocation = [-1] * num_students # Initialize allocation array with -1 for unallocated students


      #This is a helper function calculate_score that calculates the score of a given allocation. 
      #It checks if each allocated project is in the student's preference list and increments the score accordingly.
    def calculate_score(allocation):
        score = 0
        for i, project in enumerate(allocation):
            if project != -1 and project in preferences[i]:
                score += 1
        return score


      #This is a recursive helper function branch_and_bound that performs the branch and bound algorithm for project allocation. 
      #It takes the current student as a parameter and accesses the allocation variable from the outer scope using the nonlocal keyword.
    def branch_and_bound(student):
        nonlocal allocation

        # Base case: All students allocated
        if student == num_students:
            return True

        # Try assigning each available project to the current student
        for project in preferences[student]:
            if projects[project] < capacities[project] and supervisors[project] == project:
                projects[project] += 1
                allocation[student] = project

                # Recurse to the next student
                if branch_and_bound(student + 1):
                    return True

                # Backtrack
                projects[project] -= 1
                allocation[student] = -1

        return False

    # Start the branch and bound search
    branch_and_bound(0)

    return allocation

# Example usage
num_students = 15
num_projects = 7
capacities = [3, 2, 3, 2, 2, 3, 2]
preferences = [
    [0, 1, 2, 3, 4, 5, 6],
    [1, 0, 2, 3, 4, 5, 6],
    [2, 0, 1, 3, 4, 5, 6],
    [3, 0, 1, 2, 4, 5, 6],
    [4, 0, 1, 2, 3, 5, 6],
    [5, 0, 1, 2, 3, 4, 6],
    [6, 0, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 6],  
    [0, 1, 2, 3, 4, 5, 6],  
    [0, 1, 2, 3, 4, 5, 6],  
    [0, 1, 2, 3, 4, 5, 6],  
    [0, 1, 2, 3, 4, 5, 6],  
    [0, 1, 2, 3, 4, 5, 6],  
    [0, 1, 2, 3, 4, 5, 6],  
    [0, 1, 2, 3, 4, 5, 6],  

]
supervisors = [0, 1, 2, 3, 4, 5, 6]

allocation = allocate_projects(num_students, num_projects, capacities, preferences, supervisors)

# Print the allocation
for student, project in enumerate(allocation):
    print(f"Student {student+1} is allocated to Project {project+1}" if project != -1 else f"Student {student+1} is not allocated to any project")