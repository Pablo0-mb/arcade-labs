import arcade

def draw_cloud(x,y):

    arcade.draw_circle_filled(x, y, 35, [247, 193, 189])
    arcade.draw_circle_filled(x + 50, y, 35, [247, 193, 189])
    arcade.draw_circle_filled(x + 100, y, 35, [247, 193, 189])
    arcade.draw_circle_filled(x + 150, y, 35, [247, 193, 189])

    arcade.draw_circle_filled(x + 25, y + 25, 30, [247, 193, 189])
    arcade.draw_circle_filled(x + 75, y + 25, 30, [247, 193, 189])
    arcade.draw_circle_filled(x + 125, y + 25, 30, [247, 193, 189])

    arcade.draw_circle_filled(x + 25, y - 25, 30, [247, 193, 189])
    arcade.draw_circle_filled(x + 75, y - 25, 30, [247, 193, 189])
    arcade.draw_circle_filled(x + 125, y - 25, 30, [247, 193, 189])


def draw_sky():
    arcade.draw_lrtb_rectangle_filled(0, 1000, 600, 500, [247, 103, 91])
    arcade.draw_lrtb_rectangle_filled(0, 1000, 500, 400, [247, 120, 109])
    arcade.draw_lrtb_rectangle_filled(0, 1000, 400, 300, [247, 135, 126])
    arcade.draw_lrtb_rectangle_filled(0, 1000, 300, 200, [247, 157, 150])
    arcade.draw_lrtb_rectangle_filled(0, 1000, 200, 100, [247, 167, 160])
    arcade.draw_lrtb_rectangle_filled(0, 1000, 100, 0, [247, 179, 173])

    arcade.draw_circle_filled(490, 310, 75, [247, 103, 91])

def draw_bird(x,y):
    arcade.draw_arc_outline(x, y, 30, 15, arcade.color.BLACK, 0, 180, 5)
    arcade.draw_arc_outline(x + 30, y, 30, 15, arcade.color.BLACK, 0, 180, 5)

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


def on_draw(delta_time):
    arcade.start_render()
    draw_sky()

    draw_cloud(on_draw.cloud1_x+25, 500)
    draw_cloud(on_draw.cloud1_x + 250, 450)
    draw_cloud(on_draw.cloud1_x + 700, 450)
    draw_cloud(on_draw.cloud1_x + 350, 275)
    draw_cloud(on_draw.cloud1_x + 475, 250)

    draw_bird(on_draw.bird1_x, 500)
    draw_bird(on_draw.bird1_x-50, 470)
    draw_bird(on_draw.bird1_x-100, 440)
    draw_bird(on_draw.bird1_x-50, 530)
    draw_bird(on_draw.bird1_x-100, 560)
    draw_bird(on_draw.bird1_x+500, 400)
    draw_bird(on_draw.bird1_x+450, 375)
    draw_bird(on_draw.bird2_x+700, 325)

    draw_building(0, 0)
    draw_building(150, -35)
    draw_building(300, -15)
    draw_building(450, -150)
    draw_building(600, -75)
    draw_building(750, -30)
    draw_building(900, -5)

    draw_highway()

    on_draw.cloud1_x += 0.1
    on_draw.bird1_x += 1
    on_draw.bird2_x -= 1

on_draw.cloud1_x = 0
on_draw.bird1_x = 0
on_draw.bird2_x = 0

def main():
    arcade.open_window(1000, 600, "Drawing Example")
    arcade.set_background_color(arcade.color.AERO_BLUE)

    arcade.schedule(on_draw, 1 / 60)
    arcade.run()

main()
