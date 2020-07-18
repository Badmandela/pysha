import cairo
import push2_python

controls = {'instr': 0, 'instr_lpf': 64, 'instr_vol': 64, 'master_lpf': 64, 'fx': 64, 'smile': 64, 'reverb': 64,
            'tape': 64}

piano_max = 31
synth_min = 32
synth_max = 95
sampler_min = 96

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

ctx.set_font_size(12)
ctx.select_font_face("Verdana", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)

# Instrument QUASI-GLOBALS
title = "INSTRUMENT:"
control = controls['instr']
color_piano = [1, 0.25, 0.5]
color_piano_dark = [0.5, 0.125, 0.25]
color_piano_light = [1, 0.75, 0.75]
color_synth = [0, 1, 0.7]
color_synth_dark = [0, 0.5, 0.45]
color_synth_light = [0.75, 1, 1]
color_sampler = [1, 0, 0.9]
color_sampler_dark = [0.5, 0, 0.45]
color_sampler_light = [1, 0.75, 1]
center_x = 60

s = "INSTRUMENT:"
ctx.move_to(center_x - (ctx.text_extents(s)[2] / 2), 15)
if controls['instr'] <= piano_max:
    ctx.set_source_rgb(*color_piano)
if synth_min <= controls['instr'] <= synth_max:
    ctx.set_source_rgb(*color_synth)
if controls['instr'] >= sampler_min:
    ctx.set_source_rgb(*color_sampler)
ctx.show_text(s)

# Instrument canvas
ctx.rectangle(15, 23 + (30 * (controls['instr'] / 127)), 90, 15)
if controls['instr'] <= piano_max:
    ctx.set_source_rgb(*color_piano)
if synth_min <= controls['instr'] <= synth_max:
    ctx.set_source_rgb(*color_synth)
if controls['instr'] >= sampler_min:
    ctx.set_source_rgb(*color_sampler)
ctx.fill()
ctx.stroke()

# Instruments list
ctx.set_source_rgb(1, 1, 1)
ctx.select_font_face("Verdana", cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_NORMAL)
s = "PIANO"
ctx.move_to(center_x - (ctx.text_extents(s)[2] / 2), 35)
ctx.show_text(s)
s = "SYNTH"
ctx.move_to(center_x - (ctx.text_extents(s)[2] / 2), 50)
ctx.show_text(s)
s = "SAMPLER"
ctx.move_to(center_x - (ctx.text_extents(s)[2] / 2), 65)
ctx.show_text(s)
ctx.select_font_face("Verdana", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)

# Instrument_filter title
if controls['instr'] <= piano_max:
    ctx.set_source_rgb(*color_piano)
if synth_min <= controls['instr'] <= synth_max:
    ctx.set_source_rgb(*color_synth)
if controls['instr'] >= sampler_min:
    ctx.set_source_rgb(*color_sampler)
s = "INSTRUMENT LPF:"
ctx.move_to(180 - (ctx.text_extents(s)[2] / 2), 15)
ctx.show_text(s)

# Instrument_filter value (canvas - inverted)
ctx.arc(180, 70, 42, 0, 2 * 3.14)
if controls['instr'] <= piano_max:
    ctx.set_source_rgb(*color_piano_dark)
if synth_min <= controls['instr'] <= synth_max:
    ctx.set_source_rgb(*color_synth_dark)
if controls['instr'] >= sampler_min:
    ctx.set_source_rgb(*color_sampler_dark)
ctx.fill()
ctx.stroke()

# Instrument_filter canvas (value - inverted)
ctx.move_to(180, 70)
ctx.arc(180, 70, 42, 3.14 / 2, 3.14 / 2 + 360 * (controls['instr_lpf'] / 127) * (3.14 / 180))
ctx.close_path()
ctx.set_source_rgb(*screen_black)
ctx.fill()
ctx.stroke()

# Instrument_filter frame
ctx.arc(180, 70, 40, 0, 2 * 3.14)
if controls['instr_lpf'] == 127:
    ctx.set_source_rgb(*screen_dark)
else:
    if controls['instr'] <= piano_max:
        ctx.set_source_rgb(*color_piano)
    if synth_min <= controls['instr'] <= synth_max:
        ctx.set_source_rgb(*color_synth)
    if controls['instr'] >= sampler_min:
        ctx.set_source_rgb(*color_sampler)
ctx.set_line_width(10)
ctx.stroke()

# Instrument filter indicator
pos1 = 3.14 / 2 + 360 * ((controls['instr_lpf'] - 5) / 127) * (3.14 / 180)
pos2 = 3.14 / 2 + 360 * ((controls['instr_lpf'] + 5) / 127) * (3.14 / 180)

# Instrument filter indicator frame
ctx.set_line_cap(cairo.LINE_CAP_ROUND)
if controls['instr_lpf'] == 127:
    ctx.set_source_rgb(*screen_dark)
else:
    if controls['instr'] <= piano_max:
        ctx.set_source_rgb(*color_piano_light)
    if synth_min <= controls['instr'] <= synth_max:
        ctx.set_source_rgb(*color_synth_light)
    if controls['instr'] >= sampler_min:
        ctx.set_source_rgb(*color_sampler_light)
ctx.move_to(180, 70)
ctx.arc(180, 70, 46, pos1, pos2)
ctx.line_to(180, 70)
ctx.set_line_width(3)
ctx.stroke()
ctx.set_line_cap(cairo.LINE_CAP_BUTT)

# Instrument filter indicator inner
if controls['instr_lpf'] == 127:
    ctx.set_source_rgb(*screen_dark)
else:
    if controls['instr'] <= piano_max:
        ctx.set_source_rgb(*color_piano)
    if synth_min <= controls['instr'] <= synth_max:
        ctx.set_source_rgb(*color_synth)
    if controls['instr'] >= sampler_min:
        ctx.set_source_rgb(*color_sampler)
ctx.arc(180, 70, 42, pos1, pos2)
ctx.line_to(180, 70)
ctx.fill()

# Instrument filter indicator outer
if controls['instr_lpf'] == 127:
    ctx.set_source_rgb(*screen_dark)
else:
    if controls['instr'] <= piano_max:
        ctx.set_source_rgb(*color_piano_light)
    if synth_min <= controls['instr'] <= synth_max:
        ctx.set_source_rgb(*color_synth_light)
    if controls['instr'] >= sampler_min:
        ctx.set_source_rgb(*color_sampler_light)
ctx.arc(180, 70, 40, pos1, pos2)
ctx.set_line_width(12)
ctx.stroke()

# Instrument volume
pos1 = 3.14 / 2 + 360 * ((controls['instr_vol'] - 5) / 127) * (3.14 / 180)
pos2 = 3.14 / 2 + 360 * ((controls['instr_vol'] + 5) / 127) * (3.14 / 180)
center_x = 300

# Instrument_volume title
if controls['instr'] <= piano_max:
    ctx.set_source_rgb(*color_piano)
if synth_min <= controls['instr'] <= synth_max:
    ctx.set_source_rgb(*color_synth)
if controls['instr'] >= sampler_min:
    ctx.set_source_rgb(*color_sampler)
s = "INSTR. LVL:"
ctx.move_to(300 - (ctx.text_extents(s)[2] / 2), 15)
ctx.show_text(s)

ctx.stroke()

# Instrument_volume value 1 (inverted canvas)
if controls['instr_vol'] >= 100:
    ctx.set_source_rgb(*color_piano_light)
else:
    ctx.set_source_rgb(*screen_dark)
ctx.arc(300, 70, 42, 2 * 3.14, 3.14 / 2 + 360 * (controls['instr_vol'] / 127) * (3.14 / 180))
ctx.line_to(300, 70)
ctx.fill()
ctx.stroke()

# Instrument_volume value 2 (inverted canvas)
if controls['instr_vol'] <= 90:
    ctx.set_source_rgb(*color_piano_dark)
if controls['instr_vol'] >= 100:
    ctx.set_source_rgb(*color_piano_dark)
ctx.arc(300, 70, 42, 3.14 / 2 + 360 * (controls['instr_vol'] / 127) * (3.14 / 180), 2 * 3.14)
ctx.line_to(300, 70)
ctx.fill()
ctx.stroke()

# ## Instrument_volume frame
ctx.arc(300, 70, 40, 0.5 * 3.14, 2 * 3.14)
if controls['instr_vol'] <= 90:
    if controls['instr'] <= piano_max:
        ctx.set_source_rgb(*color_piano)
    if synth_min <= controls['instr'] <= synth_max:
        ctx.set_source_rgb(*color_synth)
    if controls['instr'] >= sampler_min:
        ctx.set_source_rgb(*color_sampler)
elif controls['instr_vol'] >= 100:
    ctx.set_source_rgb(*screen_dark)
    if controls['instr'] <= piano_max:
        ctx.set_source_rgb(*color_piano_light)
    if synth_min <= controls['instr'] <= synth_max:
        ctx.set_source_rgb(*color_synth_light)
    if controls['instr'] >= sampler_min:
        ctx.set_source_rgb(*color_sampler_light)
else:
    ctx.set_source_rgb(*screen_dark)

ctx.set_line_width(10)
ctx.stroke()

# Instrument_volume frame 2 !!!
ctx.arc(300, 70, 40, 0 * 3.14, 0.5 * 3.14)
if controls['instr_vol'] <= 90:
    if controls['instr'] <= piano_max:
        ctx.set_source_rgb(*color_piano_dark)
    if synth_min <= controls['instr'] <= synth_max:
        ctx.set_source_rgb(*color_synth_dark)
    if controls['instr'] >= sampler_min:
        ctx.set_source_rgb(*color_sampler_dark)
elif controls['instr_vol'] >= 100:
    ctx.set_source_rgb(*screen_dark)
    if controls['instr'] <= piano_max:
        ctx.set_source_rgb(*color_piano_light)
    if synth_min <= controls['instr'] <= synth_max:
        ctx.set_source_rgb(*color_synth_light)
    if controls['instr'] >= sampler_min:
        ctx.set_source_rgb(*color_sampler_light)
else:
    ctx.set_source_rgb(*screen_dark)

ctx.set_line_width(10)
ctx.stroke()

# Instrument indicator frame
ctx.set_line_cap(cairo.LINE_CAP_ROUND)
if controls['instr_vol'] <= 90:
    if controls['instr'] <= piano_max:
        ctx.set_source_rgb(*color_piano_light)
    if synth_min <= controls['instr'] <= synth_max:
        ctx.set_source_rgb(*color_synth_light)
    if controls['instr'] >= sampler_min:
        ctx.set_source_rgb(*color_sampler_light)
elif controls['instr_vol'] >= 100:
    if controls['instr'] <= piano_max:
        ctx.set_source_rgb(*color_piano)
    if synth_min <= controls['instr'] <= synth_max:
        ctx.set_source_rgb(*color_synth)
    if controls['instr'] >= sampler_min:
        ctx.set_source_rgb(*color_sampler)
else:
    ctx.set_source_rgb(*screen_dark)
ctx.move_to(center_x, 70)
ctx.arc(center_x, 70, 46, pos1, pos2)
ctx.line_to(center_x, 70)
ctx.set_line_width(3)
ctx.stroke()
ctx.set_line_cap(cairo.LINE_CAP_BUTT)

# Instrument_volume indicator inner
if controls['instr_vol'] <= 90:
    if controls['instr'] <= piano_max:
        ctx.set_source_rgb(*color_piano)
    if synth_min <= controls['instr'] <= synth_max:
        ctx.set_source_rgb(*color_synth)
    if controls['instr'] >= sampler_min:
        ctx.set_source_rgb(*color_sampler)
elif controls['instr_vol'] >= 100:
    ctx.set_source_rgb(*screen_dark)
    if controls['instr'] <= piano_max:
        ctx.set_source_rgb(*color_piano_light)
    if synth_min <= controls['instr'] <= synth_max:
        ctx.set_source_rgb(*color_synth_light)
    if controls['instr'] >= sampler_min:
        ctx.set_source_rgb(*color_sampler_light)
else:
    ctx.set_source_rgb(*screen_dark)

ctx.arc(300, 70, 42, pos1, pos2)
ctx.line_to(300, 70)
ctx.fill()

# Instrument_volume indicator outer
if controls['instr_vol'] <= 90:
    if controls['instr'] <= piano_max:
        ctx.set_source_rgb(*color_piano_light)
    if synth_min <= controls['instr'] <= synth_max:
        ctx.set_source_rgb(*color_synth_light)
    if controls['instr'] >= sampler_min:
        ctx.set_source_rgb(*color_sampler_light)
elif controls['instr_vol'] >= 100:
    if controls['instr'] <= piano_max:
        ctx.set_source_rgb(*color_piano)
    if synth_min <= controls['instr'] <= synth_max:
        ctx.set_source_rgb(*color_synth)
    if controls['instr'] >= sampler_min:
        ctx.set_source_rgb(*color_sampler)
else:
    ctx.set_source_rgb(*screen_dark)

ctx.arc(300, 70, 40, pos1, pos2)
ctx.set_line_width(12)
ctx.stroke()

# Master filter QUASI-GLOBALS
title = "MASTER LPF:"
control = controls['master_lpf']
color = [1, 0.5, 0.1]
color_light = [1, 0.75, 0.64]
color_dark = [0.5, 0.25, 0.05]
center_x = 420

pos1 = 3.14 / 2 + 360 * ((control - 5) / 127) * (3.14 / 180)
pos2 = 3.14 / 2 + 360 * ((control + 5) / 127) * (3.14 / 180)

# Master_filter title
ctx.move_to(center_x - (ctx.text_extents(title)[2] / 2), 15)
ctx.set_source_rgb(*color)
ctx.show_text(title)
ctx.stroke()

# Master_filter value (canvas - inverted)
ctx.arc(center_x, 70, 42, 0, 2 * 3.14)
ctx.set_source_rgb(*color_dark)
# pattern = cairo.LinearGradient(center_x - 36, 70, center_x + 36, 70)
# pattern.add_color_stop_rgb(0, *color)
# pattern.add_color_stop_rgb(1, *color_dark)
# ctx.set_source(pattern)
ctx.fill()
ctx.stroke()

# Master_filter canvas (value - inverted)
ctx.move_to(center_x, 70)
ctx.arc(center_x, 70, 42, 3.14 / 2, 3.14 / 2 + 360 * (control / 127) * (3.14 / 180))
ctx.close_path()
ctx.set_source_rgb(*screen_black)
ctx.fill()
ctx.stroke()

# Master_filter frame
ctx.arc(center_x, 70, 40, 0, 2 * 3.14)
if control == 127:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(*color)
ctx.set_line_width(10)
ctx.stroke()

# Master filter indicator frame
ctx.set_line_cap(cairo.LINE_CAP_ROUND)
if control == 127:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(*color_light)
ctx.move_to(center_x, 70)
ctx.arc(center_x, 70, 46, pos1, pos2)
ctx.line_to(center_x, 70)
ctx.set_line_width(3)
ctx.stroke()
ctx.set_line_cap(cairo.LINE_CAP_BUTT)

# Master filter indicator
if control == 127:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(1, 0.5, 0.1)
ctx.arc(center_x, 70, 42, pos1, pos2)
ctx.line_to(center_x, 70)
ctx.fill()

if control == 127:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(*color_light)
ctx.arc(center_x, 70, 40, pos1, pos2)
ctx.set_line_width(12)
ctx.stroke()

# FX QUASI-GLOBALS
title = "FX LVL:"
control = controls['fx']
color = [0.75, 0, 1]
color_light = [1, 0.64, 1]
color_dark = [0.35, 0, 0.5]
center_x = 540

pos1 = 3.14 / 2 + 360 * ((control - 5) / 127) * (3.14 / 180)
pos2 = 3.14 / 2 + 360 * ((control + 5) / 127) * (3.14 / 180)

# FX title
ctx.set_source_rgb(*color)
ctx.move_to(center_x - (ctx.text_extents(title)[2] / 2), 15)
ctx.show_text(title)
ctx.stroke()

# FX value (canvas inverted)
ctx.arc(center_x, 70, 42, 0, 2 * 3.14)
ctx.set_source_rgb(*color_dark)
ctx.fill()
ctx.stroke()

# FX canvas (value inverted)
ctx.move_to(center_x, 70)
ctx.arc(center_x, 70, 42, 3.14 / 2, 3.14 / 2 + 360 * (controls['fx'] / 127) * (3.14 / 180))
ctx.close_path()
ctx.set_source_rgb(*screen_black)
ctx.fill()
ctx.stroke()

# FX frame
ctx.arc(center_x, 70, 40, 0, 2 * 3.14)
if controls['fx'] == 127:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(*color)
ctx.set_line_width(10)
ctx.stroke()

# FX indicator frame
ctx.set_line_cap(cairo.LINE_CAP_ROUND)
if control == 127:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(*color_light)
ctx.move_to(center_x, 70)
ctx.arc(center_x, 70, 46, pos1, pos2)
ctx.line_to(center_x, 70)
ctx.set_line_width(3)
ctx.stroke()
ctx.set_line_cap(cairo.LINE_CAP_BUTT)

# FX indicator
if control == 127:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(*color)
ctx.arc(center_x, 70, 42, pos1, pos2)
ctx.line_to(center_x, 70)
ctx.fill()

if controls['fx'] == 127:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(*color_light)
ctx.arc(center_x, 70, 40, pos1, pos2)
ctx.set_line_width(12)
ctx.stroke()

# Smile QUASI-GLOBALS
title = "SMILE:"
control = controls['smile']
color = [1, 1, 0]
color_light = [1, 1, 0.75]
color_dark = [0.5, 0.5, 0]
center_x = 660

pos1 = 3.14 / 2 + 360 * ((control - 5) / 127) * (3.14 / 180)
pos2 = 3.14 / 2 + 360 * ((control + 5) / 127) * (3.14 / 180)

# Smile title
ctx.set_source_rgb(*color)
ctx.move_to(center_x - (ctx.text_extents(title)[2] / 2), 15)
ctx.show_text(title)
ctx.stroke()

# Smile canvas
ctx.arc(center_x, 70, 42, 0, 2 * 3.14)
ctx.set_source_rgb(*screen_black)
ctx.fill()
ctx.stroke()

# Smile value
ctx.move_to(center_x, 70)
ctx.arc(center_x, 70, 42, 3.14 / 2, 3.14 / 2 + 360 * (control / 127) * (3.14 / 180))
ctx.close_path()
ctx.set_source_rgb(*color_dark)
ctx.fill()
ctx.stroke()

# Smile frame
ctx.arc(center_x, 70, 40, 0, 2 * 3.14)
if control == 0:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(*color)
ctx.set_line_width(10)
ctx.stroke()

# Smile indicator frame
ctx.set_line_cap(cairo.LINE_CAP_ROUND)
if control == 0:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(*color_light)
ctx.move_to(center_x, 70)
ctx.arc(center_x, 70, 46, pos1, pos2)
ctx.line_to(center_x, 70)
ctx.set_line_width(3)
ctx.stroke()
ctx.set_line_cap(cairo.LINE_CAP_BUTT)

# Smile indicator
if control == 0:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(*color)
ctx.arc(center_x, 70, 42, pos1, pos2)
ctx.line_to(center_x, 70)
ctx.fill()
if control == 0:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(*color_light)
ctx.arc(center_x, 70, 40, pos1, pos2)
ctx.set_line_width(12)
ctx.stroke()

# Reverb QUASI-GLOBALS
title = "REVERB:"
control = controls['reverb']
color = [0, 0.85, 1]
color_light = [0.75, 1, 1]
color_dark = [0, 0.425, 0.5]
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
ctx.arc(center_x, 70, 42, 0, 2 * 3.14)
ctx.set_source_rgb(*screen_black)
ctx.fill()
ctx.stroke()

# Reverb value
ctx.move_to(center_x, 70)
ctx.arc(center_x, 70, 42, 3.14 / 2, 3.14 / 2 + 360 * (controls['reverb'] / 127) * (3.14 / 180))
ctx.close_path()
ctx.set_source_rgb(*color_dark)
ctx.fill()
ctx.stroke()

# Reverb frame
ctx.arc(center_x, 70, 40, 0, 2 * 3.14)
if controls['reverb'] == 0:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(*color)
ctx.set_line_width(10)
ctx.stroke()

# Reverb indicator frame
ctx.set_line_cap(cairo.LINE_CAP_ROUND)
if control == 0:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(*color_light)
ctx.move_to(center_x, 70)
ctx.arc(center_x, 70, 46, pos1, pos2)
ctx.line_to(center_x, 70)
ctx.set_line_width(3)
ctx.stroke()
ctx.set_line_cap(cairo.LINE_CAP_BUTT)

# Reverb indicator
if controls['reverb'] == 0:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(*color)
ctx.arc(center_x, 70, 42, pos1, pos2)
ctx.line_to(center_x, 70)
ctx.fill()
if controls['reverb'] == 0:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(*color_light)
ctx.arc(center_x, 70, 40, pos1, pos2)
ctx.set_line_width(12)
ctx.stroke()

# Tape QUASI-GLOBALS
title = "TAPE:"
control = controls['tape']
color = [1, 0.25, 0.25]
color_light = [1, 0.75, 0.75]
color_dark = [0.5, 0, 0]
center_x = 900

pos1 = 3.14 / 2 + 360 * ((controls['tape'] - 5) / 127) * (3.14 / 180)
pos2 = 3.14 / 2 + 360 * ((controls['tape'] + 5) / 127) * (3.14 / 180)

# Tape title
ctx.set_source_rgb(*color)
ctx.move_to(center_x - (ctx.text_extents(title)[2] / 2), 15)
ctx.show_text(title)
ctx.stroke()

# Tape value (canvas inverted)
ctx.arc(center_x, 70, 42, 0, 2 * 3.14)
ctx.set_source_rgb(*color_dark)
ctx.fill()
ctx.stroke()

# Tape canvas (value inverted)
ctx.move_to(center_x, 70)
ctx.arc(center_x, 70, 42, 3.14 / 2, 3.14 / 2 + 360 * (controls['tape'] / 127) * (3.14 / 180))
ctx.close_path()
ctx.set_source_rgb(*screen_black)
ctx.fill()
ctx.stroke()

# Tape frame
ctx.arc(center_x, 70, 40, 0, 2 * 3.14)
if controls['tape'] == 127:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(*color)
ctx.set_line_width(10)
ctx.stroke()

# Tape indicator frame
ctx.set_line_cap(cairo.LINE_CAP_ROUND)
if control == 127:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(*color_light)
ctx.move_to(center_x, 70)
ctx.arc(center_x, 70, 46, pos1, pos2)
ctx.line_to(center_x, 70)
ctx.set_line_width(3)
ctx.stroke()
ctx.set_line_cap(cairo.LINE_CAP_BUTT)

# Tape indicator
if controls['tape'] == 127:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(*color)
ctx.arc(center_x, 70, 42, pos1, pos2)
ctx.line_to(center_x, 70)
ctx.fill()
if controls['tape'] == 127:
    ctx.set_source_rgb(*screen_dark)
else:
    ctx.set_source_rgb(*color_light)
ctx.arc(center_x, 70, 40, pos1, pos2)
ctx.set_line_width(12)
ctx.stroke()

# CUE 1
ctx.move_to(50, 135)
ctx.curve_to(60, 130, 60, 140, 70, 135)
ctx.line_to(70, 145)
ctx.curve_to(60, 150, 60, 140, 50, 145)
ctx.close_path()
ctx.move_to(50, 135)
ctx.line_to(50, 155)

# CUE 2
ctx.move_to(170, 135)
ctx.curve_to(180, 130, 180, 140, 190, 135)
ctx.line_to(190, 145)
ctx.curve_to(180, 150, 180, 140, 170, 145)
ctx.close_path()
ctx.move_to(170, 135)
ctx.line_to(170, 155)
ctx.set_source_rgb(1, 1, 1)
ctx.set_line_width(2.5)
ctx.stroke()

# BAR 1
ctx.move_to(300, 145)
ctx.line_to(300, 155)

ctx.move_to(290, 135)
ctx.line_to(310, 135)
ctx.line_to(300, 145)
ctx.close_path()

ctx.move_to(295, 155)
ctx.line_to(305, 155)

# BAR 2
ctx.move_to(420, 145)
ctx.line_to(420, 155)

ctx.move_to(410, 135)
ctx.line_to(430, 135)
ctx.line_to(420, 145)
ctx.close_path()

ctx.move_to(415, 155)
ctx.line_to(425, 155)

ctx.set_source_rgb(1, 1, 0)
ctx.set_line_width(2.5)
ctx.stroke()

# BEAT 1
ctx.move_to(540, 140)
ctx.curve_to(540, 130, 555, 130, 550, 142)
ctx.curve_to(550, 143, 542, 152, 540, 155)
ctx.curve_to(538, 152, 530, 143, 530, 142)
ctx.curve_to(525, 130, 540, 130, 540, 140)
ctx.close_path()

# BEAT 2
ctx.move_to(660, 140)
ctx.curve_to(660, 130, 675, 130, 670, 142)
ctx.curve_to(670, 143, 662, 152, 660, 155)
ctx.curve_to(658, 152, 650, 143, 650, 142)
ctx.curve_to(645, 130, 660, 130, 660, 140)
ctx.close_path()

ctx.set_line_cap(cairo.LINE_CAP_ROUND)
ctx.set_source_rgb(1, 0.4, 0)
ctx.set_line_width(2.5)
ctx.stroke()

# NUDGE 1
ctx.move_to(769, 136)
ctx.line_to(769, 154)
ctx.set_source_rgb(1, 0.4, 0.6)
ctx.set_line_width(5)
ctx.set_line_cap(cairo.LINE_CAP_SQUARE)
ctx.stroke()

ctx.move_to(780, 135)
ctx.line_to(780, 155)
ctx.set_source_rgb(1, 0.4, 0.6)
ctx.set_line_width(2.5)
ctx.stroke()

ctx.move_to(790, 135)
ctx.line_to(790, 155)
ctx.set_source_rgb(1, 0.4, 0.6)
ctx.set_line_width(2.5)
ctx.stroke()

# NUDGE 2
ctx.move_to(890, 135)
ctx.line_to(890, 155)
ctx.set_source_rgb(1, 0.4, 0.6)
ctx.set_line_width(2.5)
ctx.set_line_cap(cairo.LINE_CAP_SQUARE)
ctx.stroke()

ctx.move_to(900, 135)
ctx.line_to(900, 155)
ctx.set_source_rgb(1, 0.4, 0.6)
ctx.set_line_width(2.5)
ctx.stroke()

ctx.move_to(911, 136)
ctx.line_to(911, 154)
ctx.set_source_rgb(1, 0.4, 0.6)
ctx.set_line_width(5)
ctx.stroke()

# End of drawing code

surface.write_to_png('screenshot.png')
