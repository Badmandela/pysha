from definitions import PyshaMode


class PyramidiMode(PyshaMode):
    # tracks_info = []
    selected_pyramid_track = 0

    # value = 64
    # vmin = 0
    # vmax = 127
    # send_midi_func = None

    # synth_midi_control_ccs = {}
    # active_midi_control_ccs = []

    def initialize(self, settings=None):

        self.select_pyramid_track(self.selected_pyramid_track)

    # # noinspection PyMethodMayBeStatic
    # def load_default_layout(self):
    #     return LAYOUT_INSTRUMENT

    # def clean_currently_notes_being_played(self):
    #     if self.app.is_mode_active(self.app.melodic_mode):
    #         self.app.melodic_mode.remove_all_notes_being_played()
    #     elif self.app.is_mode_active(self.app.rhyhtmic_mode):
    #         self.app.rhyhtmic_mode.remove_all_notes_being_played()

    def select_pyramid_track(self, track_idx):
        self.selected_pyramid_track = track_idx
        # self.load_default_layout()
        # self.clean_currently_notes_being_played()
