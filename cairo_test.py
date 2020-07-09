
import time

import cairo
import mido
import numpy
import push2_python

import definitions

push = push2_python.Push2()

# Init dictionary to store the state of encoders
controls = {'instrument': 0, 'filter': 127, 'smile': 0, 'reverb': 0, 'tape': 127 }

max_encoder_value = 127

push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_1, definitions.PINK)
push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_2, definitions.ORANGE)
push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_6, definitions.YELLOW)
push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_7, definitions.CYAN)
push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_8, definitions.RED)

push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_1, definitions.WHITE)
push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_2, definitions.WHITE)
push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_3, definitions.YELLOW)
push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_4, definitions.YELLOW)
push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_5, definitions.ORANGE)
push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_6, definitions.ORANGE)
push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_7, definitions.PINK)
push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_8, definitions.PINK)

def generate_display_frame():

    # Prepare cairo canvas
    w, h = push2_python.constants.DISPLAY_LINE_PIXELS, push2_python.constants.DISPLAY_N_LINES
    surface = cairo.ImageSurface(cairo.FORMAT_RGB16_565, w, h)
    ctx = cairo.Context(surface)

    # Initial black rectangle
    ctx.rectangle(0, 0, w, h)
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill()

    font = "Verdana"
    normal = cairo.FONT_SLANT_NORMAL
    medium = cairo.FONT_SLANT_NORMAL
    bold = cairo.FONT_WEIGHT_BOLD
    italic = cairo.FONT_SLANT_ITALIC

    ####################################################################################
    # INSTRUMENT
    if controls['instrument'] <= 41:
        ctx.set_source_rgb(1, 0.25, 0.5)
        ctx.rectangle(15, 23, 90, 15)
        ctx.fill()
        ctx.stroke()

    if controls['instrument'] >= 42:
        if controls['instrument'] <= 81:
            ctx.set_source_rgb(0, 1, 0.7)
            ctx.rectangle(15, 38, 90, 15)
            ctx.fill()
            ctx.stroke()

    if controls['instrument'] >= 82:
        ctx.set_source_rgb(0.75, 0, 1)
        ctx.rectangle(15, 53, 90, 15)
        ctx.fill()
        ctx.stroke()

    ctx.set_font_size(12)
    ctx.select_font_face(font, normal, bold)
    s = "INSTRUMENT:"
    [xbearing, ybearing, width, height, dx, dy] = ctx.text_extents(s)
    ctx.move_to(60 - (width / 2), 15)
    ctx.show_text(s)

    ########## Instruments
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(12)
    ctx.select_font_face(font, cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_NORMAL)
    s = "PIANO"
    [xbearing, ybearing, width, height, dx, dy] = ctx.text_extents(s)
    ctx.move_to(60 - (width / 2), 35)
    ctx.show_text(s)

    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(12)
    ctx.select_font_face(font, cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_NORMAL)
    s = "SYNTH"
    [xbearing, ybearing, width, height, dx, dy] = ctx.text_extents(s)
    ctx.move_to(60 - (width / 2), 50)
    ctx.show_text(s)

    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(12)
    ctx.select_font_face(font, cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_NORMAL)
    s = "SAMPLER"
    [xbearing, ybearing, width, height, dx, dy] = ctx.text_extents(s)
    ctx.move_to(60 - (width / 2), 65)
    ctx.show_text(s)

    ####################################################################################
    # FILTER

    # Filter text:
    ctx.set_source_rgb(1, 0.5, 0.1)
    ctx.set_font_size(12)
    ctx.select_font_face(font, normal, bold)
    s = "FILTER:"
    [xbearing, ybearing, width, height, dx, dy] = ctx.text_extents(s)
    ctx.move_to(180 - (width / 2), 15)
    ctx.show_text(s)

    # Filt_value = 64
    Filt_min = 120
    Filt_max = 360

    # Filter "canvas"
    ctx.rectangle(120, 25, 254, 90)
    ctx.set_source_rgb(0.1, 0.05, 0.01)
    ctx.fill()

    filter_frequency = (controls['filter'] * 2) + 120

    ctx.move_to(filter_frequency, 25)
    ctx.line_to(filter_frequency, 115)
    ctx.line_to(374, 115)
    ctx.line_to(374, 25)
    ctx.close_path()
    ctx.set_source_rgb(1, 0.5, 0.1)
    ctx.fill()

    # Filter "frame":
    ctx.rectangle(120, 25, 254, 90)
    if controls['filter'] == 127:
        ctx.set_source_rgb(0.2, 0.1, 0.02)
    else:
        ctx.set_source_rgb(1, 0.5, 0.1)
    ctx.set_line_width(5)
    ctx.stroke()

    ####################################################################################
    # SMILE

    # Smile Text
    ctx.set_source_rgb(1, 1, 0)
    ctx.set_font_size(12)
    ctx.select_font_face(font, normal, bold)
    s = "SMILE:"
    [xbearing, ybearing, width, height, dx, dy] = ctx.text_extents(s)
    ctx.move_to(660 - (width / 2), 15)
    ctx.show_text(s)
    ctx.stroke()

    # # Reverb value text
    # if reverb_value == 0:
    #     ctx.set_source_rgb(0, 0.2, 0.2)
    # else:
    #     ctx.set_source_rgb(0, 1, 1)
    # ctx.set_font_size(12)
    # ctx.select_font_face(font, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    # [xbearing, ybearing, width, height, dx, dy] = ctx.text_extents(str(reverb_value))
    # ctx.move_to(780 - (width / 2), 35)
    # ctx.show_text(str(reverb_value))

    # Smile canvas
    # ctx.arc(xc, yc, radius, start_rad, end_rad)
    ctx.arc(660, 70, 42, 0, 2 * 3.14)
    ctx.set_source_rgb(0.1, 0.1, 0)
    ctx.fill()
    ctx.stroke()

    # Smile value
    # ctx.arc(660, 75, 30, 1.6*math.pi, 360 * (smile_value / 127) * (math.pi / 180))
    ctx.move_to(660, 75)
    ctx.arc(660, 70, 42, 3.14 / 2, 3.14 / 2 + 360 * (controls['smile'] / 127) * (3.14 / 180))
    ctx.close_path()
    ctx.set_source_rgb(1, 1, 0.5)
    ctx.fill()
    ctx.stroke()

    # Smile frame
    ctx.arc(660, 70, 42, 0, 2 * 3.14)
    if controls['smile'] == 0:
        ctx.set_source_rgb(0.2, 0.2, 0)
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
    ctx.set_source_rgb(0, 0.1, 0.1)
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
        ctx.set_source_rgb(0, 0.2, 0.2)
    else:
        ctx.set_source_rgb(0, 0.75, 1)
    ctx.set_line_width(5)
    ctx.stroke()

    ####################################################################################
    ########## TAPE

    ctx.set_source_rgb(1, 0, 0)
    ctx.set_font_size(12)
    ctx.select_font_face(font, normal, bold)
    s = "TAPE:"
    [xbearing, ybearing, width, height, dx, dy] = ctx.text_extents(s)
    ctx.move_to(900 - (width / 2), 15)
    ctx.show_text(s)
    ctx.stroke()

    # Tape canvas
    ctx.arc(900, 70, 42, 0, 2 * 3.14)
    ctx.set_source_rgb(1, 0.5, 0.5)
    ctx.fill()
    ctx.stroke()

    # Tape value
    ctx.move_to(900, 75)
    ctx.arc(900, 70, 42, 3.14 / 2, 3.14 / 2 + 360 * (controls['tape'] / 127) * (3.14 / 180))
    ctx.close_path()
    ctx.set_source_rgb(0.1, 0, 0)
    ctx.fill()
    ctx.stroke()

    # Tape frame
    ctx.arc(900, 70, 42, 0, 2 * 3.14)
    if controls['tape'] == 127:
        ctx.set_source_rgb(0.2, 0, 0)
    else:
        ctx.set_source_rgb(1, 0, 0)
    ctx.set_line_width(5)
    ctx.stroke()

    ####################################################################################
    # FLAGGA 1
    ctx.move_to(50, 135)
    ctx.curve_to(60, 130, 60, 140, 70, 135)
    ctx.line_to(70, 145)
    ctx.curve_to(60, 150, 60, 140, 50, 145)
    ctx.close_path()
    ctx.move_to(50, 135)
    ctx.line_to(50, 155)

    # FLAGGA 2
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

    # COCKTAIL 1
    ctx.move_to(300, 145)
    ctx.line_to(300, 155)

    ctx.move_to(290, 135)
    ctx.line_to(310, 135)
    ctx.line_to(300, 145)
    ctx.close_path()

    ctx.move_to(295, 155)
    ctx.line_to(305, 155)

    # COCKTAIL 2
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

    # HJÄRTA 1
    ctx.move_to(540, 140)
    ctx.curve_to(540, 130, 555, 130, 550, 142)
    ctx.curve_to(550, 143, 542, 152, 540, 155)

    ctx.move_to(540, 140)
    ctx.curve_to(540, 130, 525, 130, 530, 142)
    ctx.curve_to(530, 143, 538, 152, 540, 155)

    # HJÄRTA 2
    ctx.move_to(660, 140)
    ctx.curve_to(660, 130, 675, 130, 670, 142)
    ctx.curve_to(670, 143, 662, 152, 660, 155)
    ctx.line_to(660, 155)

    ctx.move_to(660, 140)
    ctx.curve_to(660, 130, 645, 130, 650, 142)
    ctx.curve_to(650, 143, 658, 152, 660, 155)

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

    ####################################################################################
    # End of drawing code
    # surface.write_to_png('line3.png')

    # Turn canvas into numpy array compatible with push.display.display_frame method
    buf = surface.get_data()
    frame = numpy.ndarray(shape=(h, w), dtype=numpy.uint16, buffer=buf)
    frame = frame.transpose()
    return frame

####################################################################################
####################################################################################
####################################################################################
# ENCODERS

@push2_python.on_encoder_rotated(push2_python.constants.ENCODER_TRACK1_ENCODER)
def on_encoder_rotated(push, increment):
    def update_encoder_value(increment):
        updated_value = int(controls['instrument'] + increment)
        if updated_value < 0: controls['instrument'] = 0
        elif updated_value > max_encoder_value: controls['instrument'] = max_encoder_value
        else: controls['instrument'] = updated_value

    update_encoder_value(increment)

    if controls['instrument'] <= 41:
        definitions.ROOT_KEY = definitions.PINK
        app.set_melodic_mode()
        app.pads_need_update = True
        self.update_pads()

    if controls['instrument'] >= 42:
        if controls['instrument'] <= 81:
            definitions.ROOT_KEY = definitions.GREEN
            app.set_melodic_mode()
            app.pads_need_update = True
            self.update_pads()

    if controls['instrument'] >= 82:
        definitions.ROOT_KEY = definitions.PURPLE
        app.set_rhythmic_mode()
        app.pads_need_update = True
        self.update_pads()


@push2_python.on_encoder_rotated(push2_python.constants.ENCODER_TRACK2_ENCODER)
def on_encoder_rotated(push, increment):
    def update_encoder_value(increment):
        updated_filter_value = int(controls['filter'] + increment)
        if updated_filter_value < 0: controls['filter'] = 0
        elif updated_filter_value > max_encoder_value: controls['filter'] = max_encoder_value
        else: controls['filter'] = updated_filter_value
    update_encoder_value(increment)

@push2_python.on_encoder_rotated(push2_python.constants.ENCODER_TRACK6_ENCODER)
def on_encoder_rotated(push, increment):
    def update_encoder_value(increment):
        updated_value = int(controls['smile'] + increment)
        if updated_value < 0: controls['smile'] = 0
        elif updated_value > max_encoder_value: controls['smile'] = max_encoder_value
        else: controls['smile'] = updated_value
    update_encoder_value(increment)

@push2_python.on_encoder_rotated(push2_python.constants.ENCODER_TRACK7_ENCODER)
def on_encoder_rotated(push, increment):
    def update_encoder_value(increment):
        updated_value = int(controls['reverb'] + increment)
        if updated_value < 0: controls['reverb'] = 0
        elif updated_value > max_encoder_value: controls['reverb'] = max_encoder_value
        else: controls['reverb'] = updated_value
    update_encoder_value(increment)

@push2_python.on_encoder_rotated(push2_python.constants.ENCODER_TRACK8_ENCODER)
def on_encoder_rotated(push, increment):
    def update_encoder_value(increment):
        updated_value = int(controls['tape'] + increment)
        if updated_value < 0: controls['tape'] = 0
        elif updated_value > max_encoder_value: controls['tape'] = max_encoder_value
        else: controls['tape'] = updated_value
    update_encoder_value(increment)

####################################################################################
####################################################################################
####################################################################################
# BUTTONS

#####################################
# Upper row 1
@push2_python.on_button_pressed(push2_python.constants.BUTTON_UPPER_ROW_1)
def on_button_pressed(push):
    push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_1, definitions.WHITE)

@push2_python.on_button_released(push2_python.constants.BUTTON_UPPER_ROW_1)
def on_button_released(push):
    push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_1, definitions.PINK)

#####################################
# Upper row 2
@push2_python.on_button_pressed(push2_python.constants.BUTTON_UPPER_ROW_2)
def on_button_pressed(push):
    push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_2, definitions.WHITE)

@push2_python.on_button_released(push2_python.constants.BUTTON_UPPER_ROW_2)
def on_button_released(push):
    controls['filter'] = 127
    mido.Message('control_change', control=22, value=127)
    push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_2, definitions.ORANGE)

#####################################
# Upper row 6
@push2_python.on_button_pressed(push2_python.constants.BUTTON_UPPER_ROW_6)
def on_button_pressed(push):
    push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_6, definitions.WHITE)
@push2_python.on_button_released(push2_python.constants.BUTTON_UPPER_ROW_6)
def on_button_released(push):
    controls['smile'] = 0
    mido.Message('control_change', control=26, value=0)
    push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_6, definitions.YELLOW)

#####################################
# Upper row 7
@push2_python.on_button_pressed(push2_python.constants.BUTTON_UPPER_ROW_7)
def on_button_pressed(push):
    push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_7, definitions.WHITE)
@push2_python.on_button_released(push2_python.constants.BUTTON_UPPER_ROW_7)
def on_button_released(push):
    controls['reverb'] = 0
    mido.Message('control_change', control=27, value=0)
    push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_7, definitions.CYAN)

#####################################
# Upper row 8
@push2_python.on_button_pressed(push2_python.constants.BUTTON_UPPER_ROW_8)
def on_button_pressed(push):
    push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_8, definitions.WHITE)
@push2_python.on_button_released(push2_python.constants.BUTTON_UPPER_ROW_8)
def on_button_released(push):
    controls['tape'] = 127
    mido.Message('control_change', control=28, value=127)
    push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_8, definitions.RED)

#####################################
#####################################
#####################################
# Lower row 1
@push2_python.on_button_pressed(push2_python.constants.BUTTON_LOWER_ROW_1)
def on_button_pressed(push):
    mido.Message('control_change', control=101, value=127)
    push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_1, definitions.WHITE)
@push2_python.on_button_released(push2_python.constants.BUTTON_LOWER_ROW_1)
def on_button_released(push):
    mido.Message('control_change', control=101, value=0)
    push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_1, definitions.WHITE)

#####################################
# Lower row 2
@push2_python.on_button_pressed(push2_python.constants.BUTTON_LOWER_ROW_2)
def on_button_pressed(push):
    mido.Message('control_change', control=102, value=127)
    push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_2, definitions.WHITE)
@push2_python.on_button_released(push2_python.constants.BUTTON_LOWER_ROW_2)
def on_button_released(push):
    mido.Message('control_change', control=102, value=0)
    push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_2, definitions.WHITE)

#####################################
# Lower row 3
@push2_python.on_button_pressed(push2_python.constants.BUTTON_LOWER_ROW_3)
def on_button_pressed(push):
    mido.Message('control_change', control=103, value=127)
    push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_3, definitions.WHITE)
@push2_python.on_button_released(push2_python.constants.BUTTON_LOWER_ROW_3)
def on_button_released(push):
    mido.Message('control_change', control=103, value=0)
    push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_3, definitions.YELLOW)

#####################################
# Lower row 4
@push2_python.on_button_pressed(push2_python.constants.BUTTON_LOWER_ROW_4)
def on_button_pressed(push):
    mido.Message('control_change', control=104, value=127)
    push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_4, definitions.WHITE)
@push2_python.on_button_released(push2_python.constants.BUTTON_LOWER_ROW_4)
def on_button_released(push):
    mido.Message('control_change', control=104, value=0)
    push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_4, definitions.YELLOW)

#####################################
# Lower row 5
@push2_python.on_button_pressed(push2_python.constants.BUTTON_LOWER_ROW_5)
def on_button_pressed(push):
    mido.Message('control_change', control=105, value=127)
    push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_5, definitions.WHITE)
@push2_python.on_button_released(push2_python.constants.BUTTON_LOWER_ROW_5)
def on_button_released(push):
    mido.Message('control_change', control=105, value=0)
    push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_5, definitions.ORANGE)

#####################################
# Lower row 6
@push2_python.on_button_pressed(push2_python.constants.BUTTON_LOWER_ROW_6)
def on_button_pressed(push):
    mido.Message('control_change', control=106, value=127)
    push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_6, definitions.WHITE)
@push2_python.on_button_released(push2_python.constants.BUTTON_LOWER_ROW_6)
def on_button_released(push):
    mido.Message('control_change', control=106, value=0)
    push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_6, definitions.ORANGE)

#####################################
# Lower row 7
@push2_python.on_button_pressed(push2_python.constants.BUTTON_LOWER_ROW_7)
def on_button_pressed(push):
    mido.Message('control_change', control=107, value=127)
    push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_7, definitions.WHITE)
@push2_python.on_button_released(push2_python.constants.BUTTON_LOWER_ROW_7)
def on_button_released(push):
    mido.Message('control_change', control=107, value=0)
    push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_7, definitions.PINK)

#####################################
# Lower row 8
@push2_python.on_button_pressed(push2_python.constants.BUTTON_LOWER_ROW_8)
def on_button_pressed(push):
    mido.Message('control_change', control=108, value=127)
    push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_8, definitions.WHITE)
@push2_python.on_button_released(push2_python.constants.BUTTON_LOWER_ROW_8)
def on_button_released(push):
    mido.Message('control_change', control=108, value=0)
    push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_8, definitions.PINK)

####################################################################################
####################################################################################
####################################################################################

# Draw method that will generate the frame to be shown on the display
def draw():
    frame = generate_display_frame()
    push.display.display_frame(frame, input_format=push2_python.constants.FRAME_FORMAT_RGB565)

# Now start infinite loop so the app keeps running
print('App runnnig...')
while True:
    draw()
    time.sleep(1.0/30)  # Sart drawing loop, aim at ~30fps