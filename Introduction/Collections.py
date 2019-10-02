# Collections
# Tuples, arrays/lists, dictionaries

# Tuple () - Assignment
size = (100,200)

# Accessing 
width = size[0]
height = size[1]

# With tuples it's not possible to modify, delete or add values.
# To add we need to create a new tuple based on a previous one.
new_size = size + (300,) # add another value to the tuple new_size = (100,200,300)

len(size)   # = 2
max(size)   # = 200
min(size)   # = 100
does_contain = 100 in size  # Boolean - Check for value. = True


# Array or List []
movement = [5, -2, -3, 4, -1]

# With arrays it is possible to change a certain value
movement[0] = 7     # movement = [7, -2, -3, 4, -1]

# Add value to end of array
movement.append(-5) # movement = [7, -2, -3, 4, -1, -5]
movement.remove(-3) # movement = [7, -2, 4, -1, -5]     Note: It removes the value -3 not the index...



# Dictionaries - Based on "key"
# Assignment
starting_pos = {'player0': 50, 'player1': 100, 'player2': 0}

# Accessing
starting_pos['player_1']    # = 100
starting_pos.keys()         # returns an array with all the keys
starting_pos.values()       # returns an array with all the values
