import cairo
import push2_python

controls = {'instr': 32, 'instr_lpf': 64, 'master_lpf': 64, 'fx': 64, 'smile': 64, 'reverb': 64, 'tape': 64}
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
piano_max = 31
synth_min = 32
synth_max = 95
sampler_min = 96
rad = 45
line = 10
center_y = 75

# Textfont
ctx.set_font_size(12)
ctx.select_font_face("Verdana", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Instrument QUASI-GLOBALS
title = "INSTRUMENT:"
control = controls['instr']
if controls['instr'] <= piano_max:
    color = [1, 0.25, 0.5]
elif synth_min <= controls['instr'] <= synth_max:
    color = [0.1, 1, 0.7]
else:  # controls['instr'] >= sampler_min
    color = [1, 0.1, 0.9]
center_x = 60

title = "INSTRUMENT:"
ctx.move_to(center_x - (ctx.text_extents(title)[2] / 2), 15)
ctx.set_source_rgb(*color)
ctx.show_text(title)

# Instrument selector canvas
ctx.set_source_rgb(*color)
ctx.rectangle(5, 23 + (30 * (controls['instr'] / 127)), 112, 15)
ctx.fill()

# Instruments list
ctx.select_font_face("Verdana", cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_NORMAL)
s = "ELECTRIC PIANO"
ctx.move_to(center_x - (ctx.text_extents(s)[2] / 2), 35)
if controls['instr'] <= piano_max:
    ctx.set_source_rgba(1, 1, 1, 1)
else:
    ctx.set_source_rgba(1, 1, 1, 0.25)
ctx.show_text(s)
s = "SYNTHESIZER"
ctx.move_to(center_x - (ctx.text_extents(s)[2] / 2), 50)
if synth_min <= controls['instr'] <= synth_max:
    ctx.set_source_rgba(1, 1, 1, 1)
else:
    ctx.set_source_rgba(1, 1, 1, 0.25)
ctx.show_text(s)
s = "SAMPLER"
ctx.move_to(center_x - (ctx.text_extents(s)[2] / 2), 65)
if controls['instr'] >= sampler_min:
    ctx.set_source_rgba(1, 1, 1, 1)
else:
    ctx.set_source_rgba(1, 1, 1, 0.25)
ctx.show_text(s)
ctx.select_font_face("Verdana", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Instrument_filter QUASI-GLOBALS
title = "INSTRUMENT LPF:"
control = controls['instr_lpf']

if controls['instr'] <= piano_max:
    color = [1, 0.25, 0.5]
elif synth_min <= controls['instr'] <= synth_max:
    color = [0.1, 1, 0.7]
elif controls['instr'] >= sampler_min:
    color = [1, 0.1, 0.9]
center_x = 180

# Instrument_filter title
ctx.set_source_rgb(*color)
ctx.move_to(center_x - (ctx.text_extents(title)[2] / 2), 15)
ctx.show_text(title)

# Instrument_filter value (canvas - inverted)
ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
ctx.set_source_rgba(*color, 0.5)
ctx.fill()
ctx.stroke()

# Instrument_filter canvas (value - inverted)
ctx.move_to(center_x, center_y)
ctx.arc(center_x, center_y, rad, 3.14 / 2, 3.14 / 2 + 360 * (control / 127) * (3.14 / 180))
ctx.close_path()
ctx.set_source_rgb(*screen_black)
ctx.fill()
ctx.stroke()

# Instrument_filter frame
if control == 127:
    ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
    ctx.set_source_rgb(*screen_dark)
    ctx.set_line_width(10)
    ctx.stroke()
else:
    ctx.set_source_rgb(*color)
    ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
    ctx.set_line_width(line - 1)
    ctx.stroke()

    pat = cairo.MeshPattern()
    pat.begin_patch()
    pat.move_to(center_x, center_y - (rad / 4 + (line / 2)))
    pat.line_to(center_x - (rad + (line / 2)), center_y - (rad / 4 + (line / 2)))
    pat.line_to(center_x - (rad + (line / 2)), center_y + (rad + (line / 2)))
    pat.line_to(center_x, center_y + (rad + (line / 2)))
    pat.set_corner_color_rgba(0, *color, 1)
    pat.set_corner_color_rgba(1, *color, 1)
    pat.set_corner_color_rgba(2, *color, 1)
    pat.set_corner_color_rgba(3, 1, 1, 1, 0.5)
    pat.end_patch()
    pat.begin_patch()
    pat.move_to(center_x, center_y + (rad + (line / 2)))
    pat.line_to(center_x + (rad + (line / 2)), center_y + (rad + (line / 2)))
    pat.line_to(center_x + (rad + (line / 2)), center_y - (rad / 4 + (line / 2)))
    pat.line_to(center_x, center_y - (rad / 4 + (line / 2)))
    pat.set_corner_color_rgba(0, 0, 0, 0, 0.5)
    pat.set_corner_color_rgba(1, *color, 1)
    pat.set_corner_color_rgba(2, *color, 1)
    pat.set_corner_color_rgba(3, *color, 1)
    pat.end_patch()
    ctx.set_source(pat)

    ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
    ctx.set_line_width(line)
    ctx.stroke()

# Instrument_filter indicator
pos1 = 3.14 / 2 + 360 * ((controls['instr_lpf'] - 5) / 127) * (3.14 / 180)
pos2 = 3.14 / 2 + 360 * ((controls['instr_lpf'] + 5) / 127) * (3.14 / 180)

# Instrument_filter indicator inner
if controls['instr_lpf'] == 127:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(*color)
ctx.arc(center_x, center_y, rad, pos1, pos2)
ctx.line_to(center_x, center_y)
ctx.fill()

# Instrument_filter indicator outer
if controls['instr_lpf'] == 127:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgba(1, 1, 1, 0.64)
ctx.arc(center_x, center_y, rad, pos1, pos2)
ctx.set_line_width(12)
ctx.stroke()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Master filter QUASI-GLOBALS
title = "MASTER LPF:"
control = controls['master_lpf']
color = [1, 0.5, 0.1]
center_x = 420

pos1 = 3.14 / 2 + 360 * ((control - 5) / 127) * (3.14 / 180)
pos2 = 3.14 / 2 + 360 * ((control + 5) / 127) * (3.14 / 180)

# Master_filter title
ctx.move_to(center_x - (ctx.text_extents(title)[2] / 2), 15)
ctx.set_source_rgb(*color)
ctx.show_text(title)
ctx.stroke()

# Master_filter value (canvas - inverted)
ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
ctx.set_source_rgba(*color, 0.5)
ctx.fill()
ctx.stroke()

# Master_filter canvas (value - inverted)
ctx.move_to(center_x, center_y)
ctx.arc(center_x, center_y, rad, 3.14 / 2, 3.14 / 2 + 360 * (control / 127) * (3.14 / 180))
ctx.close_path()
ctx.set_source_rgb(*screen_black)
ctx.fill()
ctx.stroke()

# Master_filter frame
if control == 127:
    ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
    ctx.set_source_rgb(*screen_dark)
    ctx.set_line_width(10)
    ctx.stroke()
else:
    ctx.set_source_rgb(*color)
    ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
    ctx.set_line_width(line - 1)
    ctx.stroke()

    pat = cairo.MeshPattern()
    pat.begin_patch()
    pat.move_to(center_x, center_y - (rad / 4 + (line / 2)))
    pat.line_to(center_x - (rad + (line / 2)), center_y - (rad / 4 + (line / 2)))
    pat.line_to(center_x - (rad + (line / 2)), center_y + (rad + (line / 2)))
    pat.line_to(center_x, center_y + (rad + (line / 2)))
    pat.set_corner_color_rgba(0, *color, 1)
    pat.set_corner_color_rgba(1, *color, 1)
    pat.set_corner_color_rgba(2, *color, 1)
    pat.set_corner_color_rgba(3, 1, 1, 1, 0.5)
    pat.end_patch()
    pat.begin_patch()
    pat.move_to(center_x, center_y + (rad + (line / 2)))
    pat.line_to(center_x + (rad + (line / 2)), center_y + (rad + (line / 2)))
    pat.line_to(center_x + (rad + (line / 2)), center_y - (rad / 4 + (line / 2)))
    pat.line_to(center_x, center_y - (rad / 4 + (line / 2)))
    pat.set_corner_color_rgba(0, 0, 0, 0, 0.5)
    pat.set_corner_color_rgba(1, *color, 1)
    pat.set_corner_color_rgba(2, *color, 1)
    pat.set_corner_color_rgba(3, *color, 1)
    pat.end_patch()
    ctx.set_source(pat)

    ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
    ctx.set_line_width(line)
    ctx.stroke()

# Master filter indicator
if control == 127:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(1, 0.5, 0.1)
ctx.arc(center_x, center_y, rad, pos1, pos2)
ctx.line_to(center_x, center_y)
ctx.fill()

if control == 127:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgba(1, 1, 1, 0.64)
ctx.arc(center_x, center_y, rad, pos1, pos2)
ctx.set_line_width(12)
ctx.stroke()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# FX QUASI-GLOBALS
title = "FX LVL:"
control = controls['fx']
color = [0.75, 0.1, 1]
center_x = 540

pos1 = 3.14 / 2 + 360 * ((control - 5) / 127) * (3.14 / 180)
pos2 = 3.14 / 2 + 360 * ((control + 5) / 127) * (3.14 / 180)

# FX title
ctx.set_source_rgb(*color)
ctx.move_to(center_x - (ctx.text_extents(title)[2] / 2), 15)
ctx.show_text(title)
ctx.stroke()

# FX value (canvas inverted)
ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
ctx.set_source_rgba(*color, 0.5)
ctx.fill()
ctx.stroke()

# FX canvas (value inverted)
ctx.move_to(center_x, center_y)
ctx.arc(center_x, center_y, rad, 3.14 / 2, 3.14 / 2 + 360 * (controls['fx'] / 127) * (3.14 / 180))
ctx.close_path()
ctx.set_source_rgb(*screen_black)
ctx.fill()
ctx.stroke()

# FX frame
if control == 127:
    ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
    ctx.set_source_rgb(*screen_dark)
    ctx.set_line_width(10)
    ctx.stroke()
else:
    ctx.set_source_rgb(*color)
    ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
    ctx.set_line_width(line - 1)
    ctx.stroke()

    pat = cairo.MeshPattern()
    pat.begin_patch()
    pat.move_to(center_x, center_y - (rad / 4 + (line / 2)))
    pat.line_to(center_x - (rad + (line / 2)), center_y - (rad / 4 + (line / 2)))
    pat.line_to(center_x - (rad + (line / 2)), center_y + (rad + (line / 2)))
    pat.line_to(center_x, center_y + (rad + (line / 2)))
    pat.set_corner_color_rgba(0, *color, 1)
    pat.set_corner_color_rgba(1, *color, 1)
    pat.set_corner_color_rgba(2, *color, 1)
    pat.set_corner_color_rgba(3, 1, 1, 1, 0.5)
    pat.end_patch()
    pat.begin_patch()
    pat.move_to(center_x, center_y + (rad + (line / 2)))
    pat.line_to(center_x + (rad + (line / 2)), center_y + (rad + (line / 2)))
    pat.line_to(center_x + (rad + (line / 2)), center_y - (rad / 4 + (line / 2)))
    pat.line_to(center_x, center_y - (rad / 4 + (line / 2)))
    pat.set_corner_color_rgba(0, 0, 0, 0, 0.5)
    pat.set_corner_color_rgba(1, *color, 1)
    pat.set_corner_color_rgba(2, *color, 1)
    pat.set_corner_color_rgba(3, *color, 1)
    pat.end_patch()
    ctx.set_source(pat)

    ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
    ctx.set_line_width(line)
    ctx.stroke()

# FX indicator
if control == 127:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(*color)
ctx.arc(center_x, center_y, rad, pos1, pos2)
ctx.line_to(center_x, center_y)
ctx.fill()

if controls['fx'] == 127:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgba(1, 1, 1, 0.64)
ctx.arc(center_x, center_y, rad, pos1, pos2)
ctx.set_line_width(12)
ctx.stroke()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Smile QUASI-GLOBALS
title = "SMILE:"
control = controls['smile']
color = [1, 1, 0.1]
center_x = 660

pos1 = 3.14 / 2 + 360 * ((control - 5) / 127) * (3.14 / 180)
pos2 = 3.14 / 2 + 360 * ((control + 5) / 127) * (3.14 / 180)

# Smile title
ctx.set_source_rgb(*color)
ctx.move_to(center_x - (ctx.text_extents(title)[2] / 2), 15)
ctx.show_text(title)
ctx.stroke()

# Smile canvas
ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
ctx.set_source_rgb(*screen_black)
ctx.fill()
ctx.stroke()

# Smile value
ctx.move_to(center_x, center_y)
ctx.arc(center_x, center_y, rad, 3.14 / 2, 3.14 / 2 + 360 * (control / 127) * (3.14 / 180))
ctx.close_path()
ctx.set_source_rgba(*color, 0.5)
ctx.fill()
ctx.stroke()

# Smile frame
if control == 0:
    ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
    ctx.set_source_rgb(*screen_dark)
    ctx.set_line_width(10)
    ctx.stroke()
else:
    ctx.set_source_rgb(*color)
    ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
    ctx.set_line_width(line - 1)
    ctx.stroke()

    pat = cairo.MeshPattern()
    pat.begin_patch()
    pat.move_to(center_x, center_y - (rad / 4 + (line / 2)))
    pat.line_to(center_x - (rad + (line / 2)), center_y - (rad / 4 + (line / 2)))
    pat.line_to(center_x - (rad + (line / 2)), center_y + (rad + (line / 2)))
    pat.line_to(center_x, center_y + (rad + (line / 2)))
    pat.set_corner_color_rgba(0, *color, 1)
    pat.set_corner_color_rgba(1, *color, 1)
    pat.set_corner_color_rgba(2, *color, 1)
    pat.set_corner_color_rgba(3, 0, 0, 0, 0.5)
    pat.end_patch()
    pat.begin_patch()
    pat.move_to(center_x, center_y + (rad + (line / 2)))
    pat.line_to(center_x + (rad + (line / 2)), center_y + (rad + (line / 2)))
    pat.line_to(center_x + (rad + (line / 2)), center_y - (rad / 4 + (line / 2)))
    pat.line_to(center_x, center_y - (rad / 4 + (line / 2)))
    pat.set_corner_color_rgba(0, 1, 1, 1, 0.5)
    pat.set_corner_color_rgba(1, *color, 1)
    pat.set_corner_color_rgba(2, *color, 1)
    pat.set_corner_color_rgba(3, *color, 1)
    pat.end_patch()
    ctx.set_source(pat)

    ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
    ctx.set_line_width(line)
    ctx.stroke()

# Smile indicator
if control == 0:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(*color)
ctx.arc(center_x, center_y, rad, pos1, pos2)
ctx.line_to(center_x, center_y)
ctx.fill()
if control == 0:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgba(1, 1, 1, 0.64)
ctx.arc(center_x, center_y, rad, pos1, pos2)
ctx.set_line_width(12)
ctx.stroke()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Reverb QUASI-GLOBALS
title = "REVERB:"
control = controls['reverb']
color = [0.1, 0.85, 1]
center_x = 780

# Reverb
pos1 = 3.14 / 2 + 360 * ((controls['reverb'] - 5) / 127) * (3.14 / 180)
pos2 = 3.14 / 2 + 360 * ((controls['reverb'] + 5) / 127) * (3.14 / 180)

# Reverb title
ctx.set_source_rgb(*color)
ctx.move_to(center_x - (ctx.text_extents(title)[2] / 2), 15)
ctx.show_text(title)
ctx.stroke()

# Reverb canvas
ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
ctx.set_source_rgb(*screen_black)
ctx.fill()
ctx.stroke()

# Reverb value
ctx.move_to(center_x, center_y)
ctx.arc(center_x, center_y, rad, 3.14 / 2, 3.14 / 2 + 360 * (control / 127) * (3.14 / 180))
ctx.close_path()
ctx.set_source_rgba(*color, 0.5)
ctx.fill()
ctx.stroke()

# Reverb frame
if control == 0:
    ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
    ctx.set_source_rgb(*screen_dark)
    ctx.set_line_width(10)
    ctx.stroke()
else:
    ctx.set_source_rgb(*color)
    ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
    ctx.set_line_width(line - 1)
    ctx.stroke()

    pat = cairo.MeshPattern()
    pat.begin_patch()
    pat.move_to(center_x, center_y - (rad / 4 + (line / 2)))
    pat.line_to(center_x - (rad + (line / 2)), center_y - (rad / 4 + (line / 2)))
    pat.line_to(center_x - (rad + (line / 2)), center_y + (rad + (line / 2)))
    pat.line_to(center_x, center_y + (rad + (line / 2)))
    pat.set_corner_color_rgba(0, *color, 1)
    pat.set_corner_color_rgba(1, *color, 1)
    pat.set_corner_color_rgba(2, *color, 1)
    pat.set_corner_color_rgba(3, 0, 0, 0, 0.5)
    pat.end_patch()
    pat.begin_patch()
    pat.move_to(center_x, center_y + (rad + (line / 2)))
    pat.line_to(center_x + (rad + (line / 2)), center_y + (rad + (line / 2)))
    pat.line_to(center_x + (rad + (line / 2)), center_y - (rad / 4 + (line / 2)))
    pat.line_to(center_x, center_y - (rad / 4 + (line / 2)))
    pat.set_corner_color_rgba(0, 1, 1, 1, 0.5)
    pat.set_corner_color_rgba(1, *color, 1)
    pat.set_corner_color_rgba(2, *color, 1)
    pat.set_corner_color_rgba(3, *color, 1)
    pat.end_patch()
    ctx.set_source(pat)

    ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
    ctx.set_line_width(line)
    ctx.stroke()

# Reverb indicator
if controls['reverb'] == 0:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(*color)
ctx.arc(center_x, center_y, rad, pos1, pos2)
ctx.line_to(center_x, center_y)
ctx.fill()
if controls['reverb'] == 0:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgba(1, 1, 1, 0.64)
ctx.arc(center_x, center_y, rad, pos1, pos2)
ctx.set_line_width(12)
ctx.stroke()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Tape QUASI-GLOBALS
title = "TAPE:"
control = controls['tape']
color = [1, 0.25, 0.25]
center_x = 900

pos1 = 3.14 / 2 + 360 * ((controls['tape'] - 5) / 127) * (3.14 / 180)
pos2 = 3.14 / 2 + 360 * ((controls['tape'] + 5) / 127) * (3.14 / 180)

# Tape title
ctx.set_source_rgb(*color)
ctx.move_to(center_x - (ctx.text_extents(title)[2] / 2), 15)
ctx.show_text(title)
ctx.stroke()

# Tape value (canvas inverted)
ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
ctx.set_source_rgba(*color, 0.5)
ctx.fill()
ctx.stroke()

# Tape canvas (value inverted)
ctx.move_to(center_x, center_y)
ctx.arc(center_x, center_y, rad, 3.14 / 2, 3.14 / 2 + 360 * (control / 127) * (3.14 / 180))
ctx.close_path()
ctx.set_source_rgb(*screen_black)
ctx.fill()
ctx.stroke()

# Tape frame
if controls['fx'] == 127:
    ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
    ctx.set_source_rgb(*screen_dark)
    ctx.set_line_width(10)
    ctx.stroke()
else:
    ctx.set_source_rgb(*color)
    ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
    ctx.set_line_width(line - 1)
    ctx.stroke()

    pat = cairo.MeshPattern()
    pat.begin_patch()
    pat.move_to(center_x, center_y - (rad / 4 + (line / 2)))
    pat.line_to(center_x - (rad + (line / 2)), center_y - (rad / 4 + (line / 2)))
    pat.line_to(center_x - (rad + (line / 2)), center_y + (rad + (line / 2)))
    pat.line_to(center_x, center_y + (rad + (line / 2)))
    pat.set_corner_color_rgba(0, *color, 1)
    pat.set_corner_color_rgba(1, *color, 1)
    pat.set_corner_color_rgba(2, *color, 1)
    pat.set_corner_color_rgba(3, 1, 1, 1, 0.5)
    pat.end_patch()
    pat.begin_patch()
    pat.move_to(center_x, center_y + (rad + (line / 2)))
    pat.line_to(center_x + (rad + (line / 2)), center_y + (rad + (line / 2)))
    pat.line_to(center_x + (rad + (line / 2)), center_y - (rad / 4 + (line / 2)))
    pat.line_to(center_x, center_y - (rad / 4 + (line / 2)))
    pat.set_corner_color_rgba(0, 0, 0, 0, 0.5)
    pat.set_corner_color_rgba(1, *color, 1)
    pat.set_corner_color_rgba(2, *color, 1)
    pat.set_corner_color_rgba(3, *color, 1)
    pat.end_patch()
    ctx.set_source(pat)

    ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
    ctx.set_line_width(line)
    ctx.stroke()

# Tape indicator
if controls['tape'] == 127:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(*color)
ctx.arc(center_x, center_y, rad, pos1, pos2)
ctx.line_to(center_x, center_y)
ctx.fill()
if controls['tape'] == 127:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgba(1, 1, 1, 0.64)
ctx.arc(center_x, center_y, rad, pos1, pos2)
ctx.set_line_width(12)
ctx.stroke()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# CUE 1
color = [1, 1, 1]
color_dark = [divide / 1.5 for divide in color]
x_min = 0
x_max = 120
y_min = 130
y_max = 160
if transport['cue1'] == 0:
    ctx.move_to(50, 135)
    ctx.curve_to(60, 130, 60, 140, 70, 135)
    ctx.line_to(70, 147)
    ctx.curve_to(60, 152, 60, 142, 50, 147)
    ctx.close_path()
    ctx.move_to(50, 135)
    ctx.line_to(50, 156)
    ctx.set_source_rgb(*color)
    ctx.set_line_width(2.5)
    ctx.stroke()
elif transport['cue1'] == 127:
    ctx.move_to(x_min, y_min)
    ctx.line_to(x_max, y_min)
    ctx.line_to(x_max, y_max)
    ctx.line_to(x_min, y_max)
    ctx.close_path()
    pat = cairo.RadialGradient(x_min + 60, y_min + 15, 100, x_min + 60, y_min + 15, 0)
    pat.add_color_stop_rgb(0, *color_dark)
    pat.add_color_stop_rgb(1, *color)
    ctx.set_source(pat)
    ctx.fill()

    ctx.move_to(50, 135)
    ctx.curve_to(60, 130, 60, 140, 70, 135)
    ctx.line_to(70, 147)
    ctx.curve_to(60, 152, 60, 142, 50, 147)
    ctx.close_path()
    ctx.move_to(50, 135)
    ctx.line_to(50, 156)
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(2.5)
    ctx.stroke()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# CUE 2
color = [1, 1, 1]
color_dark = [divide / 1.5 for divide in color]
x_min = 120
x_max = 240

if transport['cue2'] == 0:
    ctx.move_to(170, 135)
    ctx.curve_to(180, 130, 180, 140, 190, 135)
    ctx.line_to(190, 147)
    ctx.curve_to(180, 152, 180, 142, 170, 147)
    ctx.close_path()
    ctx.move_to(170, 135)
    ctx.line_to(170, 156)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(2.5)
    ctx.stroke()

elif transport['cue2'] == 127:
    ctx.move_to(x_min, y_min)
    ctx.line_to(x_max, y_min)
    ctx.line_to(x_max, y_max)
    ctx.line_to(x_min, y_max)
    ctx.close_path()
    pat = cairo.RadialGradient(x_min + 60, y_min + 15, 100, x_min + 60, y_min + 15, 0)
    pat.add_color_stop_rgb(0, *color_dark)
    pat.add_color_stop_rgb(1, *color)
    ctx.set_source(pat)
    ctx.fill()

    ctx.move_to(170, 135)
    ctx.curve_to(180, 130, 180, 140, 190, 135)
    ctx.line_to(190, 147)
    ctx.curve_to(180, 152, 180, 142, 170, 147)
    ctx.close_path()
    ctx.move_to(170, 135)
    ctx.line_to(170, 156)
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(2.5)
    ctx.stroke()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# BAR 1
color = [1, 1, 0]
color_dark = [divide / 1.5 for divide in color]
x_min = 240
x_max = 360

if transport['bar1'] == 0:
    ctx.move_to(300, 145)
    ctx.line_to(300, 155)
    ctx.move_to(290, 135)
    ctx.line_to(310, 135)
    ctx.line_to(300, 145)
    ctx.close_path()
    ctx.move_to(295, 155)
    ctx.line_to(305, 155)
    ctx.set_line_width(2.5)
    ctx.set_source_rgb(*color)
    ctx.stroke()

elif transport['bar1'] == 127:
    ctx.move_to(x_min, y_min)
    ctx.line_to(x_max, y_min)
    ctx.line_to(x_max, y_max)
    ctx.line_to(x_min, y_max)
    ctx.close_path()
    pat = cairo.RadialGradient(x_min + 60, y_min + 15, 100, x_min + 60, y_min + 15, 0)
    pat.add_color_stop_rgb(0, *color_dark)
    pat.add_color_stop_rgb(1, *color)
    ctx.set_source(pat)
    ctx.fill()

    ctx.move_to(300, 145)
    ctx.line_to(300, 155)
    ctx.move_to(290, 135)
    ctx.line_to(310, 135)
    ctx.line_to(300, 145)
    ctx.close_path()
    ctx.move_to(295, 155)
    ctx.line_to(305, 155)
    ctx.set_line_width(2.5)
    ctx.set_source_rgb(0, 0, 0)
    ctx.stroke()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# BAR 2
color = [1, 1, 0]
color_dark = [divide / 1.5 for divide in color]
x_min = 360
x_max = 480

if transport['bar2'] == 0:
    ctx.move_to(420, 145)
    ctx.line_to(420, 155)
    ctx.move_to(410, 135)
    ctx.line_to(430, 135)
    ctx.line_to(420, 145)
    ctx.close_path()
    ctx.move_to(415, 155)
    ctx.line_to(425, 155)
    ctx.set_source_rgb(*color)
    ctx.set_line_width(2.5)
    ctx.stroke()

elif transport['bar2'] == 127:
    ctx.move_to(x_min, y_min)
    ctx.line_to(x_max, y_min)
    ctx.line_to(x_max, y_max)
    ctx.line_to(x_min, y_max)
    ctx.close_path()
    pat = cairo.RadialGradient(x_min + 60, y_min + 15, 100, x_min + 60, y_min + 15, 0)
    pat.add_color_stop_rgb(0, *color_dark)
    pat.add_color_stop_rgb(1, *color)
    ctx.set_source(pat)
    ctx.fill()

    ctx.move_to(420, 145)
    ctx.line_to(420, 155)
    ctx.move_to(410, 135)
    ctx.line_to(430, 135)
    ctx.line_to(420, 145)
    ctx.close_path()
    ctx.move_to(415, 155)
    ctx.line_to(425, 155)
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(2.5)
    ctx.stroke()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# BEAT 1
color = [1, 0.4, 0]
color_dark = [divide / 1.5 for divide in color]
x_min = 480
x_max = 600

if transport['beat1'] == 0:
    ctx.move_to(540, 140)
    ctx.curve_to(540, 130, 555, 130, 550, 142)
    ctx.curve_to(550, 143, 542, 152, 540, 155)
    ctx.curve_to(538, 152, 530, 143, 530, 142)
    ctx.curve_to(525, 130, 540, 130, 540, 140)
    ctx.close_path()
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.set_source_rgb(*color)
    ctx.set_line_width(2.5)
    ctx.stroke()

elif transport['beat1'] == 127:
    ctx.move_to(x_min, y_min)
    ctx.line_to(x_max, y_min)
    ctx.line_to(x_max, y_max)
    ctx.line_to(x_min, y_max)
    ctx.close_path()
    pat = cairo.RadialGradient(x_min + 60, y_min + 15, 100, x_min + 60, y_min + 15, 0)
    pat.add_color_stop_rgb(0, *color_dark)
    pat.add_color_stop_rgb(1, *color)
    ctx.set_source(pat)
    ctx.fill()

    ctx.move_to(540, 140)
    ctx.curve_to(540, 130, 555, 130, 550, 142)
    ctx.curve_to(550, 143, 542, 152, 540, 155)
    ctx.curve_to(538, 152, 530, 143, 530, 142)
    ctx.curve_to(525, 130, 540, 130, 540, 140)
    ctx.close_path()
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(2.5)
    ctx.stroke()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# BEAT 2
color = [1, 0.4, 0]
color_dark = [divide / 1.5 for divide in color]
x_min = 600
x_max = 720

if transport['beat2'] == 0:
    ctx.move_to(660, 140)
    ctx.curve_to(660, 130, 675, 130, 670, 142)
    ctx.curve_to(670, 143, 662, 152, 660, 155)
    ctx.curve_to(658, 152, 650, 143, 650, 142)
    ctx.curve_to(645, 130, 660, 130, 660, 140)
    ctx.close_path()
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.set_source_rgb(*color)
    ctx.set_line_width(2.5)
    ctx.stroke()

elif transport['beat2'] == 127:
    ctx.move_to(x_min, y_min)
    ctx.line_to(x_max, y_min)
    ctx.line_to(x_max, y_max)
    ctx.line_to(x_min, y_max)
    ctx.close_path()
    pat = cairo.RadialGradient(x_min + 60, y_min + 15, 100, x_min + 60, y_min + 15, 0)
    pat.add_color_stop_rgb(0, *color_dark)
    pat.add_color_stop_rgb(1, *color)
    ctx.set_source(pat)
    ctx.fill()

    ctx.move_to(660, 140)
    ctx.curve_to(660, 130, 675, 130, 670, 142)
    ctx.curve_to(670, 143, 662, 152, 660, 155)
    ctx.curve_to(658, 152, 650, 143, 650, 142)
    ctx.curve_to(645, 130, 660, 130, 660, 140)
    ctx.close_path()
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(2.5)
    ctx.stroke()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# NUDGE 1
color = [1, 0.4, 0.6]
color_dark = [divide / 1.5 for divide in color]
x_min = 720
x_max = 840

if transport['nudge1'] == 0:
    ctx.set_source_rgb(*color)
    ctx.move_to(764, 136)
    ctx.line_to(764, 154)
    ctx.set_line_width(5)
    ctx.set_line_cap(cairo.LINE_CAP_SQUARE)
    ctx.stroke()
    ctx.move_to(775, 135)
    ctx.line_to(775, 155)
    ctx.set_line_width(2.5)
    ctx.stroke()
    ctx.move_to(785, 135)
    ctx.line_to(785, 155)
    ctx.set_line_width(2.5)
    ctx.stroke()
    ctx.move_to(795, 134.5)
    ctx.line_to(795, 155.5)
    ctx.set_line_width(1.5)
    ctx.set_line_cap(cairo.LINE_CAP_SQUARE)
    ctx.stroke()

elif transport['nudge1'] == 127:
    ctx.move_to(x_min, y_min)
    ctx.line_to(x_max, y_min)
    ctx.line_to(x_max, y_max)
    ctx.line_to(x_min, y_max)
    ctx.close_path()
    pat = cairo.RadialGradient(x_min + 60, y_min + 15, 100, x_min + 60, y_min + 15, 0)
    pat.add_color_stop_rgb(0, *color_dark)
    pat.add_color_stop_rgb(1, *color)
    ctx.set_source(pat)
    ctx.fill()

    ctx.set_source_rgb(0, 0, 0)
    ctx.move_to(764, 136)
    ctx.line_to(764, 154)
    ctx.set_line_width(5)
    ctx.set_line_cap(cairo.LINE_CAP_SQUARE)
    ctx.stroke()
    ctx.move_to(775, 135)
    ctx.line_to(775, 155)
    ctx.set_line_width(2.5)
    ctx.stroke()
    ctx.move_to(785, 135)
    ctx.line_to(785, 155)
    ctx.set_line_width(2.5)
    ctx.stroke()
    ctx.move_to(795, 134.5)
    ctx.line_to(795, 155.5)
    ctx.set_line_width(1.5)
    ctx.set_line_cap(cairo.LINE_CAP_SQUARE)
    ctx.stroke()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# NUDGE 2
color = [1, 0.4, 0.6]
color_dark = [divide / 1.5 for divide in color]
x_min = 840
x_max = 960

if transport['nudge2'] == 0:
    ctx.set_source_rgb(*color)

    ctx.move_to(885, 134.5)
    ctx.line_to(885, 155.5)
    ctx.set_line_width(1.5)
    ctx.set_line_cap(cairo.LINE_CAP_SQUARE)
    ctx.stroke()

    ctx.move_to(895, 135)
    ctx.line_to(895, 155)
    ctx.set_line_width(2.5)
    ctx.set_line_cap(cairo.LINE_CAP_SQUARE)
    ctx.stroke()

    ctx.move_to(905, 135)
    ctx.line_to(905, 155)
    ctx.set_line_width(2.5)
    ctx.stroke()

    ctx.move_to(916, 136)
    ctx.line_to(916, 154)
    ctx.set_line_width(5)
    ctx.stroke()

elif transport['nudge2'] == 127:
    ctx.move_to(x_min, y_min)
    ctx.line_to(x_max, y_min)
    ctx.line_to(x_max, y_max)
    ctx.line_to(x_min, y_max)
    ctx.close_path()
    pat = cairo.RadialGradient(x_min + 60, y_min + 15, 100, x_min + 60, y_min + 15, 0)
    pat.add_color_stop_rgb(0, *color_dark)
    pat.add_color_stop_rgb(1, *color)
    ctx.set_source(pat)
    ctx.fill()

    ctx.set_source_rgb(0, 0, 0)

    ctx.move_to(885, 134.5)
    ctx.line_to(885, 155.5)
    ctx.set_line_width(1.5)
    ctx.set_line_cap(cairo.LINE_CAP_SQUARE)
    ctx.stroke()

    ctx.move_to(895, 135)
    ctx.line_to(895, 155)
    ctx.set_line_width(2.5)
    ctx.set_line_cap(cairo.LINE_CAP_SQUARE)
    ctx.stroke()
    ctx.move_to(905, 135)
    ctx.line_to(905, 155)
    ctx.set_line_width(2.5)
    ctx.stroke()
    ctx.move_to(916, 136)
    ctx.line_to(916, 154)
    ctx.set_line_width(5)
    ctx.stroke()

# End of drawing code


surface.write_to_png('screenshot.png')
