import mido
import push2_python

import definitions
from definitions import PyshaMode, LAYOUT_INSTRUMENT, PYRAMIDI_CHANNEL

# TODO: this shoud be loaded from some definition file(s)

synth_midi_control_cc_data = {
    'MASTER': [
        {
            'controls': [('1', 21),
                         ('2', 22),
                         ('3', 23),
                         ('4', 24),
                         ('5', 25),
                         ('6', 26),
                         ('7', 27),
                         ('8', 28)],
        }
    ]
}

class MIDICCControl(object):
    color = definitions.GRAY_LIGHT
    color_rgb = None
    name = 'Unknown'
    cc_number = 10
    value = 64
    vmin = 0
    vmax = 127
    send_midi_func = None

    def __init__(self, cc_number, name, send_midi_func):
        self.cc_number = cc_number
        self.name = name
        self.send_midi_func = send_midi_func

        if self.name == '1': # INSTRUMENT
            self.value = 0

        if self.name == '2': # INSTRUMENT FILTER
            self.value = 127

            # @push2_python.on_button_released(push2_python.constants.BUTTON_UPPER_ROW_2)
            # def function(push):
            #     self.value = 127
            #     msg = mido.Message('control_change', control=self.cc_number, value=self.value)
            #     self.send_midi_func(msg)

        if self.name == '4':
            self.value = 0

        if self.name == '5': # MASTER FILTER
            self.value = 0

        if self.name == '6': # SMILE
            self.value = 0

        if self.name == '7': # REVERB
            self.value = 0

        if self.name == '8': # TAPE
            self.value = 127

    def update_value(self, increment):
        if self.value + increment > self.vmax:
            self.value = self.vmax
        elif self.value + increment < self.vmin:
            self.value = self.vmin
        else:
            self.value += increment

        msg = mido.Message('control_change', control=self.cc_number, value=self.value)
        self.send_midi_func(msg)

##########################################################################################################
##########################################################################################################
# "Track selector mode"

class PyramidiMode(PyshaMode):
    tracks_info = []
    selected_pyramid_track = 0
    pyramidi_channel = PYRAMIDI_CHANNEL

    synth_midi_control_ccs = {}
    active_midi_control_ccs = []

    def initialize(self, settings=None):

        for synth_name, data in synth_midi_control_cc_data.items():
            self.synth_midi_control_ccs[synth_name] = []
            for section in data:
                for name, cc_number in section['controls']:
                    control = MIDICCControl(cc_number, name, self.app.send_midi)
                    self.synth_midi_control_ccs[synth_name].append(control)

        self.select_pyramid_track(self.selected_pyramid_track)

    def get_current_track_instrument_short_name(self):
        return 'MASTER'

    def get_current_track_color(self):
        return definitions.ROOT_KEY

    def get_current_track_color_rgb(self):
        return definitions.get_color_rgb_float(self.get_current_track_color())

    def load_current_default_layout(self):
        return LAYOUT_INSTRUMENT

    def clean_currently_notes_being_played(self):
        if self.app.is_mode_active(self.app.melodic_mode):
            self.app.melodic_mode.remove_all_notes_being_played()
        elif self.app.is_mode_active(self.app.rhyhtmic_mode):
            self.app.rhyhtmic_mode.remove_all_notes_being_played()

    def select_pyramid_track(self, track_idx):
        self.selected_pyramid_track = track_idx
        self.load_current_default_layout()
        self.clean_currently_notes_being_played()
        self.active_midi_control_ccs = self.synth_midi_control_ccs.get(self.get_current_track_instrument_short_name(),
                                                                       [])
    # def activate(self):
    #     self.update_buttons()

##################################################################################
############################        BUTTONS        ###############################
##################################################################################
    def on_button_pressed(self, button_name):

###################################################################
# NOTE:
# Color is managed in the "main_controls_mode"
#
#
########################## UPPER ROW PRESSED ###
# PRESSED UPP button 1
        # if button_name == push2_python.constants.BUTTON_UPPER_ROW_1:
        #     self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_1, definitions.WHITE)
        #     if definitions.ROOT_KEY == definitions.PINK:
        #         definitions.LAYOUT_INSTRUMENT = 'lmelodic'
        #         self.app.set_melodic_mode()
        #         self.app.pads_need_update = True
        #         self.update_pads()
        #
        #     if definitions.ROOT_KEY == definitions.GREEN:
        #         LAYOUT_INSTRUMENT = 'lmelodic'
        #         self.app.set_melodic_mode()
        #         self.app.pads_need_update = True
        #         self.update_pads()
        #
        #     if definitions.ROOT_KEY == definitions.PURPLE:
        #         LAYOUT_INSTRUMENT = 'lrhytmic'
        #         self.app.set_rhythmic_mode()
        #         self.app.pads_need_update = True
        #         self.update_pads()

# PRESSED UPP button 2
#         if button_name == push2_python.constants.BUTTON_UPPER_ROW_2:

# PRESSED UPP button 3
#         if button_name == push2_python.constants.BUTTON_UPPER_ROW_3:

# PRESSED UPP button 4
#         if button_name == push2_python.constants.BUTTON_UPPER_ROW_4:

# PRESSED UPP button 5
#         if button_name == push2_python.constants.BUTTON_UPPER_ROW_5:

# PRESSED UPP button 6
#         if button_name == push2_python.constants.BUTTON_UPPER_ROW_6:

# PRESSED UPP button 7
#         if button_name == push2_python.constants.BUTTON_UPPER_ROW_7:

# PRESSED UPP button 8
#         if button_name == push2_python.constants.BUTTON_UPPER_ROW_8:


########################## LOWER ROW PRESSED ###
# PRESSED LOW button 1
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_1:
            msg = mido.Message('control_change', control=101, value=127)
            self.app.send_midi(msg)

# PRESSED LOW button 2
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_2:
            msg = mido.Message('control_change', control=102, value=127)
            self.app.send_midi(msg)

# PRESSED LOW button 3
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_3:
            msg = mido.Message('control_change', control=103, value=127)
            self.app.send_midi(msg)

# PRESSED LOW button 4
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_4:
            msg = mido.Message('control_change', control=104, value=127)
            self.app.send_midi(msg)

# PRESSED LOW button 5
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_5:
            msg = mido.Message('control_change', control=105, value=127)
            self.app.send_midi(msg)

# PRESSED LOW button 6
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_6:
            msg = mido.Message('control_change', control=106, value=127)
            self.app.send_midi(msg)

# PRESSED LOW button 7
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_7:
            msg = mido.Message('control_change', control=107, value=127)
            self.app.send_midi(msg)

# PRESSED LOW button 8
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_8:
            msg = mido.Message('control_change', control=108, value=127)
            self.app.send_midi(msg)

# PRESSED button play
        if button_name == push2_python.constants.BUTTON_PLAY:
            msg = mido.Message('control_change', control=109, value=127)
            self.app.send_midi(msg)

# PRESSED button record
        if button_name == push2_python.constants.BUTTON_RECORD:
            msg = mido.Message('control_change', control=100, value=127)
            self.app.send_midi(msg)

    def on_button_released(self, button_name):


########################## UPPER ROW RELEASED ###
# RELEASED UPP button 1
#         if button_name == push2_python.constants.BUTTON_UPPER_ROW_1:

# RELEASED UPP button 2
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_2:
            msg = mido.Message('control_change', control=22, value=127)
            self.app.send_midi(msg)

# RELEASED UPP button 3
#         if button_name == push2_python.constants.BUTTON_UPPER_ROW_3:

# RELEASED UPP button 4
#         if button_name == push2_python.constants.BUTTON_UPPER_ROW_4:

# RELEASED UPP button 5
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_5:
            msg = mido.Message('control_change', control=25, value=127)
            self.app.send_midi(msg)

# RELEASED UPP button 6
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_6:
            msg = mido.Message('control_change', control=26, value=127)
            self.app.send_midi(msg)

# RELEASED UPP button 7
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_7:
            msg = mido.Message('control_change', control=27, value=0)
            self.app.send_midi(msg)

# RELEASED UPP button 8
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_8:
            msg = mido.Message('control_change', control=28, value=127)
            self.app.send_midi(msg)

########################## LOWER ROW RELEASED ###

# RELEASED LOW button 1
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_1:
            msg = mido.Message('control_change', control=101, value=0)
            self.app.send_midi(msg)

# RELEASED LOW button 2
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_2:
            msg = mido.Message('control_change', control=102, value=0)
            self.app.send_midi(msg)

# RELEASED LOW button 3
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_3:
            msg = mido.Message('control_change', control=103, value=0)
            self.app.send_midi(msg)

# RELEASED LOW button 4
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_4:
            msg = mido.Message('control_change', control=104, value=0)
            self.app.send_midi(msg)

# RELEASED LOW button 5
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_5:
            msg = mido.Message('control_change', control=105, value=0)
            self.app.send_midi(msg)

# RELEASED LOW button 6
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_6:
            msg = mido.Message('control_change', control=106, value=0)
            self.app.send_midi(msg)

# RELEASED LOW button 7
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_7:
            msg = mido.Message('control_change', control=107, value=0)
            self.app.send_midi(msg)

# RELEASED LOW button 8
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_8:
            msg = mido.Message('control_change', control=108, value=0)
            self.app.send_midi(msg)

# RELEASED button play
        if button_name == push2_python.constants.BUTTON_PLAY:
            msg = mido.Message('control_change', control=109, value=0)
            self.app.send_midi(msg)

# RELEASED button record
        if button_name == push2_python.constants.BUTTON_RECORD:
            msg = mido.Message('control_change', control=100, value=0)
            self.app.send_midi(msg)

    def on_encoder_rotated(self, encoder_name, increment):
        if encoder_name == push2_python.constants.ENCODER_TEMPO_ENCODER:
            pass

        if encoder_name == push2_python.constants.ENCODER_SWING_ENCODER:
            pass

        if encoder_name == push2_python.constants.ENCODER_MASTER_ENCODER:
            pass

        else:
            encoder_num = [
                push2_python.constants.ENCODER_TRACK1_ENCODER,
                push2_python.constants.ENCODER_TRACK2_ENCODER,
                push2_python.constants.ENCODER_TRACK3_ENCODER,
                push2_python.constants.ENCODER_TRACK4_ENCODER,
                push2_python.constants.ENCODER_TRACK5_ENCODER,
                push2_python.constants.ENCODER_TRACK6_ENCODER,
                push2_python.constants.ENCODER_TRACK7_ENCODER,
                push2_python.constants.ENCODER_TRACK8_ENCODER,
            ].index(encoder_name)
            if self.active_midi_control_ccs:
                self.active_midi_control_ccs[encoder_num].update_value(increment)
