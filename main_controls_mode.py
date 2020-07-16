import cairo
import mido
import push2_python

import definitions

SETTINGS_BUTTON = push2_python.constants.BUTTON_SETUP

controls = {'instr': 0, 'instr_lpf': 127, 'master_lpf': 127, 'fx': 127, 'smile': 0, 'reverb': 0, 'tape': 127}

max_encoder_value = 127


class MainControlsMode(definitions.PyshaMode):

    def activate(self):
        self.update_buttons()

    def deactivate(self):
        self.push.buttons.set_button_color(SETTINGS_BUTTON, definitions.BLACK)

    # def generate_display_frame():
    def update_display(self, ctx, w, h):

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
        # Piano
        if controls['instr'] <= 41:
            ctx.set_source_rgb(1, 0.25, 0.5)
        # Synth
        if 42 <= controls['instr'] <= 81:
            ctx.set_source_rgb(0, 1, 0.7)
        # Sampler
        if controls['instr'] >= 82:
            ctx.set_source_rgb(0.75, 0, 1)
        ctx.show_text(s)

        # Instrument canvas
        ctx.rectangle(15, 23 + (30 * (controls['instr'] / 127)), 90, 15)
        # Piano
        if controls['instr'] <= 41:
            ctx.set_source_rgb(1, 0.25, 0.5)
        # Synth
        if 42 <= controls['instr'] <= 81:
            ctx.set_source_rgb(0, 0.9, 0.6)
        # Sampler
        if controls['instr'] >= 82:
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
        # Piano
        if controls['instr'] <= 41:
            ctx.set_source_rgb(1, 0.25, 0.5)
        # Synth
        if 42 <= controls['instr'] <= 81:
            ctx.set_source_rgb(0, 1, 0.7)
        # Sampler
        if controls['instr'] >= 82:
            ctx.set_source_rgb(0.75, 0, 1)
        ctx.set_font_size(12)
        ctx.select_font_face(font, normal, bold)
        s = "INSTRUMENT LPF:"
        ctx.move_to(180 - (ctx.text_extents(s)[2] / 2), 15)
        ctx.show_text(s)

        # Instrument_filter value (canvas - inverted)
        ctx.arc(180, 70, 42, 0, 2 * 3.14)
        # Piano
        if controls['instr'] <= 41:
            ctx.set_source_rgb(1, 0.5, 0.75)
            if controls['instr_lpf'] == 127:
                ctx.set_source_rgb(0.1, 0.025, 0.05)
        # Synth
        if 42 <= controls['instr'] <= 81:
            ctx.set_source_rgb(0.5, 1, 0.95)
            if controls['instr_lpf'] == 127:
                ctx.set_source_rgb(0, 0.1, 0.07)
        # Sampler
        if controls['instr'] >= 82:
            ctx.set_source_rgb(0.9, 0.25, 1)
            if controls['instr_lpf'] == 127:
                ctx.set_source_rgb(0.075, 0, 0.075)
        ctx.fill()
        ctx.stroke()

        # Instrument_filter canvas (value - inverted)
        ctx.move_to(180, 75)
        ctx.arc(180, 70, 42, 3.14 / 2, 3.14 / 2 + 360 * (controls['instr_lpf'] / 127) * (3.14 / 180))
        ctx.close_path()
        ctx.set_source_rgb(0.02, 0.02, 0.02)
        ctx.fill()
        ctx.stroke()

        # Instrument_filter frame
        ctx.arc(180, 70, 42, 0, 2 * 3.14)
        if controls['instr_lpf'] == 127:
            ctx.set_source_rgb(0.032, 0.032, 0.032)
        else:
            # Piano
            if controls['instr'] <= 41:
                ctx.set_source_rgb(1, 0.25, 0.5)
            # Synth
            if 42 <= controls['instr'] <= 81:
                ctx.set_source_rgb(0.05, 0.9, 0.7)
            # Sampler
            if controls['instr'] >= 82:
                ctx.set_source_rgb(0.75, 0, 1)
        ctx.set_line_width(5)
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
        ctx.set_source_rgb(1, 0.75, 0.3)
        if controls['master_lpf'] == 127:
            ctx.set_source_rgb(0.1, 0.05, 0.01)
        ctx.fill()
        ctx.stroke()

        # Master_filter canvas (value - inverted)
        ctx.move_to(420, 75)
        ctx.arc(420, 70, 42, 3.14 / 2, 3.14 / 2 + 360 * (controls['master_lpf'] / 127) * (3.14 / 180))
        ctx.close_path()
        ctx.set_source_rgb(0.02, 0.02, 0.02)
        ctx.fill()
        ctx.stroke()

        # Master_filter frame
        ctx.arc(420, 70, 42, 0, 2 * 3.14)
        if controls['master_lpf'] == 127:
            ctx.set_source_rgb(0.032, 0.032, 0.032)
        else:
            ctx.set_source_rgb(1, 0.5, 0.1)
        ctx.set_line_width(5)
        ctx.stroke()

        # FX mix title
        ctx.set_source_rgb(0.75, 0, 1)
        ctx.set_font_size(12)
        ctx.select_font_face(font, normal, bold)
        s = "FX MIX:"
        ctx.move_to(540 - (ctx.text_extents(s)[2] / 2), 15)
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
                increment = increment / 2
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
                increment = increment / 2
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

        # encoder 4
        if encoder_name == push2_python.constants.ENCODER_TRACK4_ENCODER:
            def update_encoder_value(increment):
                increment = increment / 2
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
                increment = increment / 2
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
                increment = increment / 2
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
                increment = increment / 2
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
                increment = increment / 2
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
            msg = mido.Message('control_change', control=101, value=127)
            self.app.send_midi(msg)

        # PRESSED LOW button 2
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_2:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_2, definitions.BLACK)
            msg = mido.Message('control_change', control=102, value=127)
            self.app.send_midi(msg)

        # PRESSED LOW button 3
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_3:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_3, definitions.BLACK)
            msg = mido.Message('control_change', control=103, value=127)
            self.app.send_midi(msg)

        # PRESSED LOW button 4
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_4:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_4, definitions.BLACK)
            msg = mido.Message('control_change', control=104, value=127)
            self.app.send_midi(msg)

        # PRESSED LOW button 5
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_5:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_5, definitions.BLACK)
            msg = mido.Message('control_change', control=105, value=127)
            self.app.send_midi(msg)

        # PRESSED LOW button 6
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_6:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_6, definitions.BLACK)
            msg = mido.Message('control_change', control=106, value=127)
            self.app.send_midi(msg)

        # PRESSED LOW button 7
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_7:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_7, definitions.BLACK)
            msg = mido.Message('control_change', control=107, value=127)
            self.app.send_midi(msg)

        # PRESSED LOW button 8
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_8:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_8, definitions.BLACK)
            msg = mido.Message('control_change', control=108, value=127)
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
            msg = mido.Message('control_change', control=22, value=127)
            self.app.send_midi(msg)

        # RELEASED UPP button 4
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_4:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_4, definitions.ORANGE)
            controls['master_lpf'] = 127
            msg = mido.Message('control_change', control=24, value=127)
            self.app.send_midi(msg)

        # RELEASED UPP button 5
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_5:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_5, definitions.PURPLE)
            controls['fx'] = 127
            msg = mido.Message('control_change', control=25, value=127)
            self.app.send_midi(msg)

        # RELEASED UPP button 6
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_6:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_6, definitions.YELLOW)
            controls['smile'] = 0
            msg = mido.Message('control_change', control=26, value=0)
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
            msg = mido.Message('control_change', control=101, value=0)
            self.app.send_midi(msg)

        # RELEASED LOW button 2
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_2:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_2, definitions.WHITE)
            msg = mido.Message('control_change', control=102, value=0)
            self.app.send_midi(msg)

        # RELEASED LOW button 3
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_3:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_3, definitions.YELLOW)
            msg = mido.Message('control_change', control=103, value=0)
            self.app.send_midi(msg)

        # RELEASED LOW button 4
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_4:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_4, definitions.YELLOW)
            msg = mido.Message('control_change', control=104, value=0)
            self.app.send_midi(msg)

        # RELEASED LOW button 5
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_5:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_5, definitions.ORANGE)
            msg = mido.Message('control_change', control=105, value=0)
            self.app.send_midi(msg)

        # RELEASED LOW button 6
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_6:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_6, definitions.ORANGE)
            msg = mido.Message('control_change', control=106, value=0)
            self.app.send_midi(msg)

        # RELEASED LOW button 7
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_7:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_7, definitions.PINK)
            msg = mido.Message('control_change', control=107, value=0)
            self.app.send_midi(msg)

        # RELEASED LOW button 8
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_8:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_8, definitions.PINK)
            msg = mido.Message('control_change', control=108, value=0)
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
