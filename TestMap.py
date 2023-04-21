import arcade

# Создаем двумерный массив карты
map_data = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ]

# Устанавливаем размеры блоков и окна
block_size = 70
screen_width = 1000
screen_height = 600

class MyView(arcade.View):
    def __init__(self):
        super().__init__()
        self.player_x = 0
        self.player_y = 0
        self.player_texture = None
        self.direction_x = 0
        self.direction_y = 0
        self.background = arcade.load_texture("Assets/Texture/SpriteBlock.png")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.direction_y = 1
        elif key == arcade.key.DOWN:
            self.direction_y = -1
        elif key == arcade.key.LEFT:
            self.direction_x = -1
        elif key == arcade.key.RIGHT:
            self.direction_x = 1

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP and self.direction_y == 1:
            self.direction_y = 0
        elif key == arcade.key.DOWN and self.direction_y == -1:
            self.direction_y = 0
        elif key == arcade.key.LEFT and self.direction_x == -1:
            self.direction_x = 0
        elif key == arcade.key.RIGHT and self.direction_x == 1:
            self.direction_x = 0

    def update(self, delta_time):
        # Смещаем игрока на расстояние, пропорциональное времени между кадрами
        self.player_x += self.direction_x * block_size * delta_time
        self.player_y += self.direction_y * block_size * delta_time

        # Меняем текстуру игрока, чтобы создать эффект движения
        if self.direction_x > 0:
            self.player_texture = arcade.load_texture("Assets/Texture/SpriteCar.png")
        elif self.direction_x < 0:
            self.player_texture = arcade.load_texture("Assets/Texture/SpriteCar.png")
        elif self.direction_y > 0:
            self.player_texture = arcade.load_texture("Assets/Texture/SpriteCar.png")
        elif self.direction_y < 0:
            self.player_texture = arcade.load_texture("Assets/Texture/SpriteCar.png")

    def on_draw(self):
        arcade.start_render()
        for row in range(len(map_data)):
            for col in range(len(map_data[row])):
                # Определяем позицию блока
                x = col * block_size + block_size // 2
                y = row * block_size + block_size // 2

                if map_data[row][col] == 1:
                    arcade.draw_texture_rectangle(x, y, block_size, block_size, self.background)
                elif map_data[row][col] == 0:
                    arcade.draw_rectangle_filled(x, y, block_size, block_size, arcade.color.BLACK)

        arcade.draw_texture_rectangle(self.player_x, self.player_y, block_size, block_size, self.player_texture)

# Запускаем главный цикл
def main():
    window = arcade.Window(screen_width, screen_height, "Digger Map")
    arcade.set_background_color(arcade.color.BLACK)
    view = MyView()
    view.player_x = 3 * block_size + block_size // 2
    view.player_y = 5 * block_size + block_size // 2
    view.player_texture = arcade.load_texture("Assets/Texture/SpriteCar.png")
    window.show_view(view)
    arcade.run()

if __name__ == "__main__":
    main()