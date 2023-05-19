# Summary: Student Project Allocation

The Student Project Allocation code aims to allocate projects to students based on their preferences while minimizing the total penalty. The code uses the PuLP library to create a linear programming model and solve it to obtain an optimal solution.

## Input Data

The input data consists of the following lists:

- A list of students
- A list of projects
- Capacities for each project
- Preferences of each student for each project
- Supervisors for each project
- Maximum load for each supervisor

## Decision Variables

The code creates decision variables to represent whether:

- A student is assigned to a project
- A student is assigned to their preferred project
- A student is assigned to a project that is lower on their preference list than their assigned project.

## Objective Function and Constraints

The objective function is set up to minimize the total penalty, which is calculated based on the number of students assigned to projects that are lower on their preference list. The constraints ensure that:

- Each student is assigned to exactly one project
- Each project does not exceed its capacity
- Each student is assigned to their preferred project if possible
- Each supervisor's load does not exceed their maximum load.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2f06a2ba-920f-4a8d-8e2f-10137872428f/Untitled.png)

## Solution

The code then solves the linear programming model using the simplex algorithm and prints the solution status, allocation results, and total penalty. The allocation results show each student's assigned project and their preference rank for that project.

## Conclusion

In conclusion, the Student Project Allocation code provides an efficient and fair way to allocate projects to students based on their preferences while considering project capacities and supervisor loads. It can be easily adapted to different datasets and used in various educational institutions.

### Submitted by:

> Aryaman Raj - 20cs3011
Astitwa Dwivedi - 20cs3015
Bhawesh Kumar Pandit - 20cs3021
Ishita Srivastava - 20cs3034
Vijeet Nigam - 20cs3068
Manish Wahale - 20cs3070
>
