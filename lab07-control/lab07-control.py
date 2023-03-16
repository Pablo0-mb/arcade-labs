""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3

def draw_sky():
    arcade.draw_lrtb_rectangle_filled(0, 1000, 600, 500, [247, 103, 91])
    arcade.draw_lrtb_rectangle_filled(0, 1000, 500, 400, [247, 120, 109])
    arcade.draw_lrtb_rectangle_filled(0, 1000, 400, 300, [247, 135, 126])
    arcade.draw_lrtb_rectangle_filled(0, 1000, 300, 200, [247, 157, 150])
    arcade.draw_lrtb_rectangle_filled(0, 1000, 200, 100, [247, 167, 160])
    arcade.draw_lrtb_rectangle_filled(0, 1000, 100, 0, [247, 179, 173])

    arcade.draw_circle_filled(490, 310, 75, [247, 103, 91])

def draw_building(x,y):
    arcade.draw_lrtb_rectangle_filled(x,150+x,300+y,y,[40,40,40])
    j=5
    for i in range(4):
        arcade.draw_lrtb_rectangle_filled(x+j,x+31+j, y+290, y+250, [100,100,100])
        arcade.draw_lrtb_rectangle_filled(x+j,x+31+j, y+240, y+200, [100, 100, 100])
        arcade.draw_lrtb_rectangle_filled(x+j,x+31+j, y+190, y+150, [100, 100, 100])
        arcade.draw_lrtb_rectangle_filled(x+j,x+31+j, y+140, y+100, [100, 100, 100])
        j += 36

def draw_highway():
    arcade.draw_lrtb_rectangle_filled(0, 1000, 75, 0, [50, 50, 50])
    arcade.draw_lrtb_rectangle_filled(0, 1000, 75, 72, [30, 30, 30])
    arcade.draw_lrtb_rectangle_filled(-50, 100, 40, 35, [200, 200, 200])
    arcade.draw_lrtb_rectangle_filled(150, 300, 40, 35, [200, 200, 200])
    arcade.draw_lrtb_rectangle_filled(350, 500, 40, 35, [200, 200, 200])
    arcade.draw_lrtb_rectangle_filled(550, 700, 40, 35, [200, 200, 200])
    arcade.draw_lrtb_rectangle_filled(750, 900, 40, 35, [200, 200, 200])
    arcade.draw_lrtb_rectangle_filled(950, 1100, 40, 35, [200, 200, 200])

class Bird:
    def __init__(self, position_x, position_y, escala, color):

        self.position_x = position_x
        self.position_y = position_y
        self.escala = escala
        self.color = color

    def draw(self):
        arcade.draw_arc_outline(self.position_x, self.position_y, 30*self.escala, 15*self.escala, self.color, 0, 180, 5*self.escala)
        arcade.draw_arc_outline(self.position_x + 30*self.escala, self.position_y, 30*self.escala, 15*self.escala, self.color, 0, 180, 5*self.escala)

class Cloud:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius+5, self.color)
        arcade.draw_circle_filled(self.position_x + 50, self.position_y, self.radius+5, self.color)
        arcade.draw_circle_filled(self.position_x + 100, self.position_y, self.radius+5, self.color)
        arcade.draw_circle_filled(self.position_x + 150, self.position_y, self.radius+5, self.color)

        arcade.draw_circle_filled(self.position_x + 25, self.position_y + 25, self.radius, self.color)
        arcade.draw_circle_filled(self.position_x + 75, self.position_y + 25, self.radius, self.color)
        arcade.draw_circle_filled(self.position_x + 125, self.position_y + 25, self.radius, self.color)

        arcade.draw_circle_filled(self.position_x + 25, self.position_y - 25, self.radius, self.color)
        arcade.draw_circle_filled(self.position_x + 75, self.position_y - 25, self.radius, self.color)
        arcade.draw_circle_filled(self.position_x + 125, self.position_y - 25, self.radius, self.color)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.set_mouse_visible(False)

        self.bird = Bird(50, 50, 2, arcade.color.BLACK)

        self.cloud = Cloud(50, 50, 0, 0, 30, [247, 193, 189])

    def on_draw(self):
        arcade.start_render()

        #Background
        draw_sky()
        draw_building(0, 0)
        draw_building(150, -35)
        draw_building(300, -15)
        draw_building(450, -150)
        draw_building(600, -75)
        draw_building(750, -30)
        draw_building(900, -5)
        draw_highway()

        self.bird.draw()
        self.cloud.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.bird.position_x = x
        self.bird.position_y = y

    def update(self, delta_time):
        self.cloud.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.cloud.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.cloud.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.cloud.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.cloud.change_y = -MOVEMENT_SPEED


    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.cloud.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.cloud.change_y = 0


def main():
    window = MyGame()
    arcade.run()

main()