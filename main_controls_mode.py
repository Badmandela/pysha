import mido
import push2_python

import definitions
from display_utils import draw_title, draw_list, draw_knob, draw_cue, draw_bar, draw_beat, draw_nudge_1, draw_nudge_2
from knob import update_encoder

max_encoder_value = 254
piano_range = range(0, 40)
synth_range = range(40, 140)
sampler_range = range(140, 220)
ghost_range = range(220, 255)

controls = {'instr': 0, 'instr_lpf': 254, 'master_lpf': 254, 'fx': 0, 'smile': 0, 'reverb': 0, 'tape': 254}
transport = {'cue1': 0, 'cue2': 0, 'bar1': 0, 'bar2': 0, 'beat1': 0, 'beat2': 0, 'nudge1': 0, 'nudge2': 0}


class MainControlsMode(definitions.PyshaMode):

    def activate(self):
        self.update_buttons()

    def deactivate(self):
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_SETUP, definitions.BLACK)

    def update_display(self, ctx, w, h):

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
        ctx.rectangle(12, 23 + (60 * (control / 254)), 98, 15)
        ctx.fill()

        # Instruments list
        # 1
        text = "ELECTRIC PIANO"
        y = 34
        if control in piano_range:
            color = [1, 1, 1, 1]
        else:
            color = [1, 1, 1, 0.25]
        draw_list(ctx, center_x, y, text, *color)

        # 2
        text = "SYNTHESIZER"
        y = 54
        if control in synth_range:
            color = [1, 1, 1, 1]
        else:
            color = [1, 1, 1, 0.25]
        draw_list(ctx, center_x, y, text, *color)

        # 3
        text = "SAMPLER"
        y = 74
        if control in sampler_range:
            color = [1, 1, 1, 1]
        else:
            color = [1, 1, 1, 0.25]
        draw_list(ctx, center_x, y, text, *color)

        # 4
        text = "GHOST"
        y = 94
        if control in ghost_range:
            color = [1, 1, 1, 1]
        else:
            color = [1, 1, 1, 0.25]
        draw_list(ctx, center_x, y, text, *color)

        # Instrument_filter QUASI-GLOBALS
        title = "INSTR. LPF:"
        instrument = controls['instr']
        control = controls['instr_lpf']
        off_value = 254

        # Active text
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

        else:
            color = [1, 0.75, 0.75]

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

    def update_buttons(self):
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

        self.push.buttons.set_button_color(push2_python.constants.BUTTON_SETUP, definitions.WHITE)

    def clean_currently_notes_being_played(self):
        if self.app.is_mode_active(self.app.melodic_mode):
            self.app.melodic_mode.remove_all_notes_being_played()
        elif self.app.is_mode_active(self.app.rhyhtmic_mode):
            self.app.rhyhtmic_mode.remove_all_notes_being_played()

    def on_encoder_rotated(self, encoder_name, increment):

        if not self.app.is_mode_active(self.app.settings_mode):

            # encoder 1
            if encoder_name == push2_python.constants.ENCODER_TRACK1_ENCODER:
                msg, encoder = update_encoder(controls['instr'], 21, increment)
                self.app.send_midi(msg)
                controls['instr'] = encoder

                def update_instrument():
                    self.clean_currently_notes_being_played()
                    self.app.pads_need_update = True
                    self.update_pads()
                    self.app.buttons_need_update = True
                    self.update_buttons()

                if controls['instr'] in piano_range:
                    if not definitions.ROOT_KEY == definitions.PINK:
                        definitions.ROOT_KEY = definitions.PINK
                        definitions.NOTE_ON_COLOR = definitions.GREEN
                        self.app.set_melodic_mode()
                        update_instrument()

                if controls['instr'] in synth_range:
                    if not definitions.ROOT_KEY == definitions.GREEN:
                        definitions.ROOT_KEY = definitions.GREEN
                        definitions.NOTE_ON_COLOR = definitions.PINK
                        self.app.set_melodic_mode()
                        update_instrument()

                if controls['instr'] in sampler_range:
                    if not definitions.ROOT_KEY == definitions.PURPLE:
                        definitions.ROOT_KEY = definitions.PURPLE
                        definitions.NOTE_ON_COLOR = definitions.WHITE
                        self.app.set_rhythmic_mode()
                        update_instrument()

                if controls['instr'] in ghost_range:
                    if not definitions.ROOT_KEY == definitions.WHITE:
                        definitions.ROOT_KEY = definitions.WHITE
                        definitions.NOTE_ON_COLOR = definitions.PURPLE
                        self.app.set_melodic_mode()
                        update_instrument()

            # encoder 2
            if encoder_name == push2_python.constants.ENCODER_TRACK2_ENCODER:
                msg, encoder = update_encoder(controls['instr_lpf'], 22, increment)
                self.app.send_midi(msg)
                controls['instr_lpf'] = encoder

            # encoder 4
            if encoder_name == push2_python.constants.ENCODER_TRACK4_ENCODER:
                msg, encoder = update_encoder(controls['master_lpf'], 24, increment)
                self.app.send_midi(msg)
                controls['master_lpf'] = encoder

            # encoder 5
            if encoder_name == push2_python.constants.ENCODER_TRACK5_ENCODER:
                msg, encoder = update_encoder(controls['fx'], 25, increment)
                self.app.send_midi(msg)
                controls['fx'] = encoder

            # encoder 6
            if encoder_name == push2_python.constants.ENCODER_TRACK6_ENCODER:
                msg, encoder = update_encoder(controls['smile'], 26, increment)
                self.app.send_midi(msg)
                controls['smile'] = encoder

            # encoder 7
            if encoder_name == push2_python.constants.ENCODER_TRACK7_ENCODER:
                msg, encoder = update_encoder(controls['reverb'], 27, increment)
                self.app.send_midi(msg)
                controls['reverb'] = encoder

            # encoder 8
            if encoder_name == push2_python.constants.ENCODER_TRACK8_ENCODER:
                msg, encoder = update_encoder(controls['tape'], 28, increment)
                self.app.send_midi(msg)
                controls['tape'] = encoder

    def on_button_pressed(self, button_name):

        if button_name == push2_python.constants.BUTTON_SETUP:
            self.app.toggle_and_rotate_settings_mode()
            self.app.buttons_need_update = True

        # if button_name == push2_python.constants.BUTTON_DEVICE:
        #     self.app.toggle_and_rotate_play_mode()
        #     self.app.buttons_need_update = True

        if not self.app.is_mode_active(self.app.settings_mode):

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

        if not self.app.is_mode_active(self.app.settings_mode):

            # RELEASED UPP button 2
            if button_name == push2_python.constants.BUTTON_UPPER_ROW_2:
                self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_2, definitions.ROOT_KEY)
                controls['instr_lpf'] = 254
                # msg = mido.Message('control_change', control=22, value=controls['instr_lpf'])
                msg = mido.Message('control_change', control=22, value=int(round(controls['instr_lpf'] / 2)))
                self.app.send_midi(msg)

            # RELEASED UPP button 4
            if button_name == push2_python.constants.BUTTON_UPPER_ROW_4:
                self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_4, definitions.ORANGE)
                controls['master_lpf'] = 254
                # msg = mido.Message('control_change', control=24, value=controls['master_lpf'])
                msg = mido.Message('control_change', control=24, value=int(round(controls['master_lpf'] / 2)))
                self.app.send_midi(msg)

            # RELEASED UPP button 5
            if button_name == push2_python.constants.BUTTON_UPPER_ROW_5:
                self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_5, definitions.PURPLE)
                controls['fx'] = 254
                # msg = mido.Message('control_change', control=25, value=controls['fx'])
                msg = mido.Message('control_change', control=25, value=int(round(controls['fx'] / 2)))
                self.app.send_midi(msg)

            # RELEASED UPP button 6
            if button_name == push2_python.constants.BUTTON_UPPER_ROW_6:
                self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_6, definitions.YELLOW)
                controls['smile'] = 0
                # msg = mido.Message('control_change', control=26, value=controls['smile'])
                msg = mido.Message('control_change', control=26, value=int(round(controls['smile'] / 2)))
                self.app.send_midi(msg)

            # RELEASED UPP button 7
            if button_name == push2_python.constants.BUTTON_UPPER_ROW_7:
                self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_7, definitions.CYAN)
                controls['reverb'] = 0
                # msg = mido.Message('control_change', control=27, value=controls['reverb'])
                msg = mido.Message('control_change', control=27, value=int(round(controls['reverb'] / 2)))
                self.app.send_midi(msg)

            # RELEASED UPP button 8
            if button_name == push2_python.constants.BUTTON_UPPER_ROW_8:
                self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_8, definitions.RED)
                controls['tape'] = 254
                # msg = mido.Message('control_change', control=28, value=controls['tape'])
                msg = mido.Message('control_change', control=28, value=int(round(controls['tape'] / 2)))
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
