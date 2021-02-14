import cairo
import push2_python

from display_utils import draw_title, draw_list, draw_knob, draw_cue, draw_bar, draw_beat, draw_nudge_1, draw_nudge_2

controls = {'instr': 0, 'instr_lpf': 128, 'master_lpf': 64, 'fx': 100, 'smile': 200, 'reverb': 64, 'tape': 230}

transport = {'cue1': 0, 'cue2': 0, 'bar1': 0, 'bar2': 0, 'beat1': 0, 'beat2': 0, 'nudge1': 0, 'nudge2': 0}

max_encoder_value = 254
piano_range = range(0, 35)
synth_range = range(35, 95)
sampler_range = range(95, 170)
ghost_range = range(170, 230)
sequencer_range = range(230, 255)

w, h = push2_python.constants.DISPLAY_LINE_PIXELS, push2_python.constants.DISPLAY_N_LINES
surface = cairo.ImageSurface(cairo.FORMAT_RGB16_565, w, h)
ctx = cairo.Context(surface)

# Start of drawing code

# Initial black rectangle
ctx.rectangle(0, 0, w, h)
ctx.set_source_rgb(0, 0, 0)
ctx.fill()

# Globals
rad = 36
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
# ctx.rectangle(12, 34 + (60 * (control / 254)), 98, 15)
ctx.rectangle(12, 34 + (60 * (control / 254)), 98, 15)
ctx.fill()

# Instruments list
# 1
text = "ELECTRIC PIANO"
y = 40
if control in piano_range:
    color = [1, 1, 1, 1]
else:
    color = [1, 1, 1, 0.25]
draw_list(ctx, center_x, y, text, *color)

# 2
text = "SYNTHESIZER"
y = 55
if control in synth_range:
    color = [1, 1, 1, 1]
else:
    color = [1, 1, 1, 0.25]
draw_list(ctx, center_x, y, text, *color)

# 3
text = "SAMPLER"
y = 70
if control in sampler_range:
    color = [1, 1, 1, 1]
else:
    color = [1, 1, 1, 0.25]
draw_list(ctx, center_x, y, text, *color)

# 4
text = "GHOST"
y = 85
if control in ghost_range:
    color = [1, 1, 1, 1]
else:
    color = [1, 1, 1, 0.25]
draw_list(ctx, center_x, y, text, *color)

# 5
text = "SEQUENCER"
y = 100
if control in sequencer_range:
    color = [1, 1, 1, 1]
else:
    color = [1, 1, 1, 0.25]
draw_list(ctx, center_x, y, text, *color)

# Instrument_filter QUASI-GLOBALS
title = "INSTR. LPF:"
instrument = controls['instr']
control = controls['instr_lpf']
off_value = 254

if instrument in piano_range and control != off_value:
    color = [1, 0.25, 0.5]

# Inactive text
elif instrument in piano_range and control == off_value:
    color = [0.25, 0.06, 0.12]

# Active synth text
elif instrument in synth_range and control != off_value:
    color = [0.1, 1, 0.7]

# Inactive synth text
elif instrument in synth_range and control == off_value:
    color = [0.02, 0.25, 0.17]

# Active sampler text
elif instrument in sampler_range and control != off_value:  # controls['instr'] >= sampler_min
    color = [1, 0.1, 0.9]

# Inactive sampler text
elif instrument in sampler_range and control == off_value:
    color = [0.25, 0.02, 0.21]

# Active ghost text
elif instrument in ghost_range and control != off_value:
    color = [0.75, 0.75, 0.75]

# Inactive ghost text
elif instrument in ghost_range and control == off_value:
    color = [0.18, 0.18, 0.18]

# Active sequencer text
elif instrument in sequencer_range and control != off_value:
    color = [0.75, 0.75, 0.75]

# Inactive sequencer text
elif instrument in sequencer_range and control == off_value:
    color = [0.18, 0.18, 0.18]

else:
    color = [1, 0.75, 0.75]
# Active text

center_x = 180
draw_title(ctx, center_x, title, *color)
draw_knob(ctx, center_x, center_y, rad, control, off_value, *color)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Master_filter QUASI-GLOBALS
title = "MASTER LPF:"
control = controls['master_lpf']
center_x = 420
off_value = 254

if control != off_value:
    color = [1, 0.55, 0.1]
else:
    color = [0.25, 0.11, 0.02]

draw_title(ctx, center_x, title, *color)
draw_knob(ctx, center_x, center_y, rad, control, off_value, *color)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# FX QUASI-GLOBALS
title = "FX LVL:"
control = controls['fx']
center_x = 540
off_value = 0

if control != off_value:
    color = [0.75, 0.3, 1]
else:
    color = [0.18, 0.07, 0.25]

draw_title(ctx, center_x, title, *color)
draw_knob(ctx, center_x, center_y, rad, control, off_value, *color)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Smile QUASI-GLOBALS
title = "SMILE:"
control = controls['smile']
center_x = 660
off_value = 0

if control != off_value:
    color = [1, 1, 0.2]
else:
    color = [0.25, 0.25, 0.05]

draw_title(ctx, center_x, title, *color)
draw_knob(ctx, center_x, center_y, rad, control, off_value, *color)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Reverb QUASI-GLOBALS
title = "REVERB:"
control = controls['reverb']
center_x = 780
off_value = 0

if control != off_value:
    color = [0.2, 0.85, 1]
else:
    color = [0.02, 0.21, 0.25]

draw_title(ctx, center_x, title, *color)
draw_knob(ctx, center_x, center_y, rad, control, off_value, *color)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Tape QUASI-GLOBALS
title = "TAPE:"
control = controls['tape']
center_x = 900
off_value = 254

if control != off_value:
    color = [1, 0.3, 0.3]
else:
    color = [0.25, 0.07, 0.07]

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
