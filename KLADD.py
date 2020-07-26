import cairo
import push2_python

from display_utils import draw_title, draw_list, draw_knob, draw_cue, draw_bar, draw_beat, draw_nudge_1, draw_nudge_2

controls = {
    'instr': 0,
    'instr_lpf': 64,
    'master_lpf': 64,
    'fx': 64,
    'smile': 64,
    'reverb': 64,
    'tape': 64}

transport = {
    'cue1': 0,
    'cue2': 0,
    'bar1': 0,
    'bar2': 0,
    'beat1': 0,
    'beat2': 0,
    'nudge1': 0,
    'nudge2': 0}

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
title = "INSTRUMENT:"
control = controls['instr']
center_x = 60
if control in piano_range:
    color = [1, 0.25, 0.5]
elif control in synth_range:
    color = [0.1, 1, 0.7]
elif control in sampler_range:
    color = [1, 0.1, 0.9]
else:  # controls['instr'] in ghost_range:
    color = [0.75, 0.75, 0.75]

draw_title(ctx, center_x, title, *color)

# List selector canvas
ctx.set_source_rgb(*color)
ctx.rectangle(12, 23 + (60 * (control / 127)), 98, 15)
ctx.fill()

# Instruments list
# 1
text = "ELECTRIC PIANO"
y = 34
if control in piano_range:
    color = [1, 1, 1, 1]
else:
    color = [1, 1, 1, 0.25]
draw_list(ctx, center_x, y, text, *color)

# 2
text = "SYNTHESIZER"
y = 54
if control in synth_range:
    color = [1, 1, 1, 1]
else:
    color = [1, 1, 1, 0.25]
draw_list(ctx, center_x, y, text, *color)

# 3
text = "SAMPLER"
y = 74
if control in sampler_range:
    color = [1, 1, 1, 1]
else:
    color = [1, 1, 1, 0.25]
draw_list(ctx, center_x, y, text, *color)

# 4
text = "GHOST"
y = 94
if control in ghost_range:
    color = [1, 1, 1, 1]
else:
    color = [1, 1, 1, 0.25]
draw_list(ctx, center_x, y, text, *color)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Instrument_filter QUASI-GLOBALS
title = "INSTR. LPF:"
control = controls['instr_lpf']
off_value = 127

if controls['instr'] in piano_range:
    color = [1, 0.25, 0.5]
elif controls['instr'] in synth_range:
    color = [0.1, 1, 0.7]
elif controls['instr'] in sampler_range:  # controls['instr'] >= sampler_min
    color = [1, 0.1, 0.9]
else:
    color = [0.75, 0.75, 0.75]
center_x = 180

draw_title(ctx, center_x, title, *color)
draw_knob(ctx, center_x, center_y, rad, control, off_value, *color)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Master_filter QUASI-GLOBALS
title = "MASTER LPF:"
control = controls['master_lpf']
color = [1, 0.55, 0.1]
center_x = 420
off_value = 127

draw_title(ctx, center_x, title, *color)
draw_knob(ctx, center_x, center_y, rad, control, off_value, *color)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# FX QUASI-GLOBALS
title = "FX LVL:"
control = controls['fx']
color = [0.75, 0.3, 1]
center_x = 540

draw_title(ctx, center_x, title, *color)
draw_knob(ctx, center_x, center_y, rad, control, off_value, *color)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Smile QUASI-GLOBALS
title = "SMILE:"
control = controls['smile']
color = [1, 1, 0.2]
center_x = 660
off_value = 0

draw_title(ctx, center_x, title, *color)
draw_knob(ctx, center_x, center_y, rad, control, off_value, *color)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Reverb QUASI-GLOBALS
title = "REVERB:"
control = controls['reverb']
color = [0.2, 0.85, 1]
center_x = 780
off_value = 0

draw_title(ctx, center_x, title, *color)
draw_knob(ctx, center_x, center_y, rad, control, off_value, *color)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Tape QUASI-GLOBALS
title = "TAPE:"
control = controls['tape']
color = [1, 0.3, 0.3]
center_x = 900
off_value = 127

draw_title(ctx, center_x, title, *color)
draw_knob(ctx, center_x, center_y, rad, control, off_value, *color)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# CUE 1
midi_value = transport['cue1']
x = 60
draw_cue(ctx, x, midi_value)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# CUE 2
midi_value = transport['cue2']
x = 180
draw_cue(ctx, x, midi_value)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# BAR 1
midi_value = transport['bar1']
x = 300
draw_bar(ctx, x, midi_value)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# BAR 2
midi_value = transport['bar2']
x = 420
draw_bar(ctx, x, midi_value)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# BEAT 1
midi_value = transport['beat1']
x = 540
draw_beat(ctx, x, midi_value)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# BEAT 2
midi_value = transport['beat2']
x = 660
draw_beat(ctx, x, midi_value)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# NUDGE 1
midi_value = transport['nudge1']
x = 780
draw_nudge_1(ctx, x, midi_value)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# NUDGE 2
midi_value = transport['nudge2']
x = 900
draw_nudge_2(ctx, x, midi_value)


# End of drawing code

surface.write_to_png('screenshot.png')


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # Bar (Old Shape)
# ctx.move_to(x_min + 59, y_min + 23)
# ctx.line_to(x_min + 58, y_min + 17)
# ctx.curve_to(x_min + 53, y_min + 15, x_min + 50, y_min + 10, x_min + 50.75, y_min + 7)
# ctx.line_to(x_min + 50, y_min + 7)
# ctx.line_to(x_min + 70, y_min + 7)
# ctx.line_to(x_min + 70, y_min + 7)
# ctx.curve_to(x_min + 70, y_min + 10, x_min + 67, y_min + 15, x_min + 62, y_min + 17)
# ctx.line_to(x_min + 62, y_min + 23)
# ctx.line_to(x_min + 63, y_min + 24)
# ctx.line_to(x_min + 67, y_min + 26)
# ctx.line_to(x_min + 53, y_min + 26)
# ctx.line_to(x_min + 57, y_min + 24)
# ctx.close_path()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # Text Outline
# pat = cairo.LinearGradient(center_x - (ctx.text_extents(text)[2] / 2), ctx.text_extents(text)[3] / 2,
#                            center_x - (ctx.text_extents(text)[2] / 2), ctx.text_extents(text)[3] * 2)
# pat.add_color_stop_rgba(0, 1, 1, 1, 0.25)
# pat.add_color_stop_rgba(1, 0, 0, 0, 0.25)
# ctx.set_source(pat)
# ctx.move_to(center_x - (ctx.text_extents(text)[2] / 2), 15)
# ctx.text_path(text)
# ctx.set_line_width(0.5)
# ctx.stroke()