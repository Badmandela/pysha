import cairo
import push2_python

controls = {'instr': 0, 'instr_lpf': 127, 'instr_vol': 96, 'master_lpf': 64, 'fx': 64, 'smile': 64, 'reverb': 64, 'tape': 64}

piano_max = 31
synth_min = 32
synth_max = 95
sampler_min = 96

w, h = push2_python.constants.DISPLAY_LINE_PIXELS, push2_python.constants.DISPLAY_N_LINES
surface = cairo.ImageSurface(cairo.FORMAT_RGB16_565, w, h)
ctx = cairo.Context(surface)


# Initial black rectangle
ctx.rectangle(0, 0, w, h)
ctx.set_source_rgb(0, 0, 0)
ctx.fill()

font = "Verdana"
normal = cairo.FONT_SLANT_NORMAL
bold = cairo.FONT_WEIGHT_BOLD

# Instrument title
ctx.set_font_size(12)
ctx.select_font_face(font, normal, bold)
s = "INSTRUMENT:"
ctx.move_to(60 - (ctx.text_extents(s)[2] / 2), 15)
if controls['instr'] <= piano_max:
    ctx.set_source_rgb(1, 0.25, 0.5)
if synth_min <= controls['instr'] <= synth_max:
    ctx.set_source_rgb(0, 1, 0.7)
if controls['instr'] >= sampler_min:
    ctx.set_source_rgb(0.75, 0, 1)
ctx.show_text(s)

# Instrument canvas
ctx.rectangle(15, 23 + (30 * (controls['instr'] / 127)), 90, 15)
if controls['instr'] <= piano_max:
    ctx.set_source_rgb(1, 0.25, 0.5)
if synth_min <= controls['instr'] <= synth_max:
    ctx.set_source_rgb(0, 0.9, 0.6)
if controls['instr'] >= sampler_min:
    ctx.set_source_rgb(0.75, 0, 1)
ctx.fill()
ctx.stroke()

# Instruments list
ctx.set_source_rgb(1, 1, 1)
ctx.set_font_size(12)
ctx.select_font_face(font, cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_NORMAL)

# Piano
s = "PIANO"
ctx.move_to(60 - (ctx.text_extents(s)[2] / 2), 35)
ctx.show_text(s)

# Synth
s = "SYNTH"
ctx.move_to(60 - (ctx.text_extents(s)[2] / 2), 50)
ctx.show_text(s)

# Sampler
s = "SAMPLER"
ctx.move_to(60 - (ctx.text_extents(s)[2] / 2), 65)
ctx.show_text(s)

# Instrument_filter title
if controls['instr'] <= piano_max:
    ctx.set_source_rgb(1, 0.25, 0.5)
if synth_min <= controls['instr'] <= synth_max:
    ctx.set_source_rgb(0, 1, 0.7)
if controls['instr'] >= sampler_min:
    ctx.set_source_rgb(0.75, 0, 1)
ctx.set_font_size(12)
ctx.select_font_face(font, normal, bold)
s = "INSTRUMENT LPF:"
ctx.move_to(180 - (ctx.text_extents(s)[2] / 2), 15)
ctx.show_text(s)

# Instrument_filter value (canvas - inverted)
ctx.arc(180, 70, 42, 0, 2 * 3.14)
if controls['instr'] <= piano_max:
    ctx.set_source_rgb(0.5, 0.125, 0.25)
if synth_min <= controls['instr'] <= synth_max:
    ctx.set_source_rgb(0, 0.5, 0.45)
if controls['instr'] >= sampler_min:
    ctx.set_source_rgb(0.425, 0, 0.5)
ctx.fill()
ctx.stroke()

# Instrument_filter canvas (value - inverted)
ctx.move_to(180, 70)
ctx.arc(180, 70, 42, 3.14 / 2, 3.14 / 2 + 360 * (controls['instr_lpf'] / 127) * (3.14 / 180))
ctx.close_path()
ctx.set_source_rgb(0.02, 0.02, 0.02)
ctx.fill()
ctx.stroke()

# Instrument_filter frame
ctx.arc(180, 70, 40, 0, 2 * 3.14)
if controls['instr_lpf'] == 127:
    ctx.set_source_rgb(0.032, 0.032, 0.032)
else:
    if controls['instr'] <= piano_max:
        ctx.set_source_rgb(1, 0.25, 0.5)
    if synth_min <= controls['instr'] <= synth_max:
        ctx.set_source_rgb(0.05, 0.9, 0.7)
    if controls['instr'] >= sampler_min:
        ctx.set_source_rgb(0.75, 0, 1)
ctx.set_line_width(10)
ctx.stroke()

# Instrument filter indicator
pos1 = 3.14 / 2 + 360 * ((controls['instr_lpf'] - 5) / 127) * (3.14 / 180)
pos2 = 3.14 / 2 + 360 * ((controls['instr_lpf'] + 5) / 127) * (3.14 / 180)

if controls['instr_lpf'] == 127:
    ctx.set_source_rgb(0.032, 0.032, 0.032)
else:
    if controls['instr'] <= piano_max:
        ctx.set_source_rgb(1, 0.25, 0.5)
    if synth_min <= controls['instr'] <= synth_max:
        ctx.set_source_rgb(0.05, 0.9, 0.7)
    if controls['instr'] >= sampler_min:
        ctx.set_source_rgb(0.75, 0, 1)
ctx.arc(180, 70, 42, pos1, pos2)
ctx.line_to(180, 70)
ctx.fill()

if controls['instr_lpf'] == 127:
    ctx.set_source_rgb(0.032, 0.032, 0.032)
else:
    if controls['instr'] <= piano_max:
        ctx.set_source_rgb(1, 0.5, 0.75)
    if synth_min <= controls['instr'] <= synth_max:
        ctx.set_source_rgb(0.5, 1, 0.95)
    if controls['instr'] >= sampler_min:
        ctx.set_source_rgb(0.9, 0.25, 1)

ctx.arc(180, 70, 40, pos1, pos2)
ctx.set_line_width(12)
ctx.stroke()

# Instrument volume
pos1 = 3.14 / 2 + 360 * ((controls['instr_vol'] - 5) / 127) * (3.14 / 180)
pos2 = 3.14 / 2 + 360 * ((controls['instr_vol'] + 5) / 127) * (3.14 / 180)

# Instrument_volume title
ctx.set_font_size(12)
if controls['instr'] <= piano_max:
    ctx.set_source_rgb(1, 0.25, 0.5)
if synth_min <= controls['instr'] <= synth_max:
    ctx.set_source_rgb(0, 1, 0.7)
if controls['instr'] >= sampler_min:
    ctx.set_source_rgb(0.75, 0, 1)
ctx.select_font_face(font, normal, bold)
s = "INSTR. LVL:"
ctx.move_to(300 - (ctx.text_extents(s)[2] / 2), 15)
ctx.show_text(s)

# Instrument_volume canvas
ctx.set_source_rgb(0.02, 0.02, 0.02)
ctx.arc(300, 70, 42, 0, 2 * 3.14)
ctx.fill()
ctx.stroke()

# Instrument_volume frame
ctx.arc(300, 70, 40, 0, 2 * 3.14)
ctx.set_source_rgb(0.032, 0.032, 0.032)
ctx.set_line_width(10)
ctx.stroke()

# Instrument_volume indicator
if controls['instr_vol'] == 0:
    ctx.set_source_rgb(0.032, 0.032, 0.032)
else:
    if controls['instr'] <= piano_max:
        ctx.set_source_rgb(0.5, 0.125, 0.25)
    if synth_min <= controls['instr'] <= synth_max:
        ctx.set_source_rgb(0, 0.5, 0.45)
    if controls['instr'] >= sampler_min:
        ctx.set_source_rgb(0.425, 0, 0.5)

ctx.arc(300, 70, 42, pos1, pos2)
ctx.line_to(300, 70)
ctx.fill()

if controls['instr_vol'] == 0:
    ctx.set_source_rgb(0.032, 0.032, 0.032)
else:
    if controls['instr'] <= piano_max:
        ctx.set_source_rgb(1, 0.25, 0.5)
    if synth_min <= controls['instr'] <= synth_max:
        ctx.set_source_rgb(0, 1, 0.7)
    if controls['instr'] >= sampler_min:
        ctx.set_source_rgb(0.75, 0, 1)

ctx.arc(300, 70, 40, pos1, pos2)
ctx.set_line_width(12)
ctx.stroke()

# Master_filter title
ctx.set_source_rgb(1, 0.5, 0.1)
ctx.set_font_size(12)
ctx.select_font_face(font, normal, bold)
s = "MASTER LPF:"
ctx.move_to(420 - (ctx.text_extents(s)[2] / 2), 15)
ctx.show_text(s)
ctx.stroke()

# Master_filter value (canvas - inverted)
ctx.arc(420, 70, 42, 0, 2 * 3.14)
ctx.set_source_rgb(0.5, 0.25, 0.05)
if controls['master_lpf'] == 127:
    ctx.set_source_rgb(0.1, 0.05, 0.01)
ctx.fill()
ctx.stroke()

# Master_filter canvas (value - inverted)
ctx.move_to(420, 70)
ctx.arc(420, 70, 42, 3.14 / 2, 3.14 / 2 + 360 * (controls['master_lpf'] / 127) * (3.14 / 180))
ctx.close_path()
ctx.set_source_rgb(0.02, 0.02, 0.02)
ctx.fill()
ctx.stroke()

# Master_filter frame
ctx.arc(420, 70, 40, 0, 2 * 3.14)
if controls['master_lpf'] == 127:
    ctx.set_source_rgb(0.032, 0.032, 0.032)
else:
    ctx.set_source_rgb(1, 0.5, 0.1)
ctx.set_line_width(10)
ctx.stroke()

# Master filter indicator
pos1 = 3.14 / 2 + 360 * ((controls['master_lpf'] - 5) / 127) * (3.14 / 180)
pos2 = 3.14 / 2 + 360 * ((controls['master_lpf'] + 5) / 127) * (3.14 / 180)

ctx.arc(420, 70, 42, pos1, pos2)
ctx.line_to(420, 70)
ctx.fill()

if controls['master_lpf'] == 127:
    ctx.set_source_rgb(0.032, 0.032, 0.032)
else:
    ctx.set_source_rgb(1, 0.75, 0.3)
ctx.arc(420, 70, 40, pos1, pos2)
ctx.set_line_width(12)
ctx.stroke()

# FX
pos1 = 3.14 / 2 + 360 * ((controls['fx'] - 5) / 127) * (3.14 / 180)
pos2 = 3.14 / 2 + 360 * ((controls['fx'] + 5) / 127) * (3.14 / 180)

# FX mix title
ctx.set_source_rgb(0.75, 0, 1)
ctx.set_font_size(12)
ctx.select_font_face(font, normal, bold)
s = "FX LVL:"
ctx.move_to(540 - (ctx.text_extents(s)[2] / 2), 15)
ctx.show_text(s)
ctx.stroke()

# FX value (canvas inverted)
ctx.arc(540, 70, 42, 0, 2 * 3.14)
ctx.set_source_rgb(0.35, 0, 0.5)
if controls['fx'] == 127:
    ctx.set_source_rgb(0.075, 0, 0.075)
ctx.fill()
ctx.stroke()

# FX canvas (value inverted)
ctx.move_to(540, 70)
ctx.arc(540, 70, 42, 3.14 / 2, 3.14 / 2 + 360 * (controls['fx'] / 127) * (3.14 / 180))
ctx.close_path()
ctx.set_source_rgb(0.02, 0.02, 0.02)
ctx.fill()
ctx.stroke()

# FX frame
ctx.arc(540, 70, 40, 0, 2 * 3.14)
if controls['fx'] == 127:
    ctx.set_source_rgb(0.032, 0.032, 0.032)
else:
    ctx.set_source_rgb(0.75, 0, 1)
ctx.set_line_width(10)
ctx.stroke()

# FX indicator
ctx.arc(540, 70, 42, pos1, pos2)
ctx.line_to(540, 70)
ctx.fill()

if controls['fx'] == 127:
    ctx.set_source_rgb(0.032, 0.032, 0.032)
else:
    ctx.set_source_rgb(1, 0.5, 1)
ctx.arc(540, 70, 40, pos1, pos2)
ctx.set_line_width(12)
ctx.stroke()

# Smile
pos1 = 3.14 / 2 + 360 * ((controls['smile'] - 5) / 127) * (3.14 / 180)
pos2 = 3.14 / 2 + 360 * ((controls['smile'] + 5) / 127) * (3.14 / 180)

# Smile title
ctx.set_source_rgb(1, 1, 0)
ctx.set_font_size(12)
ctx.select_font_face(font, normal, bold)
s = "SMILE:"
ctx.move_to(660 - (ctx.text_extents(s)[2] / 2), 15)
ctx.show_text(s)
ctx.stroke()

# Smile canvas
ctx.arc(660, 70, 42, 0, 2 * 3.14)
ctx.set_source_rgb(0.02, 0.02, 0.02)
# if controls['smile'] == 127:
#     ctx.set_source_rgb(0.5, 0.5, 0)
ctx.fill()
ctx.stroke()

# Smile value
ctx.move_to(660, 70)
ctx.arc(660, 70, 42, 3.14 / 2, 3.14 / 2 + 360 * (controls['smile'] / 127) * (3.14 / 180))
ctx.close_path()
ctx.set_source_rgb(0.5, 0.5, 0)
ctx.fill()
ctx.stroke()

# Smile frame
ctx.arc(660, 70, 40, 0, 2 * 3.14)
if controls['smile'] == 0:
    ctx.set_source_rgb(0.032, 0.032, 0.032)
else:
    ctx.set_source_rgb(1, 1, 0)
ctx.set_line_width(10)
ctx.stroke()

# Smile indicator
ctx.arc(660, 70, 42, pos1, pos2)
ctx.line_to(660, 70)
ctx.fill()
if controls['smile'] == 0:
    ctx.set_source_rgb(0.032, 0.032, 0.032)
else:
    ctx.set_source_rgb(1, 1, 0.5)
ctx.arc(660, 70, 40, pos1, pos2)
ctx.set_line_width(12)
ctx.stroke()

# Reverb
pos1 = 3.14 / 2 + 360 * ((controls['reverb'] - 5) / 127) * (3.14 / 180)
pos2 = 3.14 / 2 + 360 * ((controls['reverb'] + 5) / 127) * (3.14 / 180)

# Reverb title
ctx.set_source_rgb(0, 1, 1)
ctx.set_font_size(12)
ctx.select_font_face(font, normal, bold)
s = "REVERB:"
ctx.move_to(780 - (ctx.text_extents(s)[2] / 2), 15)
ctx.show_text(s)
ctx.stroke()

# Reverb canvas
ctx.arc(780, 70, 42, 0, 2 * 3.14)
ctx.set_source_rgb(0.02, 0.02, 0.02)
if controls['reverb'] == 127:
    ctx.set_source_rgb(0.5, 1, 1)
ctx.fill()
ctx.stroke()

# Reverb value
ctx.move_to(780, 70)
ctx.arc(780, 70, 42, 3.14 / 2, 3.14 / 2 + 360 * (controls['reverb'] / 127) * (3.14 / 180))
ctx.close_path()
ctx.set_source_rgb(0, 0.425, 0.5)
ctx.fill()
ctx.stroke()

# Reverb frame
ctx.arc(780, 70, 40, 0, 2 * 3.14)
if controls['reverb'] == 0:
    ctx.set_source_rgb(0.032, 0.032, 0.032)
else:
    ctx.set_source_rgb(0, 0.75, 1)
ctx.set_line_width(10)
ctx.stroke()

# Reverb indicator
ctx.arc(780, 70, 42, pos1, pos2)
ctx.line_to(780, 70)
ctx.fill()
if controls['reverb'] == 0:
    ctx.set_source_rgb(0.032, 0.032, 0.032)
else:
    ctx.set_source_rgb(0.5, 1, 1)
ctx.arc(780, 70, 40, pos1, pos2)
ctx.set_line_width(12)
ctx.stroke()

# Tape
pos1 = 3.14 / 2 + 360 * ((controls['tape'] - 5) / 127) * (3.14 / 180)
pos2 = 3.14 / 2 + 360 * ((controls['tape'] + 5) / 127) * (3.14 / 180)

# Tape title
ctx.set_source_rgb(1, 0, 0)
ctx.set_font_size(12)
ctx.select_font_face(font, normal, bold)
s = "TAPE:"
ctx.move_to(900 - (ctx.text_extents(s)[2] / 2), 15)
ctx.show_text(s)
ctx.stroke()

# Tape value (canvas inverted)
ctx.arc(900, 70, 42, 0, 2 * 3.14)
ctx.set_source_rgb(0.5, 0, 0)
if controls['tape'] == 127:
    ctx.set_source_rgb(0.2, 0, 0)
ctx.fill()
ctx.stroke()

# Tape canvas (value inverted)
ctx.move_to(900, 70)
ctx.arc(900, 70, 42, 3.14 / 2, 3.14 / 2 + 360 * (controls['tape'] / 127) * (3.14 / 180))
ctx.close_path()
ctx.set_source_rgb(0.02, 0.02, 0.02)
ctx.fill()
ctx.stroke()

# Tape frame
ctx.arc(900, 70, 40, 0, 2 * 3.14)
if controls['tape'] == 127:
    ctx.set_source_rgb(0.032, 0.032, 0.032)
else:
    ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(10)
ctx.stroke()

# Tape indicator
ctx.arc(900, 70, 42, pos1, pos2)
ctx.line_to(900, 70)
ctx.fill()
if controls['tape'] == 127:
    ctx.set_source_rgb(0.032, 0.032, 0.032)
else:
    ctx.set_source_rgb(1, 0.5, 0.5)
ctx.arc(900, 70, 40, pos1, pos2)
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
