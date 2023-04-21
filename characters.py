import arcade
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
BLOCK_SIZE = 60
DIRT_TEXTURE = arcade.load_texture("Assets/Texture/SpriteBlock.png")
TUNNEL_TEXTURE = arcade.load_texture("Assets/Texture/SpriteTonnel.png")
class Player(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.texture = arcade.load_texture("Assets/Texture/SpriteCar.png")
        self.center_x = x
        self.center_y = y
        self.speed = 5  # скорость передвижения игрока
        self.change_x = 0
        self.change_y = 0

    def move(self):
        if self.change_x != 0:
            new_x = self.center_x + self.change_x
            if new_x > SCREEN_WIDTH - BLOCK_SIZE / 2:  # обратите внимание на SCREEN_WIDTH и BLOCK_SIZE
                self.center_x = SCREEN_WIDTH - BLOCK_SIZE / 2
            elif new_x < BLOCK_SIZE / 2:
                self.center_x = BLOCK_SIZE / 2
            else:
                self.center_x = new_x
        if self.change_y != 0:
            new_y = self.center_y + self.change_y
            if new_y > SCREEN_HEIGHT - BLOCK_SIZE / 2:
                self.center_y = SCREEN_HEIGHT - BLOCK_SIZE / 2
            elif new_y < BLOCK_SIZE / 2:
                self.center_y = BLOCK_SIZE / 2
            else:
                self.center_y = new_y

    def on_key_press(self, key, modifiers):
        # обработка нажатий клавиш на стрелочки
        if key == arcade.key.LEFT:
            self.change_x = -self.speed
        elif key == arcade.key.RIGHT:
            self.change_x = self.speed
        elif key == arcade.key.UP:
            self.change_y = self.speed
        elif key == arcade.key.DOWN:
            self.change_y = -self.speed

    def on_key_release(self, key, modifiers):
        # обработка отпускания клавиш на стрелочки
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.change_y = 0

player = Player(100, 100)
