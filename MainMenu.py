import arcade
import arcade.gui


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Digger"

class QuitButton(arcade.gui.UIFlatButton): #Создание класса кнопок
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()

class Zastavka(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
        self.background = arcade.load_texture("Assets/Menu/zastavka.png")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        arcade.draw_text("Добро пожаловать в игру DIGGER", SCREEN_WIDTH/2, SCREEN_HEIGHT/2+150, arcade.color.BLACK, font_size=40, anchor_x="center")
        arcade.draw_text("Нажмите Enter, чтобы начать игру", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-150, arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ENTER:
            game_view = GameMenu()
            self.window.show_view(game_view)
class GameMenu(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.BLACK)
        self.background = arcade.load_texture("Assets/Menu/menu.png")
        self.v_box = None

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # Создаем вертикальную BoxGroup для выравнивания кнопок
        self.v_box = arcade.gui.UIBoxLayout()

        # Создаем кнопки
        new_game_button = arcade.gui.UIFlatButton(text="Новая игра", width=200)
        new_game_button.on_click = self.on_newgame_button_click
        self.v_box.add(new_game_button.with_space_around(bottom=20))

        settings_button = arcade.gui.UIFlatButton(text="Настройки", width=200)
        settings_button.on_click = self.on_settings_button_click
        self.v_box.add(settings_button.with_space_around(bottom=20))

        quit_button = QuitButton(text="Выход", width=200)
        self.v_box.add(quit_button)

        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="center_y", child=self.v_box))

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        arcade.draw_text("DIGGER", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200, arcade.color.BLACK, font_size=72, anchor_x="center")
        self.manager.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ESCAPE:
            menu_view = Zastavka()
            self.window.show_view(menu_view)

    def on_settings_button_click(self, event):
        settings_view = SettingsView()
        self.window.show_view(settings_view)

    def on_newgame_button_click(self, event):
        new_game_view = NewGame()
        self.window.show_view(new_game_view)

class SettingsView(arcade.View):
    def __init__(self):
        super().__init__()
        self.v_box = arcade.gui.UIBoxLayout()

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
        self.background = arcade.load_texture("Assets/Menu/menu.png")
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.v_box = None
        self.v_box = arcade.gui.UIBoxLayout()

        back = arcade.gui.UIFlatButton(text="Назад", width=200,)
        back.on_click = self.on_back_button_click
        self.v_box.add(back.with_space_around(bottom=20))
        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="right", anchor_y='bottom', child=back, margin= (10,10,10,10)))

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        arcade.draw_text("Настройки", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150, arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Данная гениальная схема в Альфа тестировании", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 10,
                         arcade.color.BLACK, font_size=20, anchor_x="center")
        self.manager.draw()


    def on_back_button_click(self, event):
        menu_view = GameMenu()
        self.window.show_view(menu_view)





class NewGame(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
        self.background = arcade.load_texture("Assets/Menu/menu.png")
        self.v_box = None
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # Создаем вертикальную BoxGroup для выравнивания кнопок
        self.v_box = arcade.gui.UIBoxLayout()

        # Создаем кнопки
        onelevel = arcade.gui.UIFlatButton(text="1 уровень", width=200)
        self.v_box.add(onelevel.with_space_around(bottom=20))

        twolevel = arcade.gui.UIFlatButton(text="2 уровень", width=200)
        self.v_box.add(twolevel.with_space_around(bottom=20))
        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="center_y", child=self.v_box))

        back = arcade.gui.UIFlatButton(text="Назад", width=200, )
        back.on_click = self.on_backNEW_button_click
        self.v_box.add(back.with_space_around(bottom=20))
        self.manager.add(
            arcade.gui.UIAnchorWidget(anchor_x="right", anchor_y='bottom', child=back, margin=(10, 10, 10, 10)))

    def on_backNEW_button_click(self, event):
        menu_view = GameMenu()
        self.window.show_view(menu_view)



    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        arcade.draw_text("ВЫБОР УРОВНЯ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200, arcade.color.BLACK, font_size=72, anchor_x="center")
        self.manager.draw()


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=False)
    menu_view = Zastavka()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()