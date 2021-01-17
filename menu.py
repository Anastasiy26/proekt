from game import Game
import config as c
from button import Button

class Menu(Game):
    def __init__(self):
        super().__init__('Breakout', c.screen_width, c.screen_height, c.background_image, c.frame_rate)
        self.menu_buttons = []

    def create_menu(self, breakout):
        def on_play(button):
            self.game_over = False
            breakout.__init__()
            breakout.is_game_running = True
            breakout.start_level = True
            breakout.run()

        def on_quit(button):
            self.game_over = True
            self.is_game_running = False
            breakout.is_game_running = False


        for i, (text, click_handler) in enumerate((('PLAY', on_play), ('QUIT', on_quit))):
            b = Button(c.menu_offset_x,
                       c.menu_offset_y + (c.menu_button_h + 5) * i,
                       c.menu_button_w,
                       c.menu_button_h,
                       text,
                       click_handler,
                       padding=5)
            self.objects.append(b)
            self.menu_buttons.append(b)
            self.mouse_handlers.append(b.handle_mouse_event)