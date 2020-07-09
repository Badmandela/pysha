import math

import mido
import push2_python

import definitions
from definitions import PyshaMode, LAYOUT_INSTRUMENT, PYRAMIDI_CHANNEL
from display_utils import draw_text_at, show_title, show_value

synth_midi_control_cc_data = {
    'MASTER': [
        {
            'controls': [('INSTRUMENT', 21),
                         ('FILTER', 22),
                         ('', 23),
                         ('FX', 24),
                         ('SMILE', 25),
                         ('DELAY', 26),
                         ('REVERB', 27),
                         ('TAPE', 28)],
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

        if self.name == 'INSTRUMENT':
            self.value = 0

        if self.name == 'FILTER':
            self.value = 127
            msg = mido.Message('control_change', control=self.cc_number, value=self.value)
            self.send_midi_func(msg)

            @push2_python.on_button_released(push2_python.constants.BUTTON_UPPER_ROW_2)
            def function(push):
                self.value = 127
                msg = mido.Message('control_change', control=self.cc_number, value=self.value)
                self.send_midi_func(msg)

        if self.name == 'FX':
            self.value = 127
            msg = mido.Message('control_change', control=self.cc_number, value=self.value)
            self.send_midi_func(msg)

            @push2_python.on_button_released(push2_python.constants.BUTTON_UPPER_ROW_4)
            def function(push):
                self.value = 127
                msg = mido.Message('control_change', control=self.cc_number, value=self.value)
                self.send_midi_func(msg)

        if self.name == 'SMILE':
            self.value = 0
            msg = mido.Message('control_change', control=self.cc_number, value=self.value)
            self.send_midi_func(msg)

            @push2_python.on_button_released(push2_python.constants.BUTTON_UPPER_ROW_5)
            def function(push):
                self.value = 0
                msg = mido.Message('control_change', control=self.cc_number, value=self.value)
                self.send_midi_func(msg)

        if self.name == 'DELAY':
            self.value = 0
            msg = mido.Message('control_change', control=self.cc_number, value=self.value)
            self.send_midi_func(msg)

            @push2_python.on_button_released(push2_python.constants.BUTTON_UPPER_ROW_6)
            def function(push):
                self.value = 0
                msg = mido.Message('control_change', control=self.cc_number, value=self.value)
                self.send_midi_func(msg)

        if self.name == 'REVERB':
            self.value = 0
            msg = mido.Message('control_change', control=self.cc_number, value=self.value)
            self.send_midi_func(msg)

            @push2_python.on_button_released(push2_python.constants.BUTTON_UPPER_ROW_7)
            def function(push):
                self.value = 0
                msg = mido.Message('control_change', control=self.cc_number, value=self.value)
                self.send_midi_func(msg)

        if self.name == 'TAPE':
            self.value = 127
            msg = mido.Message('control_change', control=self.cc_number, value=self.value)
            self.send_midi_func(msg)

            @push2_python.on_button_released(push2_python.constants.BUTTON_UPPER_ROW_8)
            def function(push):
                self.value = 127
                msg = mido.Message('control_change', control=self.cc_number, value=self.value)
                self.send_midi_func(msg)


########## SCREEN ##########
    def draw(self, ctx, x, y):

        # color = self.get_color_func()

        lower_button_x = x + 40
        lower_button_y = y - 4

        if self.name == 'INSTRUMENT':
            draw_text_at(ctx, lower_button_x, lower_button_y, 'CUE', font_size=11, color=[1, 1, 1])
            if self.value < 43:
                show_title(ctx, x, y, 'RHODES', color=[255, 64, 128]) #PINK
                show_value(ctx, x, y + 10, self.value, color=[255, 64, 128]) #PINK
            if self.value > 42 and self.value < 83:
                show_title(ctx, x, y, 'SYNTH', color=[0, 158, 73]) #Typ turkos...
                show_value(ctx, x, y + 10, self.value, color=[0, 158, 73]) #Typ turkos...
            if self.value > 82:
                show_title(ctx, x, y, 'SAMPLER', color=[104, 33, 122]) #PURPLE
                show_value(ctx, x, y + 10, self.value, color=[104, 33, 122]) #PURPLE
        elif self.name == 'FILTER':
            draw_text_at(ctx, lower_button_x, lower_button_y, 'CUE', font_size=11, color=[1, 1, 1])
            show_title(ctx, x, y, 'FILTER', color=definitions.get_color_rgb_float(definitions.ORANGE))
            show_value(ctx, x, y + 10, self.value, color=definitions.get_color_rgb_float(definitions.ORANGE))
        if self.name == '':
            draw_text_at(ctx, lower_button_x, lower_button_y, 'BAR', font_size=11, color=[1, 1, 0])
        elif self.name == 'FX':
            draw_text_at(ctx, lower_button_x, lower_button_y, 'BAR', font_size=11, color=[1, 1, 0])
            show_title(ctx, x, y, self.name, color=definitions.get_color_rgb_float(definitions.PURPLE))
            show_value(ctx, x, y + 10, self.value, color=definitions.get_color_rgb_float(definitions.PURPLE))
        elif self.name == 'SMILE':
            draw_text_at(ctx, lower_button_x, lower_button_y, 'BEAT', font_size=11, color=[1, 0.4, 0])
            show_title(ctx, x, y, self.name, color=definitions.get_color_rgb_float(definitions.YELLOW))
            show_value(ctx, x, y + 10, self.value, color=definitions.get_color_rgb_float(definitions.YELLOW))
        elif self.name == 'DELAY':
            draw_text_at(ctx, lower_button_x, lower_button_y, 'BEAT', font_size=11, color=[1, 0.4, 0])
            show_title(ctx, x, y, self.name, color=definitions.get_color_rgb_float(definitions.GREEN))
            show_value(ctx, x, y + 10, self.value, color=definitions.get_color_rgb_float(definitions.GREEN))
        elif self.name == 'REVERB':
            draw_text_at(ctx, lower_button_x, lower_button_y, 'NUDGE', font_size=11, color=[1, 0.4, 0.6])
            show_title(ctx, x, y, 'REVERB', color=definitions.get_color_rgb_float(definitions.CYAN))
            show_value(ctx, x, y + 10, self.value, color=definitions.get_color_rgb_float(definitions.CYAN))
        elif self.name == 'TAPE':
            draw_text_at(ctx, lower_button_x, lower_button_y, 'NUDGE', font_size=11, color=[1, 0.4, 0.6])
            show_title(ctx, x, y, self.name, color=definitions.get_color_rgb_float(definitions.RED))
            show_value(ctx, x, y + 10, self.value, color=definitions.get_color_rgb_float(definitions.RED))

        radius = 15
        start_rad = 1.6 #* (math.pi / 180)
        end_rad = 8 #* (math.pi / 180)
        xc = x + radius + 32
        yc = y - 80

        def get_rad_for_value(value):
            total_degrees = 360
            # TODO: include vmin here to make it more generic
            return start_rad + total_degrees * (value / self.vmax) * (math.pi / 180)

        # This is needed to prevent showing line from previous position
        ctx.set_source_rgb(0, 0, 0)
        ctx.stroke()

        # Inner circle
        ctx.arc(xc, yc, radius, start_rad, end_rad)

        if self.name == '':
            ctx.set_source_rgb(0, 0, 0)

        elif self.name == 'INSTRUMENT':
            if self.value < 43:
                ctx.set_source_rgb(*definitions.get_color_rgb_float(definitions.PINK))
                if not definitions.ROOT_KEY == definitions.PINK:
                    definitions.ROOT_KEY = definitions.PINK
                if not definitions.NOTE_ON_COLOR == definitions.TURQUOISE:
                    definitions.NOTE_ON_COLOR = definitions.TURQUOISE
                    # PyramidiMode.update_pads(PyramidiMode)
                    # PyramidiMode.app.pads_need_update = True
                    # self.app.pads_need_update = True
                    # PyshaMode.update_pads(PyramidiMode)
                    # PyshaMode.update_pads(MelodicMode)
                    # PyshaMode.
                    # PyshaMode.push.pads.set_pads_color(color_matrix)
                    # self.push.pads.set_pads_color(color_matrix)
                # if not LAYOUT_INSTRUMENT == 'lmelodic':
                #     LAYOUT_INSTRUMENT = 'lmelodic'

            if self.value > 42 and self.value < 83:
                ctx.set_source_rgb(*definitions.get_color_rgb_float(definitions.GREEN))
                if not definitions.ROOT_KEY == definitions.GREEN:
                    definitions.ROOT_KEY = definitions.GREEN
                if not definitions.NOTE_ON_COLOR == definitions.PINK:
                    definitions.NOTE_ON_COLOR = definitions.PINK

            if self.value > 82:
                ctx.set_source_rgb(*definitions.get_color_rgb_float(definitions.PURPLE))
                if not definitions.ROOT_KEY == definitions.PURPLE:
                    definitions.ROOT_KEY = definitions.PURPLE
                if not definitions.NOTE_ON_COLOR == definitions.WHITE:
                    definitions.NOTE_ON_COLOR = definitions.WHITE

        elif self.name == 'FILTER':
            ctx.set_source_rgb(*definitions.get_color_rgb_float(definitions.ORANGE))
        elif self.name == 'FX':
            ctx.set_source_rgb(*definitions.get_color_rgb_float(definitions.PURPLE))
        elif self.name == 'SMILE':
            ctx.set_source_rgb(*definitions.get_color_rgb_float(definitions.YELLOW_DARK))
        elif self.name == 'DELAY':
            ctx.set_source_rgb(*definitions.get_color_rgb_float(definitions.SURF_DARK))
        elif self.name == 'REVERB':
            ctx.set_source_rgb(*definitions.get_color_rgb_float(definitions.CYAN_DARK))
        elif self.name == 'TAPE':
            ctx.set_source_rgb(*definitions.get_color_rgb_float(definitions.RED))

        ctx.set_line_width(30)
        ctx.stroke()

        # Outer circle
        ctx.arc(xc, yc, radius, start_rad, get_rad_for_value(self.value))
        if self.name == 'FILTER':
            ctx.set_source_rgb(*definitions.get_color_rgb_float(definitions.ORANGE_DARK))
        elif self.name == 'FX':
            ctx.set_source_rgb(*definitions.get_color_rgb_float(definitions.PURPLE_DARK))
        elif self.name == 'SMILE':
            ctx.set_source_rgb(*definitions.get_color_rgb_float(definitions.YELLOW))
        elif self.name == 'DELAY':
            ctx.set_source_rgb(*definitions.get_color_rgb_float(definitions.SURF))
        elif self.name == 'REVERB':
            ctx.set_source_rgb(*definitions.get_color_rgb_float(definitions.CYAN))
        elif self.name == 'TAPE':
            ctx.set_source_rgb(*definitions.get_color_rgb_float(definitions.RED_DARK))

        ctx.set_line_width(30)
        ctx.stroke()

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
##########################################################################################################

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
    def activate(self):
        self.update_buttons()

    def update_display(self, ctx, w, h):

        # Divide display in 8 parts to show different settings
        part_w = w // 8
        part_h = h

        if self.active_midi_control_ccs:
            # Draw midi contorl ccs
            for i in range(0, min(len(self.active_midi_control_ccs), 8)):
                part_x = i * part_w
                self.active_midi_control_ccs[i].draw(ctx, part_x, part_h)

    ##################################################################################
    ############################        BUTTONS        ###############################
    ##################################################################################
    def on_button_pressed(self, button_name):

        ### UPPER ROW PRESSED ###
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_1:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_1, definitions.WHITE)
            if definitions.ROOT_KEY == definitions.PINK:
                LAYOUT_INSTRUMENT = 'lmelodic'
                self.app.set_melodic_mode()
                # self.app.buttons_need_update = True
                self.app.pads_need_update = True
                self.update_pads()
                # msg = mido.Message('control_change', control=21, value=64)
                # self.app.send_midi(msg)
                # self.update_buttons()

            if definitions.ROOT_KEY == definitions.GREEN:
                LAYOUT_INSTRUMENT = 'lmelodic'
                self.app.set_melodic_mode()
                self.app.pads_need_update = True
                self.update_pads()

            if definitions.ROOT_KEY == definitions.PURPLE:
                LAYOUT_INSTRUMENT = 'lrhytmic'
                self.app.set_rhythmic_mode()
                self.app.pads_need_update = True
                self.update_pads()

        if button_name == push2_python.constants.BUTTON_UPPER_ROW_2:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_2, definitions.WHITE)

        if button_name == push2_python.constants.BUTTON_UPPER_ROW_3:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_3, definitions.WHITE)

        if button_name == push2_python.constants.BUTTON_UPPER_ROW_4:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_4, definitions.WHITE)

        if button_name == push2_python.constants.BUTTON_UPPER_ROW_5:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_5, definitions.WHITE)

        if button_name == push2_python.constants.BUTTON_UPPER_ROW_6:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_6, definitions.WHITE)

        if button_name == push2_python.constants.BUTTON_UPPER_ROW_7:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_7, definitions.WHITE)

        if button_name == push2_python.constants.BUTTON_UPPER_ROW_8:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_8, definitions.WHITE)

        ### LOWER ROW PRESSED ###
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_1:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_1, definitions.WHITE)
            msg = mido.Message('control_change', control=101, value=127)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_2:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_2, definitions.WHITE)
            msg = mido.Message('control_change', control=102, value=127)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_3:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_3, definitions.WHITE)
            msg = mido.Message('control_change', control=103, value=127)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_4:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_4, definitions.WHITE)
            msg = mido.Message('control_change', control=104, value=127)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_5:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_5, definitions.WHITE)
            msg = mido.Message('control_change', control=105, value=127)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_6:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_6, definitions.WHITE)
            msg = mido.Message('control_change', control=106, value=127)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_7:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_7, definitions.WHITE)
            msg = mido.Message('control_change', control=107, value=127)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_8:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_8, definitions.WHITE)
            msg = mido.Message('control_change', control=108, value=127)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_PLAY:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_PLAY, definitions.WHITE)
            msg = mido.Message('control_change', control=109, value=127)
            self.app.send_midi(msg)

        if button_name == push2_python.constants.BUTTON_RECORD:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_1, definitions.WHITE)
            msg = mido.Message('control_change', control=100, value=127)
            self.app.send_midi(msg)

    def on_button_released(self, button_name):

        ### UPPER ROW RELEASED ###
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_1:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_1, definitions.ROOT_KEY)

        if button_name == push2_python.constants.BUTTON_UPPER_ROW_2:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_2, definitions.ORANGE)

        if button_name == push2_python.constants.BUTTON_UPPER_ROW_3:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_3, definitions.BLACK)

        if button_name == push2_python.constants.BUTTON_UPPER_ROW_4:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_4, definitions.PURPLE)

        if button_name == push2_python.constants.BUTTON_UPPER_ROW_5:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_5, definitions.YELLOW)

        if button_name == push2_python.constants.BUTTON_UPPER_ROW_6:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_6, definitions.SURF)

        if button_name == push2_python.constants.BUTTON_UPPER_ROW_7:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_7, definitions.CYAN)

        if button_name == push2_python.constants.BUTTON_UPPER_ROW_8:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_8, definitions.RED)

        ### LOWER ROW RELEASED ###
        if button_name == push2_python.constants.BUTTON_LOWER_ROW_1:
            msg = mido.Message('control_change', control=101, value=0)
            self.app.send_midi(msg)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_1, definitions.WHITE)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_2:
            msg = mido.Message('control_change', control=102, value=0)
            self.app.send_midi(msg)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_2, definitions.WHITE)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_3:
            msg = mido.Message('control_change', control=103, value=0)
            self.app.send_midi(msg)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_3, definitions.YELLOW)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_4:
            msg = mido.Message('control_change', control=104, value=0)
            self.app.send_midi(msg)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_4, definitions.YELLOW)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_5:
            msg = mido.Message('control_change', control=105, value=0)
            self.app.send_midi(msg)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_5, definitions.ORANGE)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_6:
            msg = mido.Message('control_change', control=106, value=0)
            self.app.send_midi(msg)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_6, definitions.ORANGE)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_7:
            msg = mido.Message('control_change', control=107, value=0)
            self.app.send_midi(msg)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_7, definitions.PINK)

        if button_name == push2_python.constants.BUTTON_LOWER_ROW_8:
            msg = mido.Message('control_change', control=108, value=0)
            self.app.send_midi(msg)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_8, definitions.PINK)

        if button_name == push2_python.constants.BUTTON_PLAY:
            msg = mido.Message('control_change', control=109, value=0)
            self.app.send_midi(msg)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_PLAY, definitions.PINK)

        if button_name == push2_python.constants.BUTTON_RECORD:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_1, definitions.YELLOW)
            msg = mido.Message('control_change', control=100, value=0)
            self.app.send_midi(msg)

    def on_encoder_rotated(self, encoder_name, increment):
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
