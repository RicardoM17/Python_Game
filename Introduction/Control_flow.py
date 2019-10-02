# if statements
# if condition:
#       code to execute if condition is true

is_game_over = False
p_pos = 0
obj_pos = 3

p_pos += 2

if p_pos == obj_pos:
    is_game_over = True
elif p_pos > obj_pos:
    is_game_over = False
else:
    is_game_over = False

# Double condition "and" "or"

print(is_game_over)
