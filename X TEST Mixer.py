import cairo
import push2_python

from display_utils import draw_potentiometer, draw_xr18_button, draw_mute_button

x_air = {'trm': 96, 'bas': 96, 'gtr': 96, 'v1': 96, 'v2': 96, 'bt': 96, 'delay': 96, 'reverb': 96}

x_air_button = {'trm': 0, 'bas': 0, 'gtr': 0, 'v1': 0, 'v2': 0, 'bt': 0, 'delay': 0, 'reverb': 0}

mute_value_list = {'trm': 127, 'bas': 127, 'gtr': 127, 'v1': 127, 'v2': 127, 'bt': 127, 'delay': 127, 'reverb': 127}

w, h = push2_python.constants.DISPLAY_LINE_PIXELS, push2_python.constants.DISPLAY_N_LINES
surface = cairo.ImageSurface(cairo.FORMAT_RGB16_565, w, h)
ctx = cairo.Context(surface)

# Start of drawing code

# Initial black rectangle
ctx.rectangle(0, 0, w, h)
ctx.set_source_rgb(0, 0, 0)
ctx.fill()

# Colors
screen_black = [0, 0, 0]
screen_dark = [0.05, 0.05, 0.05]

# Globals
rad = 45
line = 10
center_y = 75

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Instrument QUASI-GLOBALS


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
text = "ALBIN"
control = x_air['trm']
mute_value = mute_value_list['trm']
xr18_button = x_air_button['trm']
center_x = 60
x = center_x
color = [1, 1, 0]

draw_xr18_button(ctx, x, xr18_button, text, color)
draw_potentiometer(ctx, x, control, mute_value, color)
draw_mute_button(ctx, x, mute_value, color)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
text = "NOAH"
control = x_air['bas']
mute_value = mute_value_list['bas']
xr18_button = x_air_button['bas']
center_x = 180
x = center_x
color = [0, 1, 0.5]

draw_xr18_button(ctx, x, xr18_button, text, color)
draw_potentiometer(ctx, x, control, mute_value, color)
draw_mute_button(ctx, x, mute_value, color)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
text = "FREDRIK"
control = x_air['gtr']
mute_value = mute_value_list['gtr']
xr18_button = x_air_button['gtr']
center_x = 300
x = center_x
color = [0, 0.5, 1]

draw_xr18_button(ctx, x, xr18_button, text, color)
draw_potentiometer(ctx, x, control, mute_value, color)
draw_mute_button(ctx, x, mute_value, color)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
text = "MARIA"
control = x_air['v1']
mute_value = mute_value_list['v1']
xr18_button = x_air_button['v1']
center_x = 420
x = center_x
color = [1, 0.25, 0.5]

draw_xr18_button(ctx, x, xr18_button, text, color)
draw_potentiometer(ctx, x, control, mute_value, color)
draw_mute_button(ctx, x, mute_value, color)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
text = "MICHELLE"
control = x_air['v2']
mute_value = mute_value_list['v2']
xr18_button = x_air_button['v2']
center_x = 540
x = center_x
color = [0.875, 0, 1]

draw_xr18_button(ctx, x, xr18_button, text, color)
draw_potentiometer(ctx, x, control, mute_value, color)
draw_mute_button(ctx, x, mute_value, color)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
text = "NIKLAS"
control = x_air['bt']
mute_value = mute_value_list['bt']
xr18_button = x_air_button['bt']
center_x = 660
x = center_x
color = [0.75, 0.75, 0.75]

draw_xr18_button(ctx, x, xr18_button, text, color)
draw_potentiometer(ctx, x, control, mute_value, color)
draw_mute_button(ctx, x, mute_value, color)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
text = "REVERB"
control = x_air['reverb']
mute_value = mute_value_list['reverb']
xr18_button = x_air_button['reverb']
center_x = 780
x = center_x
color = [0.25, 0.75, 1]

draw_xr18_button(ctx, x, xr18_button, text, color)
draw_potentiometer(ctx, x, control, mute_value, color)
draw_mute_button(ctx, x, mute_value, color)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
text = "DELAY"
control = x_air['delay']
mute_value = mute_value_list['delay']
xr18_button = x_air_button['delay']
center_x = 900
x = center_x
color = [0.25, 1, 0.75]

draw_xr18_button(ctx, x, xr18_button, text, color)
draw_potentiometer(ctx, x, control, mute_value, color)
draw_mute_button(ctx, x, mute_value, color)


# End of drawing code

surface.write_to_png('screenshot_mixer.png')
