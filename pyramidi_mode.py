import mido
import push2_python

import definitions
from definitions import PyshaMode, LAYOUT_INSTRUMENT

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

        if self.name == '1':  # INSTRUMENT
            self.value = 0    # Starting value

        if self.name == '2':  # INSTRUMENT FILTER
            self.value = 127  # Starting value

        if self.name == '4':  # MASTER FILTER
            self.value = 127  # Starting value

        if self.name == '5':  # FX
            self.value = 127  # Starting value

        if self.name == '6':  # SMILE
            self.value = 0  # Starting value

        if self.name == '7':  # REVERB
            self.value = 0  # Starting value

        if self.name == '8':  # TAPE
            self.value = 127  # Starting value

    def update_value(self, increment):
        if self.value + increment > self.vmax:
            self.value = self.vmax
        elif self.value + increment < self.vmin:
            self.value = self.vmin
        else:
            self.value += increment

        msg = mido.Message('control_change', control=self.cc_number, value=self.value)
        self.send_midi_func(msg)


class PyramidiMode(PyshaMode):
    tracks_info = []
    selected_pyramid_track = 0

    value = 64
    vmin = 0
    vmax = 127
    send_midi_func = None

    synth_midi_control_ccs = {}
    active_midi_control_ccs = []

    def initialize(self, settings=None):

        for synth_name, data in synth_midi_control_cc_data.items():                 # Comment
            self.synth_midi_control_ccs[synth_name] = []                            # Comment
            for section in data:                                                    # Comment
                for name, cc_number in section['controls']:                         # Comment
                    control = MIDICCControl(cc_number, name, self.app.send_midi)
                    self.synth_midi_control_ccs[synth_name].append(control)

        self.select_pyramid_track(self.selected_pyramid_track)

    def get_current_track_instrument_short_name(self):                              # Comment
        return 'MASTER'                                                             # Comment

    def load_default_layout(self):
        return LAYOUT_INSTRUMENT

    def clean_currently_notes_being_played(self):
        if self.app.is_mode_active(self.app.melodic_mode):
            self.app.melodic_mode.remove_all_notes_being_played()
        elif self.app.is_mode_active(self.app.rhyhtmic_mode):
            self.app.rhyhtmic_mode.remove_all_notes_being_played()

    def select_pyramid_track(self, track_idx):
        self.selected_pyramid_track = track_idx
        self.load_default_layout()
        self.clean_currently_notes_being_played()
        self.active_midi_control_ccs = self.synth_midi_control_ccs.get(self.get_current_track_instrument_short_name(),
                                                                       [])

    def activate(self):
        self.update_buttons()

    def on_button_pressed(self, button_name):

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_1:        # Trigger Cue 1
            msg = mido.Message('control_change', control=101, value=127)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_2:        # Trigger Cue 2
            msg = mido.Message('control_change', control=102, value=127)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_3:        # Trigger Bar 1
            msg = mido.Message('control_change', control=103, value=127)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_4:        # Trigger Bar 2
            msg = mido.Message('control_change', control=104, value=127)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_5:        # Trigger Beat 1
            msg = mido.Message('control_change', control=105, value=127)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_6:        # Trigger Beat 2
            msg = mido.Message('control_change', control=106, value=127)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_7:        # Trigger Nudge 1
            msg = mido.Message('control_change', control=107, value=127)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_8:        # Trigger Nudge 2
            msg = mido.Message('control_change', control=108, value=127)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_PLAY:               # Trigger Next song
            msg = mido.Message('control_change', control=109, value=127)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_RECORD:             # Trigger Loop
            msg = mido.Message('control_change', control=100, value=127)
            self.app.send_midi(msg)

    def on_button_released(self, button_name):

        if button_name == push2_python.constants.BUTTON_UPPER_ROW_2:        # Reset Instrument filter
            msg = mido.Message('control_change', control=22, value=127)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_UPPER_ROW_4:        # Reset Master filter
            msg = mido.Message('control_change', control=24, value=127)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_UPPER_ROW_5:        # Reset FX
            msg = mido.Message('control_change', control=25, value=127)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_UPPER_ROW_6:        # Reset Smile
            msg = mido.Message('control_change', control=26, value=127)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_UPPER_ROW_7:        # Reset Reverb
            msg = mido.Message('control_change', control=27, value=0)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_UPPER_ROW_8:        # Reset Tape
            msg = mido.Message('control_change', control=28, value=127)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_1:        # Reset Cue 1
            msg = mido.Message('control_change', control=101, value=0)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_2:        # Reset Cue 2
            msg = mido.Message('control_change', control=102, value=0)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_3:        # Reset Bar 1
            msg = mido.Message('control_change', control=103, value=0)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_4:        # Reset Bar 2
            msg = mido.Message('control_change', control=104, value=0)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_5:        # Reset Beat 1
            msg = mido.Message('control_change', control=105, value=0)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_6:        # Reset Beat 2
            msg = mido.Message('control_change', control=106, value=0)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_7:        # Reset Nudge 1
            msg = mido.Message('control_change', control=107, value=0)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_8:        # Reset Nudge 2
            msg = mido.Message('control_change', control=108, value=0)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_PLAY:               # Reset Next song
            msg = mido.Message('control_change', control=109, value=0)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_RECORD:             # Reset Loop
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
