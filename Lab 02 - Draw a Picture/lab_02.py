import arcade
arcade.open_window(600, 600, "Landscape")
# Draw the sky
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
arcade.start_render()

# Draw the grass
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)

# Draw the mountains
arcade.draw_triangle_filled(0, 200, 150, 450, 300, 200, arcade.color.MAROON)
arcade.draw_triangle_filled(300, 200, 450, 450, 600, 200, arcade.color.MAROON)

# Draw the sun
arcade.draw_circle_filled(300, 450, 50, arcade.color.YELLOW)

# Draw the river
arcade.draw_rectangle_filled(300, 150, 50, 100, arcade.color.BLUE)

# Draw the lake
arcade.draw_circle_filled(300, 50, 100, arcade.color.BLUE)
arcade.draw_circle_filled(400, 80, 75, arcade.color.BLUE)
arcade.draw_circle_filled(200, 80, 75, arcade.color.BLUE)
arcade.draw_circle_filled(475, 75, 50, arcade.color.BLUE)

# Draw the tree
arcade.draw_rectangle_filled(50, 45, 20, 70, arcade.color.MAROON)
arcade.draw_circle_filled(50, 115, 45, arcade.color.GREEN)

# Draw the cloud
arcade.draw_circle_filled(450, 525, 35, arcade.color.WHITE_SMOKE)
arcade.draw_circle_filled(485, 520, 30, arcade.color.WHITE_SMOKE)
arcade.draw_circle_filled(415, 520, 25, arcade.color.WHITE_SMOKE)

arcade.finish_render()
arcade.run()