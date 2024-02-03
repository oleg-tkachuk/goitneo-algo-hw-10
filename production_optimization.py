import pulp as plp

# Declaring variables for the number of products produced
lemonade = plp.LpVariable("Lemonade", 0, None, plp.LpInteger)
fruit_juice = plp.LpVariable("Fruit juice", 0, None, plp.LpInteger)

# Create a maximization model
model = plp.LpProblem("Maximizing beverage production", plp.LpMaximize)

# Add a goal function: maximize the total number of products
model += lemonade + fruit_juice

# Add restrictions for ingredients
model += 2*lemonade + 1*fruit_juice <= 100, "Water limitations"
model += 1*lemonade <= 50, "Sugar limitations"
model += 1*lemonade <= 30, "Limitations of lemon juice"
model += 2*fruit_juice <= 40, "Limitations of fruit puree"

# Solving the problem
model.solve()

# Displaying the results
lemonade_qty = lemonade.varValue
fruit_juice_qty = fruit_juice.varValue
total_products = lemonade_qty + fruit_juice_qty

print(f"Homework 10 - Task 1 | The quantity of lemonade: {lemonade_qty}") 
print(f"Homework 10 - Task 1 | The quantity of fruit juice: {fruit_juice_qty}")
print(f"Homework 10 - Task 1 | Total products: {total_products}")
