import arcade
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
BLOCK_SIZE = 60
DIRT_TEXTURE = arcade.load_texture("Assets/Texture/SpriteBlock.png")

class Map:
    def __init__(self, map_data):
        self.map_data = map_data

    def draw(self):
        top_y = SCREEN_HEIGHT - (len(self.map_data) * BLOCK_SIZE)
        for row in range(len(self.map_data)):
            for col in range(len(self.map_data[0])):
                if self.map_data[row][col] == 1:
                    arcade.draw_texture_rectangle(
                        col * BLOCK_SIZE + BLOCK_SIZE / 2,
                        top_y + row * BLOCK_SIZE + BLOCK_SIZE / 2,
                        BLOCK_SIZE,
                        BLOCK_SIZE,
                        DIRT_TEXTURE
                    )
                else:
                    arcade.draw_rectangle_filled(
                        col * BLOCK_SIZE + BLOCK_SIZE / 2,
                        top_y + row * BLOCK_SIZE + BLOCK_SIZE / 2,
                        BLOCK_SIZE,
                        BLOCK_SIZE,
                        arcade.color.BLACK
                    )
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
def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT,)
    arcade.set_background_color(arcade.color.BLACK)

    # Определение объектов карты и игрока
    map_data = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    game_map = Map(map_data)
    player = Player(3 * BLOCK_SIZE + BLOCK_SIZE / 2, 3 * BLOCK_SIZE + BLOCK_SIZE / 2)

    # Определение функций on_key_press и on_key_release
    def on_key_press(key, modifiers):
        player.on_key_press(key, modifiers)

    def on_key_release(key, modifiers):
        player.on_key_release(key, modifiers)

    # Регистрация функций on_key_press и on_key_release в обработчиках событий
    arcade.get_window().push_handlers(
        on_key_press=on_key_press,
        on_key_release=on_key_release
    )

    def update(delta_time):
        player.move()
        arcade.start_render()
        game_map.draw()
        player.draw()
        arcade.finish_render() # конец пакетной отрисовки

    arcade.schedule(update, 1 / 60)
    arcade.run()


if __name__ == "__main__":
    main()