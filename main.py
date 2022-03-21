import arcade


WIDTH = 800
HEIGHT = 600


class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

        self.playerx = 400
        self.playery = 350
        self.speedx1 = 400
        self.speedy1 = 400

        self.player_list = arcade.SpriteList()
        self.player = arcade.AnimatedWalkingSprite()

        self.player.frames = []

        self.player_list.append(self.player)

        self.player.stand_right_textures = []
        self.player.stand_right_textures.append(arcade.load_texture('Diablo/Ход вправо/Стоит вправо.png'))

        self.player.walk_right_textures = []
        self.player.walk_right_textures.append(arcade.load_texture('Diablo/Ход вправо/D25.png'))
        self.player.walk_right_textures.append(arcade.load_texture('Diablo/Ход вправо/D26.png'))
        self.player.walk_right_textures.append(arcade.load_texture('Diablo/Ход вправо/D27.png'))
        self.player.walk_right_textures.append(arcade.load_texture('Diablo/Ход вправо/D28.png'))
        self.player.walk_right_textures.append(arcade.load_texture('Diablo/Ход вправо/D29.png'))
        self.player.walk_right_textures.append(arcade.load_texture('Diablo/Ход вправо/D30.png'))
        self.player.walk_right_textures.append(arcade.load_texture('Diablo/Ход вправо/D31.png'))
        self.player.walk_right_textures.append(arcade.load_texture('Diablo/Ход вправо/D32.png'))

        self.player.stand_left_textures = []
        self.player.stand_left_textures.append(arcade.load_texture('Diablo/Ход влево/Стоит влево.png'))

        self.player.walk_left_textures.append(arcade.load_texture('Diablo/Ход влево/D9.png'))
        self.player.walk_left_textures.append(arcade.load_texture('Diablo/Ход влево/D10.png'))
        self.player.walk_left_textures.append(arcade.load_texture('Diablo/Ход влево/D11.png'))
        self.player.walk_left_textures.append(arcade.load_texture('Diablo/Ход влево/D12.png'))
        self.player.walk_left_textures.append(arcade.load_texture('Diablo/Ход влево/D13.png'))
        self.player.walk_left_textures.append(arcade.load_texture('Diablo/Ход влево/D14.png'))
        self.player.walk_left_textures.append(arcade.load_texture('Diablo/Ход влево/D15.png'))
        self.player.walk_left_textures.append(arcade.load_texture('Diablo/Ход влево/D16.png'))

        self.player.stand_up_textures = []
        self.player.stand_up_textures.append(arcade.load_texture('Diablo/Ход вперед/Стоит вперед.png'))

        self.player.walk_up_textures.append(arcade.load_texture('Diablo/Ход вперед/D17.png'))
        self.player.walk_up_textures.append(arcade.load_texture('Diablo/Ход вперед/D18.png'))
        self.player.walk_up_textures.append(arcade.load_texture('Diablo/Ход вперед/D19.png'))
        self.player.walk_up_textures.append(arcade.load_texture('Diablo/Ход вперед/D20.png'))
        self.player.walk_up_textures.append(arcade.load_texture('Diablo/Ход вперед/D21.png'))
        self.player.walk_up_textures.append(arcade.load_texture('Diablo/Ход вперед/D22.png'))
        self.player.walk_up_textures.append(arcade.load_texture('Diablo/Ход вперед/D23.png'))
        self.player.walk_up_textures.append(arcade.load_texture('Diablo/Ход вперед/D24.png'))

        self.player.stand_down_textures = []
        self.player.stand_down_textures.append(arcade.load_texture('Diablo/Ход вниз/Стоит.png'))

        self.player.walk_down_textures.append(arcade.load_texture('Diablo/Ход вниз/D1.png'))
        self.player.walk_down_textures.append(arcade.load_texture('Diablo/Ход вниз/D2.png'))
        self.player.walk_down_textures.append(arcade.load_texture('Diablo/Ход вниз/D3.png'))
        self.player.walk_down_textures.append(arcade.load_texture('Diablo/Ход вниз/D4.png'))
        self.player.walk_down_textures.append(arcade.load_texture('Diablo/Ход вниз/D5.png'))
        self.player.walk_down_textures.append(arcade.load_texture('Diablo/Ход вниз/D6.png'))
        self.player.walk_down_textures.append(arcade.load_texture('Diablo/Ход вниз/D7.png'))
        self.player.walk_down_textures.append(arcade.load_texture('Diablo/Ход вниз/D8.png'))


        self.player.center_x = 400
        self.player.center_y = 300

        self.player.scale = 1.5

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()


    def on_update(self, delta_time):
        self.player_list.update()
        self.player_list.update_animation()

    def on_key_press(self, symbol, modifiers):

        if symbol == arcade.key.RIGHT:
            self.player.change_x = 10
        elif symbol == arcade.key.LEFT:
            self.player.change_x = -10
        elif symbol == arcade.key.UP:
            self.player.change_y = 10
        elif symbol == arcade.key.DOWN:
            self.player.change_y = -10

    def on_key_release(self, symbol, modifiers):

        if symbol == arcade.key.RIGHT or symbol == arcade.key.LEFT:
            self.player.change_x = 0
        if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
            self.player.change_y = 0

def main():

    game = MyGame(WIDTH, HEIGHT)
    arcade.run()

main()





