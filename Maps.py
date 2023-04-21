import arcade
from characters import Player

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