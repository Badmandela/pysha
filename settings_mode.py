import time

import push2_python.constants

import definitions
from display_utils import show_title, show_value


class SettingsMode(definitions.PyshaMode):
    # Pad settings
    # - Root note
    # - Aftertouch mode
    # - Velocity curve
    # - Channel aftertouch range

    # MIDI settings
    # - Midi device IN
    # - Midi channel IN
    # - Midi device OUT
    # - Midi channel OUT
    # - Rerun MIDI initial configuration

    # About panel
    # - definitions.VERSION info
    # - Save current settings
    #  - FPS

    current_page = 0
    n_pages = 1
    encoders_state = {}
    is_running_sw_update = False

    def move_to_next_page(self):
        self.app.buttons_need_update = True
        self.current_page += 1
        if self.current_page >= self.n_pages:
            self.current_page = 0
            return True  # Return true because page rotation finished 
        return False

    def initialize(self, settings=None):
        current_time = time.time()
        for encoder_name in self.push.encoders.available_names:
            self.encoders_state[encoder_name] = {
                'last_message_received': current_time,
            }

    def activate(self):
        self.current_page = 0
        self.update_buttons()

    def deactivate(self):
        self.set_all_upper_row_buttons_off()

    def check_for_delayed_actions(self):
        current_time = time.time()
        if self.app.midi_in_tmp_device_idx is not None:
            # Means we are in the process of changing the MIDI in device
            if current_time - self.encoders_state[push2_python.constants.ENCODER_TRACK1_ENCODER]['last_message_received'] > definitions.DELAYED_ACTIONS_APPLY_TIME:
                self.app.set_midi_in_device_by_index(self.app.midi_in_tmp_device_idx)
                self.app.midi_in_tmp_device_idx = None
        if self.app.midi_out_tmp_device_idx is not None:
            # Means we are in the process of changing the MIDI in device
            if current_time - self.encoders_state[push2_python.constants.ENCODER_TRACK3_ENCODER]['last_message_received'] > definitions.DELAYED_ACTIONS_APPLY_TIME:
                self.app.set_midi_out_device_by_index(self.app.midi_out_tmp_device_idx)
                self.app.midi_out_tmp_device_idx = None

    def set_all_upper_row_buttons_off(self):
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_1, definitions.OFF_BTN_COLOR)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_2, definitions.OFF_BTN_COLOR)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_3, definitions.OFF_BTN_COLOR)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_4, definitions.OFF_BTN_COLOR)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_5, definitions.OFF_BTN_COLOR)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_6, definitions.OFF_BTN_COLOR)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_7, definitions.OFF_BTN_COLOR)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_8, definitions.OFF_BTN_COLOR)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_LEFT, definitions.OFF_BTN_COLOR)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UP, definitions.OFF_BTN_COLOR)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_RIGHT, definitions.OFF_BTN_COLOR)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_DOWN, definitions.OFF_BTN_COLOR)

    def update_buttons(self):
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_1, definitions.WHITE)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_2, definitions.OFF_BTN_COLOR)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_3, definitions.WHITE)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_4, definitions.WHITE)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_5, definitions.WHITE)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_6, definitions.WHITE)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_7, definitions.WHITE)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_8, definitions.OFF_BTN_COLOR)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_LEFT, definitions.WHITE)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_UP, definitions.WHITE)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_RIGHT, definitions.WHITE)
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_DOWN, definitions.WHITE)


    def update_display(self, ctx, w, h):

        # Divide display in 8 parts to show different settings
        part_w = w // 8
        part_h = h

        # Draw labels and values
        for i in range(0, 8):
            part_x = i * part_w
            part_y = 0

            ctx.set_source_rgb(0, 0, 0)  # Draw black background
            ctx.rectangle(part_x - 3, part_y, w, h)  # do x -3 to add some margin between parts
            ctx.fill()

            color = [1.0, 1.0, 1.0]

            if self.current_page == 0:  # Performance settings

                if i == 0:  # Root note
                    if not self.app.is_mode_active(self.app.melodic_mode):
                        color = definitions.get_color_rgb_float(definitions.FONT_COLOR_DISABLED)
                    # show_title(ctx, part_x, h, 'ROOT NOTE')
                    show_title(ctx, part_x, h, "ROOT NOTE")
                    show_value(ctx, part_x, h, "{0} ({1})".format(self.app.melodic_mode.note_number_to_name(
                        self.app.melodic_mode.root_midi_note), self.app.melodic_mode.root_midi_note), color)

                elif i == 2:  # MIDI in device
                    if self.app.midi_in_tmp_device_idx is not None:
                        color = definitions.get_color_rgb_float(definitions.FONT_COLOR_DELAYED_ACTIONS)
                        if self.app.midi_in_tmp_device_idx < 0:
                            name = "None"
                        else:
                            name = "{0} {1}".format(self.app.midi_in_tmp_device_idx + 1,
                                                    self.app.available_midi_in_device_names[
                                                        self.app.midi_in_tmp_device_idx])
                    else:
                        if self.app.midi_in is not None:
                            name = "{0} {1}".format(
                                self.app.available_midi_in_device_names.index(self.app.midi_in.name) + 1,
                                self.app.midi_in.name)
                        else:
                            color = definitions.get_color_rgb_float(definitions.FONT_COLOR_DISABLED)
                            name = "None"
                    show_title(ctx, part_x, h, 'IN DEVICE')
                    show_value(ctx, part_x, h, name, color)

                elif i == 3:  # MIDI in channel
                    if self.app.midi_in is None:
                        color = definitions.get_color_rgb_float(definitions.FONT_COLOR_DISABLED)
                    show_title(ctx, part_x, h, 'IN CH')
                    show_value(ctx, part_x, h, self.app.midi_in_channel + 1 if self.app.midi_in_channel > -1 else "All",
                               color)

                elif i == 4:  # MIDI out device
                    if self.app.midi_out_tmp_device_idx is not None:
                        color = definitions.get_color_rgb_float(definitions.FONT_COLOR_DELAYED_ACTIONS)
                        if self.app.midi_out_tmp_device_idx < 0:
                            name = "None"
                        else:
                            name = "{0} {1}".format(self.app.midi_out_tmp_device_idx + 1,
                                                    self.app.available_midi_out_device_names[
                                                        self.app.midi_out_tmp_device_idx])

                    else:
                        if self.app.midi_out is not None:
                            name = "{0} {1}".format(
                                self.app.available_midi_out_device_names.index(self.app.midi_out.name) + 1,
                                self.app.midi_out.name)
                        else:
                            color = definitions.get_color_rgb_float(definitions.FONT_COLOR_DISABLED)
                            name = "None"

                    if 'iConnectAUDIO2+ USB1' in name:
                        name = 'iCA2 USB1'
                        color = definitions.get_color_rgb_float(definitions.GREEN)

                    if 'iConnectAUDIO2+ DIN' in name:
                        name = 'iCA2 DIN'
                        color = definitions.get_color_rgb_float(definitions.RED)

                    show_title(ctx, part_x, h, 'OUT DEVICE')
                    show_value(ctx, part_x, h, name, color)

                elif i == 5:  # MIDI out channel
                    if self.app.midi_out is None:
                        color = definitions.get_color_rgb_float(definitions.FONT_COLOR_DISABLED)
                    show_title(ctx, part_x, h, 'OUT CH')
                    show_value(ctx, part_x, h, self.app.midi_out_channel + 1, color)

                elif i == 6:  # Re-send MIDI connection established (to push, not MIDI in/out device)
                    show_title(ctx, part_x, h, 'RESET MIDI')


                elif i == 7:  # definitions.VERSION info
                    show_title(ctx, part_x, h, 'VERSION')
                    show_value(ctx, part_x, h, 'Niklas Pysha ' + definitions.VERSION, color)




    def on_encoder_rotated(self, encoder_name, increment):

        self.encoders_state[encoder_name]['last_message_received'] = time.time()

        if self.current_page == 0:  # Performance settings
            if encoder_name == push2_python.constants.ENCODER_TRACK1_ENCODER:
                self.app.melodic_mode.set_root_midi_note(self.app.melodic_mode.root_midi_note + increment)
                # Using async update method because we don't really need immediate response here
                self.app.pads_need_update = True

            if encoder_name == push2_python.constants.ENCODER_TRACK3_ENCODER:
                if self.app.midi_in_tmp_device_idx is None:
                    if self.app.midi_in is not None:
                        self.app.midi_in_tmp_device_idx = self.app.available_midi_in_device_names.index(
                            self.app.midi_in.name)
                    else:
                        self.app.midi_in_tmp_device_idx = -1
                self.app.midi_in_tmp_device_idx += increment
                if self.app.midi_in_tmp_device_idx >= len(self.app.available_midi_in_device_names):
                    self.app.midi_in_tmp_device_idx = len(self.app.available_midi_in_device_names) - 1
                elif self.app.midi_in_tmp_device_idx < -1:
                    self.app.midi_in_tmp_device_idx = -1  # Will use -1 for "None"

            elif encoder_name == push2_python.constants.ENCODER_TRACK4_ENCODER:
                self.app.set_midi_in_channel(self.app.midi_in_channel + increment, wrap=False)

            elif encoder_name == push2_python.constants.ENCODER_TRACK5_ENCODER:
                if self.app.midi_out_tmp_device_idx is None:
                    if self.app.midi_out is not None:
                        self.app.midi_out_tmp_device_idx = self.app.available_midi_out_device_names.index(
                            self.app.midi_out.name)
                    else:
                        self.app.midi_out_tmp_device_idx = -1
                self.app.midi_out_tmp_device_idx += increment
                if self.app.midi_out_tmp_device_idx >= len(self.app.available_midi_out_device_names):
                    self.app.midi_out_tmp_device_idx = len(self.app.available_midi_out_device_names) - 1
                elif self.app.midi_out_tmp_device_idx < -1:
                    self.app.midi_out_tmp_device_idx = -1  # Will use -1 for "None"

            elif encoder_name == push2_python.constants.ENCODER_TRACK6_ENCODER:
                self.app.set_midi_out_channel(self.app.midi_out_channel + increment, wrap=False)

        else:
            pass

    def on_button_pressed(self, button_name):

        if self.current_page == 0:  # Performance settings
            if button_name == push2_python.constants.BUTTON_UPPER_ROW_1:
                self.app.melodic_mode.set_root_midi_note(48)
                self.app.pads_need_update = True

            elif button_name == push2_python.constants.BUTTON_LEFT:
                self.app.melodic_mode.set_root_midi_note(self.app.melodic_mode.root_midi_note - 1)
                self.app.pads_need_update = True

            elif button_name == push2_python.constants.BUTTON_RIGHT:
                self.app.melodic_mode.set_root_midi_note(self.app.melodic_mode.root_midi_note + 1)
                self.app.pads_need_update = True

            elif button_name == push2_python.constants.BUTTON_UP:
                self.app.melodic_mode.set_root_midi_note(self.app.melodic_mode.root_midi_note + 12)
                self.app.pads_need_update = True

            elif button_name == push2_python.constants.BUTTON_DOWN:
                self.app.melodic_mode.set_root_midi_note(self.app.melodic_mode.root_midi_note - 12)
                self.app.pads_need_update = True

            elif button_name == push2_python.constants.BUTTON_UPPER_ROW_3:
                if self.app.midi_in_tmp_device_idx is None:
                    if self.app.midi_in is not None:
                        self.app.midi_in_tmp_device_idx = self.app.available_midi_in_device_names.index(
                            self.app.midi_in.name)
                    else:
                        self.app.midi_in_tmp_device_idx = -1
                self.app.midi_in_tmp_device_idx += 1
                # Make index position wrap
                if self.app.midi_in_tmp_device_idx >= len(self.app.available_midi_in_device_names):
                    self.app.midi_in_tmp_device_idx = -1  # Will use -1 for "None"
                elif self.app.midi_in_tmp_device_idx < -1:
                    self.app.midi_in_tmp_device_idx = len(self.app.available_midi_in_device_names) - 1

            elif button_name == push2_python.constants.BUTTON_UPPER_ROW_4:
                self.app.set_midi_in_channel(self.app.midi_in_channel + 1, wrap=True)

            elif button_name == push2_python.constants.BUTTON_UPPER_ROW_5:
                if self.app.midi_out_tmp_device_idx is None:
                    if self.app.midi_out is not None:
                        self.app.midi_out_tmp_device_idx = self.app.available_midi_out_device_names.index(
                            self.app.midi_out.name)
                    else:
                        self.app.midi_out_tmp_device_idx = -1
                self.app.midi_out_tmp_device_idx += 1
                # Make index position wrap
                if self.app.midi_out_tmp_device_idx >= len(self.app.available_midi_out_device_names):
                    self.app.midi_out_tmp_device_idx = -1  # Will use -1 for "None"
                elif self.app.midi_out_tmp_device_idx < -1:
                    self.app.midi_out_tmp_device_idx = len(self.app.available_midi_out_device_names) - 1

            elif button_name == push2_python.constants.BUTTON_UPPER_ROW_6:
                self.app.set_midi_out_channel(self.app.midi_out_channel + 1, wrap=True)

            elif button_name == push2_python.constants.BUTTON_UPPER_ROW_6:
                self.app.on_midi_push_connection_established()