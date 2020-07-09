import definitions
import push2_python

# from pyramidi_mode import MIDICCControl

# TOGGLE_DISPLAY_BUTTON = push2_python.constants.BUTTON_USER
# SETTINGS_BUTTON = push2_python.constants.BUTTON_SETUP
# MELODIC_RHYTHMIC_TOGGLE_BUTTON = push2_python.constants.BUTTON_NOTE


class MainControlsMode(definitions.PyshaMode):

    def activate(self):
        self.update_buttons()

    # def deactivate(self):
    #     self.push.buttons.set_button_color(MELODIC_RHYTHMIC_TOGGLE_BUTTON, definitions.BLACK)
    #     self.push.buttons.set_button_color(TOGGLE_DISPLAY_BUTTON, definitions.BLACK)
    #     self.push.buttons.set_button_color(SETTINGS_BUTTON, definitions.BLACK)

    # def update_buttons(self):
    #     # self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_1, definitions.ROOT_KEY)
    #     # self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_2, definitions.ORANGE)
    #     # self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_3, definitions.BLACK)
    #     # self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_4, definitions.PURPLE)
    #     # self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_5, definitions.YELLOW)
    #     # self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_6, definitions.SURF)
    #     # self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_7, definitions.CYAN)
    #     # self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_8, definitions.RED)
    #     #
    #     # self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_1, definitions.WHITE)
    #     # self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_2, definitions.WHITE)
    #     # self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_3, definitions.YELLOW)
    #     # self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_4, definitions.YELLOW)
    #     # self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_5, definitions.ORANGE)
    #     # self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_6, definitions.ORANGE)
    #     # self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_7, definitions.PINK)
    #     # self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_8, definitions.PINK)
    #     #
    #     # self.push.buttons.set_button_color(push2_python.constants.BUTTON_PLAY, definitions.PINK)
    #     # self.push.buttons.set_button_color(push2_python.constants.BUTTON_RECORD, definitions.YELLOW)

        # Note button, to toggle melodic/rhythmic mode
        # self.push.buttons.set_button_color(MELODIC_RHYTHMIC_TOGGLE_BUTTON, definitions.WHITE)

        # # Mute button, to toggle display on/off
        # if self.app.use_push2_display:
        #     self.push.buttons.set_button_color(TOGGLE_DISPLAY_BUTTON, definitions.WHITE)
        # else:
        #     self.push.buttons.set_button_color(TOGGLE_DISPLAY_BUTTON, definitions.OFF_BTN_COLOR)
        #
        # # Settings button, to toggle settings mode
        # if self.app.is_mode_active(self.app.settings_mode):
        #     self.push.buttons.set_button_color(SETTINGS_BUTTON, definitions.WHITE, animation='pulsing')
        # else:
        #     self.push.buttons.set_button_color(SETTINGS_BUTTON, definitions.OFF_BTN_COLOR)

    # def on_button_pressed(self, button_name):
    #     # if button_name == MELODIC_RHYTHMIC_TOGGLE_BUTTON:
    #     #     self.app.toggle_melodic_rhythmic_modes()
    #     #     self.app.pads_need_update = True
    #     #     self.app.buttons_need_update = True
    #     if button_name == SETTINGS_BUTTON:
    #         self.app.toggle_and_rotate_settings_mode()
    #         self.app.buttons_need_update = True
    #     elif button_name == TOGGLE_DISPLAY_BUTTON:
    #         self.app.use_push2_display = not self.app.use_push2_display
    #         if not self.app.use_push2_display:
    #             self.push.display.send_to_display(self.push.display.prepare_frame(self.push.display.make_black_frame()))
    #         self.app.buttons_need_update = True




