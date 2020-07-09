import definitions
import push2_python
import cairo
import mido

from pyramidi_mode import MIDICCControl

SETTINGS_BUTTON = push2_python.constants.BUTTON_SETUP

controls = {'instrument': 0, 'filter': 127, 'smile': 0, 'reverb': 0, 'tape': 127 }

max_encoder_value = 127



class MainControlsMode(definitions.PyshaMode):

    def activate(self):
        self.update_buttons()

    def deactivate(self):
        self.push.buttons.set_button_color(SETTINGS_BUTTON, definitions.BLACK)

    # def generate_display_frame():
    def update_display(self, ctx, w, h):

        ####################################################################################
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

        # Filter "canvas"
        ctx.rectangle(120, 25, 254, 90)
        ctx.set_source_rgb(0.1, 0.05, 0.01)
        ctx.fill()

        # Filter frequency:
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

        # Smile canvas
        ctx.arc(660, 70, 42, 0, 2 * 3.14)
        ctx.set_source_rgb(0.1, 0.1, 0)
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

    def update_buttons(self):
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_SETUP, definitions.WHITE)

        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_1, definitions.ROOT_KEY)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_2, definitions.ORANGE)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_3, definitions.BLACK)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_4, definitions.BLACK)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_5, definitions.BLACK)
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
            self.push.buttons.set_button_color(SETTINGS_BUTTON, definitions.WHITE, animation='pulsing')
        else:
            self.push.buttons.set_button_color(SETTINGS_BUTTON, definitions.OFF_BTN_COLOR)

    def on_encoder_rotated(self, encoder_name, increment):

# encoder 1
        if encoder_name == push2_python.constants.ENCODER_TRACK1_ENCODER:
            def update_encoder_value(increment):
                updated_value = int(controls['instrument'] + increment)
                if updated_value < 0:
                    controls['instrument'] = 0
                elif updated_value > max_encoder_value:
                    controls['instrument'] = max_encoder_value
                else:
                    controls['instrument'] = updated_value

            update_encoder_value(increment)
            # msg = mido.Message('control_change', control=21, value=controls['instrument'])
            # self.send_midi_func(msg)

            if controls['instrument'] <= 41:
                definitions.ROOT_KEY = definitions.PINK
                definitions.LAYOUT_INSTRUMENT = 'lmelodic'
                definitions.NOTE_ON_COLOR = definitions.SURF
                self.app.set_melodic_mode()
                self.app.pads_need_update = True
                self.update_pads()
                self.app.buttons_need_update = True
                self.update_buttons()
                self.app.melodic_mode.remove_all_notes_being_played()

            if controls['instrument'] >= 42:
                if controls['instrument'] <= 81:
                    definitions.ROOT_KEY = definitions.GREEN
                    definitions.LAYOUT_INSTRUMENT = 'lmelodic'
                    definitions.NOTE_ON_COLOR = definitions.PINK
                    self.app.set_melodic_mode()
                    self.app.pads_need_update = True
                    self.update_pads()
                    self.app.buttons_need_update = True
                    self.update_buttons()
                    self.app.melodic_mode.remove_all_notes_being_played()

            if controls['instrument'] >= 82:
                definitions.ROOT_KEY = definitions.PURPLE
                definitions.LAYOUT_INSTRUMENT = 'lrhytmic'
                definitions.NOTE_ON_COLOR = definitions.WHITE
                self.app.set_rhythmic_mode()
                self.app.pads_need_update = True
                self.update_pads()
                self.app.buttons_need_update = True
                self.update_buttons()
                self.app.melodic_mode.remove_all_notes_being_played()
# encoder 2
        if encoder_name == push2_python.constants.ENCODER_TRACK2_ENCODER:
            def update_encoder_value(increment):
                updated_filter_value = int(controls['filter'] + increment)
                if updated_filter_value < 0: controls['filter'] = 0
                elif updated_filter_value > max_encoder_value: controls['filter'] = max_encoder_value
                else: controls['filter'] = updated_filter_value
            update_encoder_value(increment)

# encoder 6
        if encoder_name == push2_python.constants.ENCODER_TRACK6_ENCODER:
            def update_encoder_value(increment):
                updated_filter_value = int(controls['smile'] + increment)
                if updated_filter_value < 0: controls['smile'] = 0
                elif updated_filter_value > max_encoder_value: controls['smile'] = max_encoder_value
                else: controls['smile'] = updated_filter_value
            update_encoder_value(increment)

# encoder 7
        if encoder_name == push2_python.constants.ENCODER_TRACK7_ENCODER:
            def update_encoder_value(increment):
                updated_filter_value = int(controls['reverb'] + increment)
                if updated_filter_value < 0: controls['reverb'] = 0
                elif updated_filter_value > max_encoder_value: controls['reverb'] = max_encoder_value
                else: controls['reverb'] = updated_filter_value
            update_encoder_value(increment)

# encoder 8
        if encoder_name == push2_python.constants.ENCODER_TRACK8_ENCODER:
            def update_encoder_value(increment):
                updated_filter_value = int(controls['tape'] + increment)
                if updated_filter_value < 0: controls['tape'] = 0
                elif updated_filter_value > max_encoder_value: controls['tape'] = max_encoder_value
                else: controls['tape'] = updated_filter_value
            update_encoder_value(increment)

    def on_button_pressed(self, button_name):
        if button_name == SETTINGS_BUTTON:
            self.app.toggle_and_rotate_settings_mode()
            self.app.buttons_need_update = True

# PRESSED button 2
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_2:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_2, definitions.WHITE)

# PRESSED button 6
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_6:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_6, definitions.WHITE)

# PRESSED button 7
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_7:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_7, definitions.WHITE)

# PRESSED button 8
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_8:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_8, definitions.WHITE)

# PRESSED LOW button 1
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_1:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_1, definitions.WHITE)
            # msg = mido.Message('control_change', control=101, value=127)
            # self.app.send_midi(msg)

# PRESSED LOW button 2
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_2:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_2, definitions.WHITE)
            # msg = mido.Message('control_change', control=102, value=127)
            # self.app.send_midi(msg)

# PRESSED LOW button 3
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_3:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_3, definitions.WHITE)
            # msg = mido.Message('control_change', control=103, value=127)
            # self.app.send_midi(msg)

# PRESSED LOW button 4
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_4:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_4, definitions.WHITE)
            # msg = mido.Message('control_change', control=104, value=127)
            # self.app.send_midi(msg)

# PRESSED LOW button 5
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_5:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_5, definitions.WHITE)
            # msg = mido.Message('control_change', control=105, value=127)
            # self.app.send_midi(msg)

# PRESSED LOW button 6
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_6:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_6, definitions.WHITE)
            # msg = mido.Message('control_change', control=106, value=127)
            # self.app.send_midi(msg)

# PRESSED LOW button 7
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_7:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_7, definitions.WHITE)
            # msg = mido.Message('control_change', control=107, value=127)
            # self.app.send_midi(msg)

# PRESSED LOW button 8
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_8:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_8, definitions.WHITE)
            # msg = mido.Message('control_change', control=108, value=127)
            # self.app.send_midi(msg)

# PRESSED button play
        if button_name == push2_python.constants.BUTTON_PLAY:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_PLAY, definitions.WHITE)
            # msg = mido.Message('control_change', control=109, value=127)
            # self.app.send_midi(msg)

# PRESSED button record
        if button_name == push2_python.constants.BUTTON_RECORD:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_1, definitions.WHITE)
            # msg = mido.Message('control_change', control=100, value=127)
            # self.app.send_midi(msg)

    def on_button_released(self, button_name):

# RELEASED UPP button 2
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_2:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_2, definitions.ORANGE)
            controls['filter'] = 127

# RELEASED UPP button 6
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_6:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_6, definitions.YELLOW)
            controls['smile'] = 0

# RELEASED UPP button 7
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_7:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_7, definitions.CYAN)
            controls['reverb'] = 0

# RELEASED UPP button 8
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_8:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_8, definitions.RED)
            controls['tape'] = 127

# RELEASED LOW button 1
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_1:
            # msg = mido.Message('control_change', control=101, value=0)
            # self.app.send_midi(msg)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_1, definitions.WHITE)

# RELEASED LOW button 2
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_2:
            # msg = mido.Message('control_change', control=102, value=0)
            # self.app.send_midi(msg)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_2, definitions.WHITE)

# RELEASED LOW button 3
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_3:
            # msg = mido.Message('control_change', control=103, value=0)
            # self.app.send_midi(msg)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_3, definitions.YELLOW)

# RELEASED LOW button 4
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_4:
            # msg = mido.Message('control_change', control=104, value=0)
            # self.app.send_midi(msg)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_4, definitions.YELLOW)

# RELEASED LOW button 5
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_5:
            # msg = mido.Message('control_change', control=105, value=0)
            # self.app.send_midi(msg)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_5, definitions.ORANGE)

# RELEASED LOW button 6
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_6:
            # msg = mido.Message('control_change', control=106, value=0)
            # self.app.send_midi(msg)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_6, definitions.ORANGE)

# RELEASED LOW button 7
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_7:
            # msg = mido.Message('control_change', control=107, value=0)
            # self.app.send_midi(msg)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_7, definitions.PINK)

# RELEASED LOW button 8
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_8:
            # msg = mido.Message('control_change', control=108, value=0)
            # self.app.send_midi(msg)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_8, definitions.PINK)

# RELEASED button play
        if button_name == push2_python.constants.BUTTON_PLAY:
            # msg = mido.Message('control_change', control=109, value=0)
            # self.app.send_midi(msg)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_PLAY, definitions.PINK)

# RELEASED button record
        if button_name == push2_python.constants.BUTTON_RECORD:
            # msg = mido.Message('control_change', control=100, value=0)
            # self.app.send_midi(msg)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_1, definitions.YELLOW)
