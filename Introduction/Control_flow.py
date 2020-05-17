# if statements
# if condition:
#       code to execute if condition is true

is_game_over = False
p_pos = 0
obj_pos = 3

p_pos += 1

if p_pos == obj_pos:
    is_game_over = True
elif p_pos > obj_pos:
    is_game_over = False
else:
    is_game_over = False

# Double condition "and" "or"

print(is_game_over)

is_game_over = False
p_x_pos = 2
e_x_pos = 3
end_x_pos = 10
speed = 2

while not is_game_over:
    print(p_x_pos)
    print(e_x_pos)
    if p_x_pos == e_x_pos:
        print('You lose')
        is_game_over = True
    elif p_x_pos >= end_x_pos:
        print('You win')
        is_game_over = True
    else:
        p_x_pos += 3
        e_x_pos += 1


x_pos = 5
movements = [1,-2,6,-3,-2,4]

for movement in movements:
    x_pos += movement
print(x_pos)


    

