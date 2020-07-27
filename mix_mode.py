import push2_python
import push2_python.constants

import definitions
from display_utils import draw_potentiometer, draw_xr18_button, draw_mute_button

x_air = {'trm': 96, 'bas': 96, 'gtr': 96, 'v1': 96, 'v2': 96, 'bt': 96, 'delay': 96, 'reverb': 96}
x_air_button = {'trm': 0, 'bas': 0, 'gtr': 0, 'v1': 0, 'v2': 0, 'bt': 0, 'delay': 0, 'reverb': 0}
mute_value_list = {'trm': 127, 'bas': 127, 'gtr': 127, 'v1': 127, 'v2': 127, 'bt': 127, 'delay': 127, 'reverb': 127}

max_encoder_value = 127

class MixMode(definitions.PyshaMode):
    current_mix_page = 0
    n_mix_pages = 1
    encoders_state = {}

    def move_to_next_mix_page(self):
        self.app.buttons_need_update = True
        self.current_mix_page += 1
        if self.current_mix_page >= self.n_mix_pages:
            self.current_mix_page = 0
            return True  # Return true because page rotation finished 
        else:
            return False

    def activate(self):
        self.current_mix_page = 0
        self.update_buttons()

    def deactivate(self):
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_SETUP, definitions.OFF_BTN_COLOR)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_1, definitions.BLACK)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_2, definitions.BLACK)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_3, definitions.BLACK)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_4, definitions.BLACK)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_5, definitions.BLACK)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_6, definitions.BLACK)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_7, definitions.BLACK)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_8, definitions.BLACK)

        self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_1, definitions.BLACK)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_2, definitions.BLACK)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_3, definitions.BLACK)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_4, definitions.BLACK)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_5, definitions.BLACK)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_6, definitions.BLACK)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_7, definitions.BLACK)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_8, definitions.BLACK)

        self.push.buttons.set_button_color(push2_python.constants.BUTTON_PLAY, definitions.BLACK)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_RECORD, definitions.BLACK)

        self.push.buttons.set_button_color(push2_python.constants.BUTTON_MIX, definitions.WHITE)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_DEVICE, definitions.WHITE)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_SETUP, definitions.WHITE)

    def update_display(self, ctx, w, h):
        if self.current_mix_page == 0:  # Performance settings
            # Start of drawing code

            # Initial black rectangle
            ctx.rectangle(0, 0, w, h)
            ctx.set_source_rgb(0, 0, 0)
            ctx.fill()

            # Colors
            screen_black = [0, 0, 0]
            screen_dark = [0.05, 0.05, 0.05]

            # Globals
            rad = 45
            line = 10
            center_y = 75

            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            # Instrument QUASI-GLOBALS

            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            text = "ALBIN"
            control = x_air['trm']
            mute_value = mute_value_list['trm']
            xr18_button = x_air_button['trm']
            center_x = 60
            x = center_x
            color = [1, 1, 0]

            draw_xr18_button(ctx, x, xr18_button, text, color)
            draw_potentiometer(ctx, x, control, mute_value, color)
            draw_mute_button(ctx, x, mute_value, color)

            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            text = "NOAH"
            control = x_air['bas']
            mute_value = mute_value_list['bas']
            xr18_button = x_air_button['bas']
            center_x = 180
            x = center_x
            color = [0, 1, 0.5]

            draw_xr18_button(ctx, x, xr18_button, text, color)
            draw_potentiometer(ctx, x, control, mute_value, color)
            draw_mute_button(ctx, x, mute_value, color)

            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            text = "FREDRIK"
            control = x_air['gtr']
            mute_value = mute_value_list['gtr']
            xr18_button = x_air_button['gtr']
            center_x = 300
            x = center_x
            color = [0, 0.5, 1]

            draw_xr18_button(ctx, x, xr18_button, text, color)
            draw_potentiometer(ctx, x, control, mute_value, color)
            draw_mute_button(ctx, x, mute_value, color)

            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            text = "MARIA"
            control = x_air['v1']
            mute_value = mute_value_list['v1']
            xr18_button = x_air_button['v1']
            center_x = 420
            x = center_x
            color = [1, 0.25, 0.5]

            draw_xr18_button(ctx, x, xr18_button, text, color)
            draw_potentiometer(ctx, x, control, mute_value, color)
            draw_mute_button(ctx, x, mute_value, color)

            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            text = "MICHELLE"
            control = x_air['v2']
            mute_value = mute_value_list['v2']
            xr18_button = x_air_button['v2']
            center_x = 540
            x = center_x
            color = [0.875, 0, 1]

            draw_xr18_button(ctx, x, xr18_button, text, color)
            draw_potentiometer(ctx, x, control, mute_value, color)
            draw_mute_button(ctx, x, mute_value, color)

            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            text = "NIKLAS"
            control = x_air['bt']
            mute_value = mute_value_list['bt']
            xr18_button = x_air_button['bt']
            center_x = 660
            x = center_x
            color = [0.75, 0.75, 0.75]

            draw_xr18_button(ctx, x, xr18_button, text, color)
            draw_potentiometer(ctx, x, control, mute_value, color)
            draw_mute_button(ctx, x, mute_value, color)

            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            text = "REVERB"
            control = x_air['reverb']
            mute_value = mute_value_list['reverb']
            xr18_button = x_air_button['reverb']
            center_x = 780
            x = center_x
            color = [0.25, 0.75, 1]

            draw_xr18_button(ctx, x, xr18_button, text, color)
            draw_potentiometer(ctx, x, control, mute_value, color)
            draw_mute_button(ctx, x, mute_value, color)

            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            text = "DELAY"
            control = x_air['delay']
            mute_value = mute_value_list['delay']
            xr18_button = x_air_button['delay']
            center_x = 900
            x = center_x
            color = [0.25, 1, 0.75]

            draw_xr18_button(ctx, x, xr18_button, text, color)
            draw_potentiometer(ctx, x, control, mute_value, color)
            draw_mute_button(ctx, x, mute_value, color)

            # End of drawing code

    def update_buttons(self):
        if self.current_mix_page == 0:  # Performance settings
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_SETUP, definitions.OFF_BTN_COLOR)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_1, definitions.YELLOW)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_2, definitions.GREEN)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_3, definitions.CYAN)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_4, definitions.PINK)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_5, definitions.PURPLE)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_6, definitions.WHITE)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_7, definitions.CYAN)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_8, definitions.GREEN)

            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_1, definitions.YELLOW)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_2, definitions.GREEN)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_3, definitions.CYAN)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_4, definitions.PINK)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_5, definitions.PURPLE)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_6, definitions.WHITE)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_7, definitions.CYAN)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_8, definitions.GREEN)

            self.push.buttons.set_button_color(push2_python.constants.BUTTON_MIX, definitions.WHITE)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_DEVICE, definitions.WHITE)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_SETUP, definitions.WHITE)

    def on_encoder_rotated(self, encoder_name, increment):
        if self.current_mix_page == 0:  # Performance settings
            # encoder 1
            if encoder_name == push2_python.constants.ENCODER_TRACK1_ENCODER:
                def update_encoder_value(increment):
                    updated_filter_value = int(x_air['trm'] + increment)
                    if updated_filter_value < 0:
                        x_air['trm'] = 0
                    elif updated_filter_value > max_encoder_value:
                        x_air['trm'] = max_encoder_value
                    else:
                        x_air['trm'] = updated_filter_value

                update_encoder_value(increment)
                # msg = mido.Message('control_change', control=24, value=controls['master_lpf'])
                # self.app.send_midi(msg)

            # encoder 2
            if encoder_name == push2_python.constants.ENCODER_TRACK2_ENCODER:
                def update_encoder_value(increment):
                    updated_filter_value = int(x_air['bas'] + increment)
                    if updated_filter_value < 0:
                        x_air['bas'] = 0
                    elif updated_filter_value > max_encoder_value:
                        x_air['bas'] = max_encoder_value
                    else:
                        x_air['bas'] = updated_filter_value

                update_encoder_value(increment)
                # msg = mido.Message('control_change', control=22, value=controls['instr_lpf'])
                # self.app.send_midi(msg)

            # encoder 3
            if encoder_name == push2_python.constants.ENCODER_TRACK3_ENCODER:
                def update_encoder_value(increment):
                    updated_filter_value = int(x_air['gtr'] + increment)
                    if updated_filter_value < 0:
                        x_air['gtr'] = 0
                    elif updated_filter_value > max_encoder_value:
                        x_air['gtr'] = max_encoder_value
                    else:
                        x_air['gtr'] = updated_filter_value

                update_encoder_value(increment)
                # msg = mido.Message('control_change', control=23, value=controls['instr_vol'])
                # self.app.send_midi(msg)

            # encoder 4
            if encoder_name == push2_python.constants.ENCODER_TRACK4_ENCODER:
                def update_encoder_value(increment):
                    updated_filter_value = int(x_air['v1'] + increment)
                    if updated_filter_value < 0:
                        x_air['v1'] = 0
                    elif updated_filter_value > max_encoder_value:
                        x_air['v1'] = max_encoder_value
                    else:
                        x_air['v1'] = updated_filter_value

                update_encoder_value(increment)
                # msg = mido.Message('control_change', control=24, value=controls['master_lpf'])
                # self.app.send_midi(msg)

            # encoder 5
            if encoder_name == push2_python.constants.ENCODER_TRACK5_ENCODER:
                def update_encoder_value(increment):
                    updated_filter_value = int(x_air['v2'] + increment)
                    if updated_filter_value < 0:
                        x_air['v2'] = 0
                    elif updated_filter_value > max_encoder_value:
                        x_air['v2'] = max_encoder_value
                    else:
                        x_air['v2'] = updated_filter_value

                update_encoder_value(increment)
                # msg = mido.Message('control_change', control=25, value=controls['fx'])
                # self.app.send_midi(msg)

            # encoder 6
            if encoder_name == push2_python.constants.ENCODER_TRACK6_ENCODER:
                def update_encoder_value(increment):
                    updated_filter_value = int(x_air['bt'] + increment)
                    if updated_filter_value < 0:
                        x_air['bt'] = 0
                    elif updated_filter_value > max_encoder_value:
                        x_air['bt'] = max_encoder_value
                    else:
                        x_air['bt'] = updated_filter_value

                update_encoder_value(increment)
                # msg = mido.Message('control_change', control=26, value=controls['smile'])
                # self.app.send_midi(msg)

            # encoder 7
            if encoder_name == push2_python.constants.ENCODER_TRACK7_ENCODER:
                def update_encoder_value(increment):
                    updated_filter_value = int(x_air['reverb'] + increment)
                    if updated_filter_value < 0:
                        x_air['reverb'] = 0
                    elif updated_filter_value > max_encoder_value:
                        x_air['reverb'] = max_encoder_value
                    else:
                        x_air['reverb'] = updated_filter_value

                update_encoder_value(increment)
                # msg = mido.Message('control_change', control=27, value=controls['reverb'])
                # self.app.send_midi(msg)

            # encoder 8
            if encoder_name == push2_python.constants.ENCODER_TRACK8_ENCODER:
                def update_encoder_value(increment):
                    updated_filter_value = int(x_air['delay'] + increment)
                    if updated_filter_value < 0:
                        x_air['delay'] = 0
                    elif updated_filter_value > max_encoder_value:
                        x_air['delay'] = max_encoder_value
                    else:
                        x_air['delay'] = updated_filter_value

                update_encoder_value(increment)
                # msg = mido.Message('control_change', control=28, value=controls['tape'])
                # self.app.send_midi(msg)


    def on_button_pressed(self, button_name):
        if self.current_mix_page == 0:  # Playmode
            # if button_name == push2_python.constants.BUTTON_SETUP:
            #     self.app.toggle_and_rotate_settings_mode()
            #     self.app.buttons_need_update = True
            #
            # if button_name == push2_python.constants.BUTTON_DEVICE:
            #     self.app.toggle_and_rotate_play_mode()
            #     self.app.buttons_need_update = True
            #
            # if button_name == push2_python.constants.BUTTON_MIX:
            #     self.app.toggle_and_rotate_mix_mode()
            #     self.app.buttons_need_update = True

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
                # msg = mido.Message('control_change', control=101, value=transport['cue1'])
                # self.app.send_midi(msg)

            # PRESSED LOW button 2
            if button_name == push2_python.constants.BUTTON_LOWER_ROW_2:
                self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_2, definitions.BLACK)
                if mute_value_list['trm'] == 127:
                    mute_value_list['trm'] = 0
                elif mute_value_list['trm'] == 0:
                    mute_value_list['trm'] = 127
                # msg = mido.Message('control_change', control=102, value=transport['cue2'])
                # self.app.send_midi(msg)

            # # PRESSED LOW button 3
            # if button_name == push2_python.constants.BUTTON_LOWER_ROW_3:
            #     self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_3, definitions.BLACK)
            #     transport['bar1'] = 127
            #     msg = mido.Message('control_change', control=103, value=transport['bar1'])
            #     self.app.send_midi(msg)
            #
            # # PRESSED LOW button 4
            # if button_name == push2_python.constants.BUTTON_LOWER_ROW_4:
            #     self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_4, definitions.BLACK)
            #     transport['bar2'] = 127
            #     msg = mido.Message('control_change', control=104, value=transport['bar2'])
            #     self.app.send_midi(msg)
            #
            # # PRESSED LOW button 5
            # if button_name == push2_python.constants.BUTTON_LOWER_ROW_5:
            #     self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_5, definitions.BLACK)
            #     transport['beat1'] = 127
            #     msg = mido.Message('control_change', control=105, value=transport['beat1'])
            #     self.app.send_midi(msg)
            #
            # # PRESSED LOW button 6
            # if button_name == push2_python.constants.BUTTON_LOWER_ROW_6:
            #     self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_6, definitions.BLACK)
            #     transport['beat2'] = 127
            #     msg = mido.Message('control_change', control=106, value=transport['beat2'])
            #     self.app.send_midi(msg)
            #
            # # PRESSED LOW button 7
            # if button_name == push2_python.constants.BUTTON_LOWER_ROW_7:
            #     self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_7, definitions.BLACK)
            #     transport['nudge1'] = 127
            #     msg = mido.Message('control_change', control=107, value=transport['nudge1'])
            #     self.app.send_midi(msg)
            #
            # # PRESSED LOW button 8
            # if button_name == push2_python.constants.BUTTON_LOWER_ROW_8:
            #     self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_8, definitions.BLACK)
            #     transport['nudge2'] = 127
            #     msg = mido.Message('control_change', control=108, value=transport['nudge2'])
            #     self.app.send_midi(msg)

    def on_button_released(self, button_name):
        if self.current_mix_page == 0:  # Performance settings
            # RELEASED UPP button 2
            if button_name == push2_python.constants.BUTTON_UPPER_ROW_2:
                self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_2, definitions.YELLOW)

            # RELEASED UPP button 4
            if button_name == push2_python.constants.BUTTON_UPPER_ROW_4:
                self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_4, definitions.GREEN)

            # RELEASED UPP button 5
            if button_name == push2_python.constants.BUTTON_UPPER_ROW_5:
                self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_5, definitions.CYAN)

            # RELEASED UPP button 6
            if button_name == push2_python.constants.BUTTON_UPPER_ROW_6:
                self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_6, definitions.PINK)

            # RELEASED UPP button 7
            if button_name == push2_python.constants.BUTTON_UPPER_ROW_7:
                self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_7, definitions.CYAN)

            # RELEASED UPP button 8
            if button_name == push2_python.constants.BUTTON_UPPER_ROW_8:
                self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_8, definitions.RED)

            # RELEASED LOW button 1
            if button_name == push2_python.constants.BUTTON_LOWER_ROW_1:
                self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_1, definitions.WHITE)

            # RELEASED LOW button 2
            if button_name == push2_python.constants.BUTTON_LOWER_ROW_2:
                self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_2, definitions.WHITE)

            # RELEASED LOW button 3
            if button_name == push2_python.constants.BUTTON_LOWER_ROW_3:
                self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_3, definitions.YELLOW)

            # RELEASED LOW button 4
            if button_name == push2_python.constants.BUTTON_LOWER_ROW_4:
                self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_4, definitions.YELLOW)

            # RELEASED LOW button 5
            if button_name == push2_python.constants.BUTTON_LOWER_ROW_5:
                self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_5, definitions.ORANGE)

            # RELEASED LOW button 6
            if button_name == push2_python.constants.BUTTON_LOWER_ROW_6:
                self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_6, definitions.ORANGE)

            # RELEASED LOW button 7
            if button_name == push2_python.constants.BUTTON_LOWER_ROW_7:
                self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_7, definitions.PINK)

            # RELEASED LOW button 8
            if button_name == push2_python.constants.BUTTON_LOWER_ROW_8:
                self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_8, definitions.PINK)
