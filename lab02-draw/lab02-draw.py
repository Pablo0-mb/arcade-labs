import arcade
import random

arcade.open_window(1000, 600, "Drawing Example")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

# Sky
arcade.draw_lrtb_rectangle_filled(0, 1000, 600, 500, [247,103,91])
arcade.draw_lrtb_rectangle_filled(0, 1000, 500, 400, [247,120,109])
arcade.draw_lrtb_rectangle_filled(0, 1000, 400, 300, [247,135,126])
arcade.draw_lrtb_rectangle_filled(0, 1000, 300, 200, [247,157,150])
arcade.draw_lrtb_rectangle_filled(0, 1000, 200, 100, [247,167,160])

arcade.draw_circle_filled(490, 110, 75, [247,103,91])

# Cloud1

for i in range(4):
    x = random.randint(50,950)
    y = random.randint(200,500)

    arcade.draw_circle_filled(x, y, 35, [247, 193, 189])
    arcade.draw_circle_filled(x+50, y, 35, [247, 193, 189])
    arcade.draw_circle_filled(x+100, y, 35, [247, 193, 189])
    arcade.draw_circle_filled(x+150, y, 35, [247, 193, 189])

    arcade.draw_circle_filled(x+25, y+25, 30, [247, 193, 189])
    arcade.draw_circle_filled(x+75, y+25, 30, [247, 193, 189])
    arcade.draw_circle_filled(x+125, y+25, 30, [247, 193, 189])

    arcade.draw_circle_filled(x+25, y-25, 30, [247, 193, 189])
    arcade.draw_circle_filled(x+75, y-25, 30, [247, 193, 189])
    arcade.draw_circle_filled(x+125, y-25, 30, [247, 193, 189])



# Sea
arcade.draw_lrtb_rectangle_filled(0, 1000, 100, 0, [84,118,131])
arcade.draw_ellipse_outline(490, 50, 150, 75, [126,167,183], 75, 180, -1)


# Birds
for i in range(5):
    x = random.randint(50, 950)
    y = random.randint(200, 500)

    arcade.draw_arc_outline(x, y, 50, 15, arcade.color.BLACK, 0, 180, 10)
    arcade.draw_arc_outline(x+50, y, 50, 15, arcade.color.BLACK, 0, 180, 10)


arcade.finish_render()
arcade.run()
