import cairo
import push2_python

from display_utils import draw_title, draw_potentiometer, draw_list

controls = {
    'gain': 96, 'selector': 0, 'eq_gain': 64, 'eq_frequency': 64, 'eq_width': 64}



piano_range = range(0, 20)
synth_range = range(20, 70)
sampler_range = range(70, 110)
ghost_range = range(110, 128)

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
text = "GAIN"
control = controls['gain']
center_x = 60
x = center_x
color = [1, 1, 0]

draw_title(ctx, x, text, *color)
draw_potentiometer(ctx, x, control, 127, color)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
title = "SELECTOR:"
control = controls['selector']
center_x = 420

draw_title(ctx, center_x, title, *color)

# List selector canvas
ctx.set_source_rgb(*color)
ctx.rectangle(372, 23 + (60 * (control / 127)), 98, 15)
ctx.fill()

# 1
text = "LOW CUT"
y = 34
if control in piano_range:
    color = [1, 1, 1]
else:
    color = [0.25, 0.25, 0.25]
draw_list(ctx, center_x, y, text, *color)

# 2
text = "PEAK 1"
y = 54
if control in synth_range:
    color = [1, 1, 1]
else:
    color = [0.25, 0.25, 0.25]
draw_list(ctx, center_x, y, text, *color)

# 3
text = "PEAK 2"
y = 74
if control in sampler_range:
    color = [1, 1, 1]
else:
    color = [0.25, 0.25, 0.25]
draw_list(ctx, center_x, y, text, *color)

# 4
text = "PEAK 3"
y = 94
if control in ghost_range:
    color = [1, 1, 1]
else:
    color = [0.25, 0.25, 0.25]
draw_list(ctx, center_x, y, text, *color)

# 5
text = "HIGH SHELF"
y = 114
if control in ghost_range:
    color = [1, 1, 1]
else:
    color = [0.25, 0.25, 0.25]
draw_list(ctx, center_x, y, text, *color)

color = [1, 1, 0]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
text = "Gain"
control = controls['eq_gain']
center_x = 540
x = center_x
draw_title(ctx, x, text, *color)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
text = "Frequency"
control = controls['eq_frequency']
center_x = 660
x = center_x
draw_title(ctx, x, text, *color)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
text = "Width"
control = controls['eq_width']
center_x = 780
x = center_x
draw_title(ctx, x, text, *color)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# End of drawing code

surface.write_to_png('screenshot_channel.png')
