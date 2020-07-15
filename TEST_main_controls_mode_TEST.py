import cairo
import push2_python
import numpy

import definitions

SETTINGS_BUTTON = push2_python.constants.BUTTON_SETUP

controls = {'instrument': 0, 'instrument_filter': 127, 'master_filter': 127, 'fx': 127, 'smile': 0, 'reverb': 0, 'tape': 127 }

max_encoder_value = 127

# class MainControlsMode(definitions.PyshaMode):

    # # def generate_display_frame():
    # def update_display(self, ctx, w, h):

w, h = push2_python.constants.DISPLAY_LINE_PIXELS, push2_python.constants.DISPLAY_N_LINES
surface = cairo.ImageSurface(cairo.FORMAT_RGB16_565, w, h)
ctx = cairo.Context(surface)

####################################################################################
# Initial black rectangle
ctx.rectangle(0, 0, w, h)
ctx.set_source_rgb(0, 0, 0)
ctx.fill()

font = "Verdana"
normal = cairo.FONT_SLANT_NORMAL
bold = cairo.FONT_WEIGHT_BOLD

####################################################################################
# INSTRUMENT_SELECTION
# Instrument title
ctx.set_font_size(12)
ctx.select_font_face(font, normal, bold)
s = "INSTRUMENT:"
[xbearing, ybearing, width, height, dx, dy] = ctx.text_extents(s)
ctx.move_to(60 - (width / 2), 15)
# Piano
if controls['instrument'] <= 41: ctx.set_source_rgb(1, 0.25, 0.5)
# Synth
if controls['instrument'] >= 42 and controls['instrument'] <= 81: ctx.set_source_rgb(0, 1, 0.7)
# Sampler
if controls['instrument'] >= 82: ctx.set_source_rgb(0.75, 0, 1)
ctx.show_text(s)

# Instrument canvas
ctx.rectangle(15, 23 + (30 * (controls['instrument'] / 127)), 90, 15)
# Piano
if controls['instrument'] <= 41: ctx.set_source_rgb(1, 0.25, 0.5)
# Synth
if controls['instrument'] >= 42 and controls['instrument'] <= 81: ctx.set_source_rgb(0, 0.9, 0.6)
# Sampler
if controls['instrument'] >= 82: ctx.set_source_rgb(0.75, 0, 1)
ctx.fill()
ctx.stroke()

# Instruments list
ctx.set_source_rgb(1, 1, 1)
ctx.set_font_size(12)
ctx.select_font_face(font, cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_NORMAL)

# Piano
s = "PIANO"
[xbearing, ybearing, width, height, dx, dy] = ctx.text_extents(s)
ctx.move_to(60 - (width / 2), 35)
ctx.show_text(s)

# Synth
s = "SYNTH"
[xbearing, ybearing, width, height, dx, dy] = ctx.text_extents(s)
ctx.move_to(60 - (width / 2), 50)
ctx.show_text(s)

# Sampler
s = "SAMPLER"
[xbearing, ybearing, width, height, dx, dy] = ctx.text_extents(s)
ctx.move_to(60 - (width / 2), 65)
ctx.show_text(s)

####################################################################################
# INSTRUMENT_FILTER

# Instrument_filter title
# Piano
if controls['instrument'] <= 41: ctx.set_source_rgb(1, 0.25, 0.5)
# Synth
if controls['instrument'] >= 42 and controls['instrument'] <= 81: ctx.set_source_rgb(0, 1, 0.7)
# Sampler
if controls['instrument'] >= 82: ctx.set_source_rgb(0.75, 0, 1)

ctx.set_font_size(12)
ctx.select_font_face(font, normal, bold)
s = "INSTRUMENT LPF:"
[xbearing, ybearing, width, height, dx, dy] = ctx.text_extents(s)
ctx.move_to(180 - (width / 2), 15)
ctx.show_text(s)

# Instrument_filter value (canvas - inverted)
ctx.arc(180, 70, 42, 0, 2 * 3.14)
# Piano
if controls['instrument'] <= 41:
    ctx.set_source_rgb(1, 0.5, 0.75)
    if controls['instrument_filter'] == 127:
        ctx.set_source_rgb(0.1, 0.025, 0.05)
# Synth
if controls['instrument'] >= 42 and controls['instrument'] <= 81:
        ctx.set_source_rgb(0.5, 1, 0.95)
        if controls['instrument_filter'] == 127:
            ctx.set_source_rgb(0, 0.1, 0.07)
# Sampler
if controls['instrument'] >= 82:
    ctx.set_source_rgb(0.9, 0.25, 1)
    if controls['instrument_filter'] == 127:
        ctx.set_source_rgb(0.075, 0, 0.075)
ctx.fill()
ctx.stroke()

# Instrument_filter canvas (value - inverted)
ctx.move_to(180, 75)
ctx.arc(180, 70, 42, 3.14 / 2, 3.14 / 2 + 360 * (controls['instrument_filter'] / 127) * (3.14 / 180))
ctx.close_path()
ctx.set_source_rgb(0.02, 0.02, 0.02)
ctx.fill()
ctx.stroke()

# Instrument_filter frame
ctx.arc(180, 70, 42, 0, 2 * 3.14)
if controls['instrument_filter'] == 127:
    ctx.set_source_rgb(0.032, 0.032, 0.032)
else:
    # Piano
    if controls['instrument'] <= 41:
        ctx.set_source_rgb(1, 0.25, 0.5)
    # Synth
    if controls['instrument'] >= 42 and controls['instrument'] <= 81:
            ctx.set_source_rgb(0.05, 0.9, 0.7)
    # Sampler
    if controls['instrument'] >= 82:
        ctx.set_source_rgb(0.75, 0, 1)

ctx.set_line_width(5)
ctx.stroke()

####################################################################################
# MASTER_FILTER

# Master_filter title
ctx.set_source_rgb(1, 0.5, 0.1)
ctx.set_font_size(12)
ctx.select_font_face(font, normal, bold)
s = "MASTER LPF:"
[xbearing, ybearing, width, height, dx, dy] = ctx.text_extents(s)
ctx.move_to(420 - (width / 2), 15)
ctx.show_text(s)
ctx.stroke()

# Master_filter value (canvas - inverted)
ctx.arc(420, 70, 42, 0, 2 * 3.14)
ctx.set_source_rgb(1, 0.75, 0.3)
if controls['master_filter'] == 127:
    ctx.set_source_rgb(0.1, 0.05, 0.01)
ctx.fill()
ctx.stroke()

# Master_filter canvas (value - inverted)
ctx.move_to(420, 75)
ctx.arc(420, 70, 42, 3.14 / 2, 3.14 / 2 + 360 * (controls['master_filter'] / 127) * (3.14 / 180))
ctx.close_path()
ctx.set_source_rgb(0.02, 0.02, 0.02)
ctx.fill()
ctx.stroke()

# Master_filter frame
ctx.arc(420, 70, 42, 0, 2 * 3.14)
if controls['master_filter'] == 127:
    ctx.set_source_rgb(0.032, 0.032, 0.032)
else:
    ctx.set_source_rgb(1, 0.5, 0.1)
ctx.set_line_width(5)
ctx.stroke()

####################################################################################
# FX MIX
# FX mix title
ctx.set_source_rgb(0.75, 0, 1)
ctx.set_font_size(12)
ctx.select_font_face(font, normal, bold)
s = "FX MIX:"
[xbearing, ybearing, width, height, dx, dy] = ctx.text_extents(s)
ctx.move_to(540 - (width / 2), 15)
ctx.show_text(s)
ctx.stroke()

# FX value (canvas inverted)
ctx.arc(540, 70, 42, 0, 2 * 3.14)
ctx.set_source_rgb(1, 0.5, 1)
if controls['fx'] == 127:
    ctx.set_source_rgb(0.075, 0, 0.075)
ctx.fill()
ctx.stroke()

# FX canvas (value inverted)
ctx.move_to(540, 75)
ctx.arc(540, 70, 42, 3.14 / 2, 3.14 / 2 + 360 * (controls['fx'] / 127) * (3.14 / 180))
ctx.close_path()
ctx.set_source_rgb(0.02, 0.02, 0.02)
ctx.fill()
ctx.stroke()

# FX frame
ctx.arc(540, 70, 42, 0, 2 * 3.14)
if controls['fx'] == 127:
    ctx.set_source_rgb(0.032, 0.032, 0.032)
else:
    ctx.set_source_rgb(0.75, 0, 1)
ctx.set_line_width(5)
ctx.stroke()

####################################################################################
# SMILE
# Smile title
ctx.set_source_rgb(1, 1, 0)
ctx.set_font_size(12)
ctx.select_font_face(font, normal, bold)
s = "SMILE:"
[xbearing, ybearing, width, height, dx, dy] = ctx.text_extents(s)
ctx.move_to(660 - (width / 2), 15)
ctx.show_text(s)
ctx.stroke()

# Smile canvas
ctx.arc(660, 70, 42, 0, 2 * 3.14)
ctx.set_source_rgb(0.02, 0.02, 0.02)
if controls['smile'] == 127:
    ctx.set_source_rgb(1, 1, 0.5)
ctx.fill()
ctx.stroke()

# Smile value
ctx.move_to(660, 75)
ctx.arc(660, 70, 42, 3.14 / 2, 3.14 / 2 + 360 * (controls['smile'] / 127) * (3.14 / 180))
ctx.close_path()
ctx.set_source_rgb(1, 1, 0.5)
ctx.fill()
ctx.stroke()

# Smile frame
ctx.arc(660, 70, 42, 0, 2 * 3.14)
if controls['smile'] == 0:
    ctx.set_source_rgb(0.032, 0.032, 0.032)
else:
    ctx.set_source_rgb(1, 1, 0)
ctx.set_line_width(5)
ctx.stroke()

####################################################################################
########## REVERB
# Reverb title
ctx.set_source_rgb(0, 1, 1)
ctx.set_font_size(12)
ctx.select_font_face(font, normal, bold)
s = "REVERB:"
[xbearing, ybearing, width, height, dx, dy] = ctx.text_extents(s)
ctx.move_to(780 - (width / 2), 15)
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
ctx.move_to(780, 75)
ctx.arc(780, 70, 42, 3.14 / 2, 3.14 / 2 + 360 * (controls['reverb'] / 127) * (3.14 / 180))
ctx.close_path()
ctx.set_source_rgb(0.5, 1, 1)
ctx.fill()
ctx.stroke()

# Reverb frame
ctx.arc(780, 70, 42, 0, 2 * 3.14)
if controls['reverb'] == 0:
    ctx.set_source_rgb(0.032, 0.032, 0.032)
else:
    ctx.set_source_rgb(0, 0.75, 1)
ctx.set_line_width(5)
ctx.stroke()

####################################################################################
########## TAPE
# Tape title
ctx.set_source_rgb(1, 0, 0)
ctx.set_font_size(12)
ctx.select_font_face(font, normal, bold)
s = "TAPE:"
[xbearing, ybearing, width, height, dx, dy] = ctx.text_extents(s)
ctx.move_to(900 - (width / 2), 15)
ctx.show_text(s)
ctx.stroke()

# Tape value (canvas inverted)
ctx.arc(900, 70, 42, 0, 2 * 3.14)
ctx.set_source_rgb(1, 0.5, 0.5)
if controls['tape'] == 127:
    ctx.set_source_rgb(0.2, 0, 0)
ctx.fill()
ctx.stroke()

# Tape canvas (value inverted)
ctx.move_to(900, 75)
ctx.arc(900, 70, 42, 3.14 / 2, 3.14 / 2 + 360 * (controls['tape'] / 127) * (3.14 / 180))
ctx.close_path()
ctx.set_source_rgb(0.02, 0.02, 0.02)
ctx.fill()
ctx.stroke()

# Tape frame
ctx.arc(900, 70, 42, 0, 2 * 3.14)
if controls['tape'] == 127:
    ctx.set_source_rgb(0.032, 0.032, 0.032)
else:
    ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(5)
ctx.stroke()

####################################################################################
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
# RELEASED
# ctx.move_to(300, 145)
# ctx.line_to(290, 135)
# ctx.line_to(310, 135)
# ctx.close_path()
# ctx.line_to(300, 155)
# ctx.move_to(295, 155)
# ctx.line_to(305, 155)
#
# ctx.set_source_rgb(1, 1, 0)
# ctx.set_line_width(2.5)
# ctx.stroke()

# PUSHED
# ctx.move_to(240, 130)
# ctx.line_to(360, 130)
# ctx.line_to(360, 160)
# ctx.line_to(240, 160)
# ctx.close_path()
# ctx.set_source_rgb(1, 1, 0)
# ctx.fill()
#
# ctx.move_to(300, 145)
# ctx.line_to(290, 135)
# ctx.line_to(310, 135)
# ctx.close_path()
# ctx.line_to(300, 155)
# ctx.move_to(295, 155)
# ctx.line_to(305, 155)
#
# ctx.set_source_rgb(0, 0, 0)
# ctx.set_line_width(2.5)
# ctx.stroke()


# BAR 2
ctx.move_to(420, 145)
ctx.line_to(410, 135)
ctx.line_to(430, 135)
ctx.close_path()
ctx.line_to(420, 155)
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
# RELEASED
# ctx.move_to(660, 140)
# ctx.curve_to(660, 130, 675, 130, 670, 142)
# ctx.curve_to(670, 143, 662, 152, 660, 155)
# ctx.curve_to(658, 152, 650, 143, 650, 142)
# ctx.curve_to(645, 130, 660, 130, 660, 140)
# ctx.close_path()
#
# ctx.set_line_cap(cairo.LINE_CAP_ROUND)
# ctx.set_source_rgb(1, 0.4, 0)
# ctx.set_line_width(2.5)
# ctx.stroke()

# PUSHED
ctx.move_to(600, 130)
ctx.line_to(720, 130)
ctx.line_to(720, 160)
ctx.line_to(600, 160)
ctx.set_source_rgb(1, 0.4, 0)
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

####################################################################################
# End of drawing code
buf = surface.get_data()
frame = numpy.ndarray(shape=(h, w), dtype=numpy.uint16, buffer=buf).transpose()
# self.push.display.display_frame(frame, input_format=push2_python.constants.FRAME_FORMAT_RGB565)

surface.write_to_png('screenshot_2.png')
