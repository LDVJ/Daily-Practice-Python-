# # Create variables for:
# Your age
# Current year
# Number of siblings
# Print each with its type.

# your_age = 23
# current_year = 2026
# num_siblings = 2

# print("Your age:", your_age, "Type: ", type(your_age))
# print("Current year:", current_year,"Type: ", type(current_year))
# print("Number of siblings:", num_siblings,"Type: ", type(num_siblings))

#======================================================================#

# You have 50 students and need groups of 6.
# How many complete groups?
# How many students left over?
# Write code to calculate this.

# students = 50
# groups_size = 6

# complete_groups = students // groups_size 
# print("Complete Groups: ", complete_groups)

# remaining_students = students % groups_size
# print("Remaining Students: ", remaining_students)


#======================================================================#

# Calculate total with tax:
# Price: $50.00
# Tax rate: 8.5%
# Formula: total = price × (1 + tax_rate/100)

# price = 50
# tax_rate = 8.5

# total = price * (1 + (tax_rate/100))
# print(f'Total: ${total}')

#======================================================================#

# Calculate BMI:
# Formula: BMI = weight(kg) / height(m)²
# Weight: 70 kg
# Height: 1.75 m
# Round to 2 decimal places

weight = 70
height = 1.75
bmi = weight/(height**2)
print(f'BMI: {round(bmi,2)}')

#======================================================================#

# first = "Alice"
# middle = "Marie"
# last = "Johnson"
# # Output: "Alice Marie Johnson"

# first = "Alice"
# middle = "Marie"
# last = "Johnson"

# print(f'{first} {middle} {last}')

#======================================================================#

# Create a simple game state:
# is_game_over = False
# player_alive = True
# has_won = False
# Print game status.

# is_game_over = False
# is_player_alive = True
# has_won = False

# print("Game Over: ", is_game_over)
# print("Player Alive: ",is_player_alive)
# print("Won: ",has_won)

# your_age = 23
# current_year = 2026
# num_siblings = 2

# print(f'Your age: {your_age}, Type: {type(your_age)}')
# print(f'Current year: {current_year}, Type: {type(current_year)}')
# print(f'Number of siblings: {num_siblings}, Type: {type(num_siblings)}')