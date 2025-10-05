## Linear Programming for Embedded Task Optimization
## ------------------------------------------------
## Scenario:
## In embedded systems (such as IoT devices or microcontrollers), resources like battery, memory, and time are limited.
## The goal is to determine the optimal number of two operations per cycle:
##   - Sensing Task  (collect data)
##   - Reporting Task (send data)
##
## Mathematical Formulation:
## We want to maximize the system utility:
##     Maximize: 5x + 4y
## Where:
##     x = number of sensing tasks per cycle
##     y = number of reporting tasks per cycle
##
## Subject to resource constraints:
##     2x + 3y   <= 20      # Battery usage constraint
##     50x + 100y <= 500    # Memory usage constraint
##     100x + 200y <= 1000  # Time constraint per cycle
##     x, y >= 0            # Tasks cannot be negative
##
## This script uses the PuLP library to model and solve the above LP problem.
## The underlying method is the simplex algorithm (or equivalent).
## ------------------------------------------------

from pulp import LpProblem, LpVariable, LpMaximize

# Create the optimization problem
prob = LpProblem("Embedded_Task_Optimization", LpMaximize)

# Decision variables (number of tasks per cycle)
x = LpVariable('Sensing_Task', lowBound=0, cat='Integer')
y = LpVariable('Reporting_Task', lowBound=0, cat='Integer')

# Objective: maximize utility
prob += 5 * x + 4 * y

# Constraints
prob += 2 * x + 3 * y <= 20      # Battery constraint
prob += 50 * x + 100 * y <= 500  # Memory constraint
prob += 100 * x + 200 * y <= 1000 # Time constraint

# Solve the problem
prob.solve()

# Show results
print("Optimal Sensing Task per cycle:", x.value())
print("Optimal Reporting Task per cycle:", y.value())
print("Maximum Utility:", 5 * x.value() + 4 * y.value())
