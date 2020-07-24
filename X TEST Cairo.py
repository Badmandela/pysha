import cairo
import push2_python

from display_utils import draw_title, draw_knob, draw_cue, draw_bar, draw_beat, draw_nudge_1, draw_nudge_2

controls = {'instr': 0, 'instr_lpf': 127, 'master_lpf': 127, 'fx': 127, 'smile': 0, 'reverb': 64, 'tape': 64}
transport = {'cue1': 0, 'cue2': 0, 'bar1': 0, 'bar2': 0, 'beat1': 0, 'beat2': 0, 'nudge1': 0, 'nudge2': 0}

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
piano_max = 20
synth_min = 21
synth_max = 68
sampler_min = 69
sampler_max = 109
ghost_min = 110
rad = 45
line = 10
center_y = 75

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Instrument QUASI-GLOBALS
title = "INSTRUMENT:"
control = controls['instr']
center_x = 60
if controls['instr'] <= piano_max:
    color = [1, 0.25, 0.5]
elif synth_min <= controls['instr'] <= synth_max:
    color = [0.1, 1, 0.7]
elif sampler_min <= controls['instr'] <= sampler_max: # controls['instr'] >= sampler_min
    color = [1, 0.1, 0.9]
else:
    color = [0.75, 0.75, 0.75]

draw_title(ctx, center_x, title, *color)

# Instrument selector canvas
ctx.set_source_rgb(*color)
ctx.rectangle(5, 23 + (60 * (controls['instr'] / 127)), 112, 15)
ctx.fill()

# Instruments list
ctx.set_font_size(10)
ctx.select_font_face("Unscreen", cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_NORMAL)
s = "ELECTRIC PIANO"
ctx.move_to(center_x - (ctx.text_extents(s)[2] / 2), 33)
if controls['instr'] <= piano_max:
    ctx.set_source_rgba(1, 1, 1, 1)
else:
    ctx.set_source_rgba(1, 1, 1, 0.25)
ctx.show_text(s)
s = "SYNTHESIZER"
ctx.move_to(center_x - (ctx.text_extents(s)[2] / 2), 53)
if synth_min <= controls['instr'] <= synth_max:
    ctx.set_source_rgba(1, 1, 1, 1)
else:
    ctx.set_source_rgba(1, 1, 1, 0.25)
ctx.show_text(s)
s = "SAMPLER"
ctx.move_to(center_x - (ctx.text_extents(s)[2] / 2), 73)
if sampler_min <= controls['instr'] <= sampler_max:
    ctx.set_source_rgba(1, 1, 1, 1)
else:
    ctx.set_source_rgba(1, 1, 1, 0.25)
ctx.show_text(s)
s = "GHOST"
ctx.move_to(center_x - (ctx.text_extents(s)[2] / 2), 93)
if controls['instr'] >= ghost_min:
    ctx.set_source_rgba(1, 1, 1, 1)
else: # if controls['instr'] >= ghost_min:
    ctx.set_source_rgba(1, 1, 1, 0.25)
ctx.show_text(s)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Instrument_filter QUASI-GLOBALS
title = "INSTR. LPF:"
control = controls['instr_lpf']
off_value = 127

if controls['instr'] <= piano_max:
    color = [1, 0.25, 0.5]
elif synth_min <= controls['instr'] <= synth_max:
    color = [0.1, 1, 0.7]
elif sampler_min <= controls['instr'] <= sampler_max:  # controls['instr'] >= sampler_min
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
