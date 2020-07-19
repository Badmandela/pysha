import cairo
import mido
import push2_python

import definitions

SETTINGS_BUTTON = push2_python.constants.BUTTON_SETUP

controls = {'instr': 0, 'instr_lpf': 127, 'master_lpf': 127, 'fx': 127, 'smile': 0, 'reverb': 0, 'tape': 127}
transport = {'cue1': 0, 'cue2': 0, 'bar1': 0, 'bar2': 0, 'beat1': 0, 'beat2': 0, 'nudge1': 0, 'nudge2': 0}

max_encoder_value = 127
piano_max = 31
synth_min = 32
synth_max = 95
sampler_min = 96


class MainControlsMode(definitions.PyshaMode):

    def activate(self):
        self.update_buttons()

    def deactivate(self):
        self.push.buttons.set_button_color(SETTINGS_BUTTON, definitions.BLACK)

    # def generate_display_frame():
    def update_display(self, ctx, w, h):

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
        center_y = 75

        # Textfont
        ctx.set_font_size(12)
        ctx.select_font_face("Verdana", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)

        # Instrument QUASI-GLOBALS
        title = "INSTRUMENT:"
        control = controls['instr']
        if controls['instr'] <= piano_max:
            color = [1, 0.25, 0.5]
        elif synth_min <= controls['instr'] <= synth_max:
            color = [0.1, 1, 0.7]
        else:  # controls['instr'] >= sampler_min
            color = [1, 0.1, 0.9]
        color_dark = [divide / 2 for divide in color]
        color_light = [1, 1, 1]
        center_x = 60

        title = "INSTRUMENT:"
        ctx.move_to(center_x - (ctx.text_extents(title)[2] / 2), 15)
        ctx.set_source_rgb(*color)
        ctx.show_text(title)

        # Instrument canvas
        ctx.rectangle(15, 23 + (30 * (controls['instr'] / 127)), 90, 15)
        ctx.set_source_rgb(*color)
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

        # Instrument_filter QUASI-GLOBALS
        title = "INSTRUMENT LPF:"
        control = controls['instr_lpf']

        if controls['instr'] <= piano_max:
            color = [1, 0.25, 0.5]
        elif synth_min <= controls['instr'] <= synth_max:
            color = [0.1, 1, 0.7]
        elif controls['instr'] >= sampler_min:
            color = [1, 0.1, 0.9]
        color_dark = [divide / 2 for divide in color]
        color_light = [1, 1, 1]
        center_x = 180

        # Instrument_filter title
        ctx.set_source_rgb(*color)
        s = "INSTRUMENT LPF:"
        ctx.move_to(center_x - (ctx.text_extents(s)[2] / 2), 15)
        ctx.show_text(s)

        # Instrument_filter value (canvas - inverted)
        ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
        ctx.set_source_rgb(*color_dark)
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
        ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
        if control == 127:
            ctx.set_source_rgb(*screen_dark)
        else:
            pat = cairo.MeshPattern()
            pat.begin_patch()
            pat.move_to(center_x, center_y - 50)
            pat.line_to(center_x - 60, center_y - 50)
            pat.line_to(center_x - 60, center_y + 50)
            pat.line_to(center_x + 200, center_y + 200)
            pat.set_corner_color_rgb(0, *color)
            pat.set_corner_color_rgb(1, *color)
            pat.set_corner_color_rgb(2, *color)
            pat.set_corner_color_rgb(3, *color_light)
            pat.end_patch()
            pat.begin_patch()
            pat.move_to(center_x, center_y + 500)
            pat.line_to(center_x + 60, center_y + 50)
            pat.line_to(center_x + 60, center_y - 50)
            pat.line_to(center_x, center_y - 50)
            pat.set_corner_color_rgb(0, *color_dark)
            pat.set_corner_color_rgb(1, *color)
            pat.set_corner_color_rgb(2, *color)
            pat.set_corner_color_rgb(3, *color)
            pat.end_patch()
            ctx.set_source(pat)

        ctx.set_line_width(10)
        ctx.stroke()

        # Instrument filter indicator
        pos1 = 3.14 / 2 + 360 * ((controls['instr_lpf'] - 5) / 127) * (3.14 / 180)
        pos2 = 3.14 / 2 + 360 * ((controls['instr_lpf'] + 5) / 127) * (3.14 / 180)

        # Instrument filter indicator inner
        if controls['instr_lpf'] == 127:
            ctx.set_source_rgb(*screen_dark)
        else:
            ctx.set_source_rgb(*color)
        ctx.arc(center_x, center_y, rad, pos1, pos2)
        ctx.line_to(center_x, center_y)
        ctx.fill()

        # Instrument filter indicator outer
        if controls['instr_lpf'] == 127:
            ctx.set_source_rgb(*screen_dark)
        else:
            ctx.set_source_rgb(*color_light)
        ctx.arc(center_x, center_y, rad, pos1, pos2)
        ctx.set_line_width(12)
        ctx.stroke()

        # Master filter QUASI-GLOBALS
        title = "MASTER LPF:"
        control = controls['master_lpf']
        color = [1, 0.5, 0.1]
        color_dark = [divide / 2 for divide in color]
        color_light = [1, 1, 1]
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
        ctx.set_source_rgb(*color_dark)
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
        ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
        if control == 127:
            ctx.set_source_rgb(*screen_dark)
        else:
            pat = cairo.MeshPattern()
            pat.begin_patch()
            pat.move_to(center_x, center_y - 50)
            pat.line_to(center_x - 60, center_y - 50)
            pat.line_to(center_x - 60, center_y + 50)
            pat.line_to(center_x + 200, center_y + 200)
            pat.set_corner_color_rgb(0, *color)
            pat.set_corner_color_rgb(1, *color)
            pat.set_corner_color_rgb(2, *color)
            pat.set_corner_color_rgb(3, *color_light)
            pat.end_patch()
            pat.begin_patch()
            pat.move_to(center_x, center_y + 500)
            pat.line_to(center_x + 60, center_y + 50)
            pat.line_to(center_x + 60, center_y - 50)
            pat.line_to(center_x, center_y - 50)
            pat.set_corner_color_rgb(0, *color_dark)
            pat.set_corner_color_rgb(1, *color)
            pat.set_corner_color_rgb(2, *color)
            pat.set_corner_color_rgb(3, *color)
            pat.end_patch()
            ctx.set_source(pat)
        ctx.set_line_width(10)
        ctx.stroke()

        # # Master filter indicator frame
        # ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        # if control == 127:
        #     ctx.set_source_rgb(*screen_dark)
        # else:
        #     ctx.set_source_rgb(*color_light)
        # ctx.move_to(center_x, center_y)
        # ctx.arc(center_x, center_y, 46, pos1, pos2)
        # ctx.line_to(center_x, center_y)
        # ctx.set_line_width(3)
        # ctx.stroke()
        # ctx.set_line_cap(cairo.LINE_CAP_BUTT)

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
            ctx.set_source_rgb(*color_light)
        ctx.arc(center_x, center_y, rad, pos1, pos2)
        ctx.set_line_width(12)
        ctx.stroke()

        # FX QUASI-GLOBALS
        title = "FX LVL:"
        control = controls['fx']
        color = [0.75, 0.1, 1]
        color_dark = [divide / 2 for divide in color]
        color_light = [1, 1, 1]
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
        ctx.set_source_rgb(*color_dark)
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
        ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
        if controls['fx'] == 127:
            ctx.set_source_rgb(*screen_dark)
        else:
            pat = cairo.MeshPattern()
            pat.begin_patch()
            pat.move_to(center_x, center_y - 50)
            pat.line_to(center_x - 60, center_y - 50)
            pat.line_to(center_x - 60, center_y + 50)
            pat.line_to(center_x + 200, center_y + 200)
            pat.set_corner_color_rgb(0, *color)
            pat.set_corner_color_rgb(1, *color)
            pat.set_corner_color_rgb(2, *color)
            pat.set_corner_color_rgb(3, *color_light)
            pat.end_patch()
            pat.begin_patch()
            pat.move_to(center_x, center_y + 500)
            pat.line_to(center_x + 60, center_y + 50)
            pat.line_to(center_x + 60, center_y - 50)
            pat.line_to(center_x, center_y - 50)
            pat.set_corner_color_rgb(0, *color_dark)
            pat.set_corner_color_rgb(1, *color)
            pat.set_corner_color_rgb(2, *color)
            pat.set_corner_color_rgb(3, *color)
            pat.end_patch()
            ctx.set_source(pat)
        ctx.set_line_width(10)
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
            ctx.set_source_rgb(*color_light)
        ctx.arc(center_x, center_y, rad, pos1, pos2)
        ctx.set_line_width(12)
        ctx.stroke()

        # Smile QUASI-GLOBALS
        title = "SMILE:"
        control = controls['smile']
        color = [1, 1, 0.1]
        color_dark = [divide / 2 for divide in color]
        color_light = [1, 1, 1]
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
        ctx.set_source_rgb(*color_dark)
        ctx.fill()
        ctx.stroke()

        # Smile frame
        ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
        if control == 0:
            ctx.set_source_rgb(*screen_dark)
        else:
            pat = cairo.MeshPattern()
            pat.begin_patch()
            pat.move_to(center_x, center_y - 50)
            pat.line_to(center_x - 60, center_y - 50)
            pat.line_to(center_x - 60, center_y + 50)
            pat.line_to(center_x + 200, center_y + 200)
            pat.set_corner_color_rgb(0, *color)
            pat.set_corner_color_rgb(1, *color)
            pat.set_corner_color_rgb(2, *color)
            pat.set_corner_color_rgb(3, *color_dark)
            pat.end_patch()
            pat.begin_patch()
            pat.move_to(center_x, center_y + 500)
            pat.line_to(center_x + 60, center_y + 50)
            pat.line_to(center_x + 60, center_y - 50)
            pat.line_to(center_x, center_y - 50)
            pat.set_corner_color_rgb(0, *color_light)
            pat.set_corner_color_rgb(1, *color)
            pat.set_corner_color_rgb(2, *color)
            pat.set_corner_color_rgb(3, *color)
            pat.end_patch()
            ctx.set_source(pat)
        ctx.set_line_width(10)
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
            ctx.set_source_rgb(*color_light)
        ctx.arc(center_x, center_y, rad, pos1, pos2)
        ctx.set_line_width(12)
        ctx.stroke()

        # Reverb QUASI-GLOBALS
        title = "REVERB:"
        control = controls['reverb']
        color = [0.1, 0.85, 1]
        color_dark = [divide / 2 for divide in color]
        color_light = [1, 1, 1]
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
        ctx.set_source_rgb(*color_dark)
        ctx.fill()
        ctx.stroke()

        # Reverb frame
        ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
        if controls['reverb'] == 0:
            ctx.set_source_rgb(*screen_dark)
        else:
            pat = cairo.MeshPattern()
            pat.begin_patch()
            pat.move_to(center_x, center_y - 50)
            pat.line_to(center_x - 60, center_y - 50)
            pat.line_to(center_x - 60, center_y + 50)
            pat.line_to(center_x + 200, center_y + 200)
            pat.set_corner_color_rgb(0, *color)
            pat.set_corner_color_rgb(1, *color)
            pat.set_corner_color_rgb(2, *color)
            pat.set_corner_color_rgb(3, *color_dark)
            pat.end_patch()
            pat.begin_patch()
            pat.move_to(center_x, center_y + 500)
            pat.line_to(center_x + 60, center_y + 50)
            pat.line_to(center_x + 60, center_y - 50)
            pat.line_to(center_x, center_y - 50)
            pat.set_corner_color_rgb(0, *color_light)
            pat.set_corner_color_rgb(1, *color)
            pat.set_corner_color_rgb(2, *color)
            pat.set_corner_color_rgb(3, *color)
            pat.end_patch()
            ctx.set_source(pat)
        ctx.set_line_width(10)
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
            ctx.set_source_rgb(*color_light)
        ctx.arc(center_x, center_y, rad, pos1, pos2)
        ctx.set_line_width(12)
        ctx.stroke()

        # Tape QUASI-GLOBALS
        title = "TAPE:"
        control = controls['tape']
        color = [1, 0.25, 0.25]
        color_dark = [divide / 2 for divide in color]
        color_light = [1, 1, 1]
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
        ctx.set_source_rgb(*color_dark)
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
        ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
        if controls['tape'] == 127:
            ctx.set_source_rgb(*screen_dark)
        else:
            pat = cairo.MeshPattern()
            pat.begin_patch()
            pat.move_to(center_x, center_y - 50)
            pat.line_to(center_x - 60, center_y - 50)
            pat.line_to(center_x - 60, center_y + 50)
            pat.line_to(center_x + 200, center_y + 200)
            pat.set_corner_color_rgb(0, *color)
            pat.set_corner_color_rgb(1, *color)
            pat.set_corner_color_rgb(2, *color)
            pat.set_corner_color_rgb(3, *color_light)
            pat.end_patch()
            pat.begin_patch()
            pat.move_to(center_x, center_y + 500)
            pat.line_to(center_x + 60, center_y + 50)
            pat.line_to(center_x + 60, center_y - 50)
            pat.line_to(center_x, center_y - 50)
            pat.set_corner_color_rgb(0, *color_dark)
            pat.set_corner_color_rgb(1, *color)
            pat.set_corner_color_rgb(2, *color)
            pat.set_corner_color_rgb(3, *color)
            pat.end_patch()
            ctx.set_source(pat)
        ctx.set_line_width(10)
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
            ctx.set_source_rgb(*color_light)
        ctx.arc(center_x, center_y, rad, pos1, pos2)
        ctx.set_line_width(12)
        ctx.stroke()

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

    def update_buttons(self):

        # Color all buttons...
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_SETUP, definitions.OFF_BTN_COLOR)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_1, definitions.ROOT_KEY)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_2, definitions.ROOT_KEY)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_3, definitions.BLACK)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_4, definitions.ORANGE)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_5, definitions.PURPLE)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_6, definitions.YELLOW)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_7, definitions.CYAN)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_8, definitions.RED)

        self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_1, definitions.WHITE)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_2, definitions.WHITE)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_3, definitions.YELLOW)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_4, definitions.YELLOW)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_5, definitions.ORANGE)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_6, definitions.ORANGE)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_7, definitions.PINK)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_8, definitions.PINK)

        self.push.buttons.set_button_color(push2_python.constants.BUTTON_PLAY, definitions.PINK)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_RECORD, definitions.YELLOW)

        # Settings button, to toggle settings mode
        if self.app.is_mode_active(self.app.settings_mode):
            self.push.buttons.set_button_color(SETTINGS_BUTTON, definitions.WHITE)
        else:
            self.push.buttons.set_button_color(SETTINGS_BUTTON, definitions.OFF_BTN_COLOR)

    def clean_currently_notes_being_played(self):
        if self.app.is_mode_active(self.app.melodic_mode):
            self.app.melodic_mode.remove_all_notes_being_played()
        elif self.app.is_mode_active(self.app.rhyhtmic_mode):
            self.app.rhyhtmic_mode.remove_all_notes_being_played()

    def on_encoder_rotated(self, encoder_name, increment):

        # encoder 1
        if encoder_name == push2_python.constants.ENCODER_TRACK1_ENCODER:
            def update_encoder_value(increment):
                updated_value = int(controls['instr'] + increment)
                if updated_value < 0:
                    controls['instr'] = 0
                elif updated_value > max_encoder_value:
                    controls['instr'] = max_encoder_value
                else:
                    controls['instr'] = updated_value

            update_encoder_value(increment)
            msg = mido.Message('control_change', control=21, value=controls['instr'])
            self.app.send_midi(msg)

            if controls['instr'] <= 41:
                if not definitions.ROOT_KEY == definitions.PINK:
                    definitions.ROOT_KEY = definitions.PINK
                    definitions.NOTE_ON_COLOR = definitions.GREEN
                    self.clean_currently_notes_being_played()
                    self.app.set_melodic_mode()
                    self.app.pads_need_update = True
                    self.update_pads()
                    self.app.buttons_need_update = True
                    self.update_buttons()

            if 42 <= controls['instr'] <= 81:
                if not definitions.ROOT_KEY == definitions.GREEN:
                    definitions.ROOT_KEY = definitions.GREEN
                    definitions.NOTE_ON_COLOR = definitions.PINK
                    self.clean_currently_notes_being_played()
                    self.app.set_melodic_mode()
                    self.app.pads_need_update = True
                    self.update_pads()
                    self.app.buttons_need_update = True
                    self.update_buttons()

            if controls['instr'] >= 82:
                if not definitions.ROOT_KEY == definitions.PURPLE:
                    definitions.ROOT_KEY = definitions.PURPLE
                    definitions.NOTE_ON_COLOR = definitions.WHITE
                    # definitions.LAYOUT_INSTRUMENT = 'lrhytmic'
                    self.clean_currently_notes_being_played()
                    self.app.set_rhythmic_mode()
                    self.app.pads_need_update = True
                    self.update_pads()
                    self.app.buttons_need_update = True
                    self.update_buttons()
                    # self.app.melodic_mode.remove_all_notes_being_played()

        # encoder 2
        if encoder_name == push2_python.constants.ENCODER_TRACK2_ENCODER:
            def update_encoder_value(increment):
                updated_filter_value = int(controls['instr_lpf'] + increment)
                if updated_filter_value < 0:
                    controls['instr_lpf'] = 0
                elif updated_filter_value > max_encoder_value:
                    controls['instr_lpf'] = max_encoder_value
                else:
                    controls['instr_lpf'] = updated_filter_value

            update_encoder_value(increment)
            msg = mido.Message('control_change', control=22, value=controls['instr_lpf'])
            self.app.send_midi(msg)

        # encoder 3
        if encoder_name == push2_python.constants.ENCODER_TRACK3_ENCODER:
            def update_encoder_value(increment):
                updated_filter_value = int(controls['instr_vol'] + increment)
                if updated_filter_value < 0:
                    controls['instr_vol'] = 0
                elif updated_filter_value > max_encoder_value:
                    controls['instr_vol'] = max_encoder_value
                else:
                    controls['instr_vol'] = updated_filter_value

            update_encoder_value(increment)
            msg = mido.Message('control_change', control=23, value=controls['instr_vol'])
            self.app.send_midi(msg)

        # encoder 4
        if encoder_name == push2_python.constants.ENCODER_TRACK4_ENCODER:
            def update_encoder_value(increment):
                updated_filter_value = int(controls['master_lpf'] + increment)
                if updated_filter_value < 0:
                    controls['master_lpf'] = 0
                elif updated_filter_value > max_encoder_value:
                    controls['master_lpf'] = max_encoder_value
                else:
                    controls['master_lpf'] = updated_filter_value

            update_encoder_value(increment)
            msg = mido.Message('control_change', control=24, value=controls['master_lpf'])
            self.app.send_midi(msg)

        # encoder 5
        if encoder_name == push2_python.constants.ENCODER_TRACK5_ENCODER:
            def update_encoder_value(increment):
                updated_filter_value = int(controls['fx'] + increment)
                if updated_filter_value < 0:
                    controls['fx'] = 0
                elif updated_filter_value > max_encoder_value:
                    controls['fx'] = max_encoder_value
                else:
                    controls['fx'] = updated_filter_value

            update_encoder_value(increment)
            msg = mido.Message('control_change', control=25, value=controls['fx'])
            self.app.send_midi(msg)

        # encoder 6
        if encoder_name == push2_python.constants.ENCODER_TRACK6_ENCODER:
            def update_encoder_value(increment):
                updated_filter_value = int(controls['smile'] + increment)
                if updated_filter_value < 0:
                    controls['smile'] = 0
                elif updated_filter_value > max_encoder_value:
                    controls['smile'] = max_encoder_value
                else:
                    controls['smile'] = updated_filter_value

            update_encoder_value(increment)
            msg = mido.Message('control_change', control=26, value=controls['smile'])
            self.app.send_midi(msg)

        # encoder 7
        if encoder_name == push2_python.constants.ENCODER_TRACK7_ENCODER:
            def update_encoder_value(increment):
                updated_filter_value = int(controls['reverb'] + increment)
                if updated_filter_value < 0:
                    controls['reverb'] = 0
                elif updated_filter_value > max_encoder_value:
                    controls['reverb'] = max_encoder_value
                else:
                    controls['reverb'] = updated_filter_value

            update_encoder_value(increment)
            msg = mido.Message('control_change', control=27, value=controls['reverb'])
            self.app.send_midi(msg)

        # encoder 8
        if encoder_name == push2_python.constants.ENCODER_TRACK8_ENCODER:
            def update_encoder_value(increment):
                updated_filter_value = int(controls['tape'] + increment)
                if updated_filter_value < 0:
                    controls['tape'] = 0
                elif updated_filter_value > max_encoder_value:
                    controls['tape'] = max_encoder_value
                else:
                    controls['tape'] = updated_filter_value

            update_encoder_value(increment)
            msg = mido.Message('control_change', control=28, value=controls['tape'])
            self.app.send_midi(msg)

    def on_button_pressed(self, button_name):
        if button_name == SETTINGS_BUTTON:
            self.app.toggle_and_rotate_settings_mode()
            self.app.buttons_need_update = True

        # PRESSED UPP button 2
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_2:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_2, definitions.BLACK)

        # PRESSED UPP button 4
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_4:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_4, definitions.BLACK)

        # PRESSED UPP button 5
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_5:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_5, definitions.BLACK)

        # PRESSED UPP button 6
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_6:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_6, definitions.BLACK)

        # PRESSED UPP button 7
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_7:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_7, definitions.BLACK)

        # PRESSED UPP button 8
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_8:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_8, definitions.BLACK)

        # PRESSED LOW button 1
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_1:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_1, definitions.BLACK)
            transport['cue1'] = 127
            msg = mido.Message('control_change', control=101, value=transport['cue1'])
            self.app.send_midi(msg)

        # PRESSED LOW button 2
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_2:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_2, definitions.BLACK)
            transport['cue2'] = 127
            msg = mido.Message('control_change', control=102, value=transport['cue2'])
            self.app.send_midi(msg)

        # PRESSED LOW button 3
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_3:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_3, definitions.BLACK)
            transport['bar1'] = 127
            msg = mido.Message('control_change', control=103, value=transport['bar1'])
            self.app.send_midi(msg)

        # PRESSED LOW button 4
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_4:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_4, definitions.BLACK)
            transport['bar2'] = 127
            msg = mido.Message('control_change', control=104, value=transport['bar2'])
            self.app.send_midi(msg)

        # PRESSED LOW button 5
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_5:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_5, definitions.BLACK)
            transport['beat1'] = 127
            msg = mido.Message('control_change', control=105, value=transport['beat1'])
            self.app.send_midi(msg)

        # PRESSED LOW button 6
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_6:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_6, definitions.BLACK)
            transport['beat2'] = 127
            msg = mido.Message('control_change', control=106, value=transport['beat2'])
            self.app.send_midi(msg)

        # PRESSED LOW button 7
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_7:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_7, definitions.BLACK)
            transport['nudge1'] = 127
            msg = mido.Message('control_change', control=107, value=transport['nudge1'])
            self.app.send_midi(msg)

        # PRESSED LOW button 8
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_8:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_8, definitions.BLACK)
            transport['nudge2'] = 127
            msg = mido.Message('control_change', control=108, value=transport['nudge2'])
            self.app.send_midi(msg)

        # PRESSED button play
        if button_name == push2_python.constants.BUTTON_PLAY:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_PLAY, definitions.BLACK)
            msg = mido.Message('control_change', control=109, value=127)
            self.app.send_midi(msg)

        # PRESSED button record
        if button_name == push2_python.constants.BUTTON_RECORD:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_RECORD, definitions.BLACK)
            msg = mido.Message('control_change', control=100, value=127)
            self.app.send_midi(msg)

    def on_button_released(self, button_name):

        # RELEASED UPP button 2
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_2:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_2, definitions.ROOT_KEY)
            controls['instr_lpf'] = 127
            msg = mido.Message('control_change', control=22, value=controls['instr_lpf'])
            self.app.send_midi(msg)

        # RELEASED UPP button 4
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_4:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_4, definitions.ORANGE)
            controls['master_lpf'] = 127
            msg = mido.Message('control_change', control=24, value=controls['master_lpf'])
            self.app.send_midi(msg)

        # RELEASED UPP button 5
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_5:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_5, definitions.PURPLE)
            controls['fx'] = 127
            msg = mido.Message('control_change', control=25, value=controls['fx'])
            self.app.send_midi(msg)

        # RELEASED UPP button 6
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_6:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_6, definitions.YELLOW)
            controls['smile'] = 0
            msg = mido.Message('control_change', control=26, value=controls['smile'])
            self.app.send_midi(msg)

        # RELEASED UPP button 7
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_7:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_7, definitions.CYAN)
            controls['reverb'] = 0
            msg = mido.Message('control_change', control=27, value=controls['reverb'])
            self.app.send_midi(msg)

        # RELEASED UPP button 8
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_8:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_8, definitions.RED)
            controls['tape'] = 127
            msg = mido.Message('control_change', control=28, value=controls['tape'])
            self.app.send_midi(msg)

        # RELEASED LOW button 1
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_1:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_1, definitions.WHITE)
            transport['cue1'] = 0
            msg = mido.Message('control_change', control=101, value=transport['cue1'])
            self.app.send_midi(msg)

        # RELEASED LOW button 2
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_2:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_2, definitions.WHITE)
            transport['cue2'] = 0
            msg = mido.Message('control_change', control=102, value=transport['cue2'])
            self.app.send_midi(msg)

        # RELEASED LOW button 3
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_3:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_3, definitions.YELLOW)
            transport['bar1'] = 0
            msg = mido.Message('control_change', control=103, value=transport['bar1'])
            self.app.send_midi(msg)

        # RELEASED LOW button 4
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_4:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_4, definitions.YELLOW)
            transport['bar2'] = 0
            msg = mido.Message('control_change', control=104, value=transport['bar2'])
            self.app.send_midi(msg)

        # RELEASED LOW button 5
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_5:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_5, definitions.ORANGE)
            transport['beat1'] = 0
            msg = mido.Message('control_change', control=105, value=transport['beat1'])
            self.app.send_midi(msg)

        # RELEASED LOW button 6
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_6:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_6, definitions.ORANGE)
            transport['beat2'] = 0
            msg = mido.Message('control_change', control=106, value=transport['beat2'])
            self.app.send_midi(msg)

        # RELEASED LOW button 7
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_7:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_7, definitions.PINK)
            transport['nudge1'] = 0
            msg = mido.Message('control_change', control=107, value=transport['nudge1'])
            self.app.send_midi(msg)

        # RELEASED LOW button 8
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_8:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_8, definitions.PINK)
            transport['nudge2'] = 0
            msg = mido.Message('control_change', control=108, value=transport['nudge2'])
            self.app.send_midi(msg)

        # RELEASED button play
        if button_name == push2_python.constants.BUTTON_PLAY:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_PLAY, definitions.PINK)
            msg = mido.Message('control_change', control=109, value=0)
            self.app.send_midi(msg)

        # RELEASED button record
        if button_name == push2_python.constants.BUTTON_RECORD:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_RECORD, definitions.YELLOW)
            msg = mido.Message('control_change', control=100, value=0)
            self.app.send_midi(msg)
