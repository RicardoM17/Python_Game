# Classes and objects

class GameCharacter:

    speed = 5

    def __init__(self, name, width, height, x_pos, y_pos):
        self.name = name
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, x_movement, y_movement):
        self.x_pos += x_movement
        self.y_pos += y_movement
        


character_0 = GameCharacter('Alice', 50, 100, 100, 100)
print(character_0.name)

character_0.name = 'Bob'
print(character_0.name)

character_0.move(50,100)
print(character_0.x_pos)
print(character_0.y_pos)

# subclasses

class PlayerCharacter(GameCharacter):

    speed = 10

    def __init__(self, name, x_pos, y_pos):
        super().__init__(name, 100, 100, x_pos, y_pos)

    def move(self, y_movement):
        super().move(0, y_movement)

player_character = PlayerCharacter('P_character', 500, 500)

print(player_character.name)
player_character.move(100)
print(player_character.x_pos)
print(player_character.y_pos)

    
