import definitions
import mido
import push2_python
import time
import math

from definitions import PyshaMode, OFF_BTN_COLOR, LAYOUT_MELODIC, LAYOUT_RHYTHMIC, LAYOUT_INSTRUMENT, PYRAMIDI_CHANNEL
from display_utils import draw_text_at, show_title, show_value

# TODO: this shoud be loaded from some definition file(s)
synth_midi_control_cc_data = {
    'MASTER': [
        {
            'section': 'MASTER CONTROLS',
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
    # section = 'unknown'
    cc_number = 10
    value = 64
    vmin = 0
    vmax = 127
    get_color_func = None
    send_midi_func = None



    # def __init__(self, cc_number, name, section_name, get_color_func, send_midi_func):
    def __init__(self, cc_number, name, get_color_func, send_midi_func):
        self.cc_number = cc_number
        self.name = name
        # self.section = section_name
        self.get_color_func = get_color_func
        self.send_midi_func = send_midi_func

        if self.name == 'INSTRUMENT':
            self.value = 0

        if self.name == 'FILTER':
            self.value = 127

            @push2_python.on_button_released(push2_python.constants.BUTTON_UPPER_ROW_2)
            def function(push):
                self.value = 127
                msg = mido.Message('control_change', control=self.cc_number, value=self.value)
                self.send_midi_func(msg)

        if self.name == 'FX':
            self.value = 127
            @push2_python.on_button_released(push2_python.constants.BUTTON_UPPER_ROW_4)
            def function(push):
                self.value = 127
                msg = mido.Message('control_change', control=self.cc_number, value=self.value)
                self.send_midi_func(msg)

        if self.name == 'SMILE':
            self.value = 0
            @push2_python.on_button_released(push2_python.constants.BUTTON_UPPER_ROW_5)
            def function(push):
                self.value = 0
                msg = mido.Message('control_change', control=self.cc_number, value=self.value)
                self.send_midi_func(msg)

        if self.name == 'DELAY':
            self.value = 0
            @push2_python.on_button_released(push2_python.constants.BUTTON_UPPER_ROW_6)
            def function(push):
                self.value = 0
                msg = mido.Message('control_change', control=self.cc_number, value=self.value)
                self.send_midi_func(msg)

        if self.name == 'REVERB':
            self.value = 0
            @push2_python.on_button_released(push2_python.constants.BUTTON_UPPER_ROW_7)
            def function(push):
                self.value = 0
                msg = mido.Message('control_change', control=self.cc_number, value=self.value)
                self.send_midi_func(msg)

        if self.name == 'TAPE':
            self.value = 127
            @push2_python.on_button_released(push2_python.constants.BUTTON_UPPER_ROW_8)
            def function(push):
                self.value = 127
                msg = mido.Message('control_change', control=self.cc_number, value=self.value)
                self.send_midi_func(msg)



    def draw(self, ctx, x, y):
        color = self.get_color_func()
        if self.name == '':
            show_title(ctx, x, y, self.name, color=(0, 0, 0))
            show_value(ctx, x, y + 10, self.value, color=(0, 0, 0))
        elif self.name == 'INSTRUMENT':
            if self.value < 43:
                show_title(ctx, x, y, self.name, color=definitions.get_color_rgb_float(definitions.PINK))
                show_value(ctx, x, y + 10, self.value, color=definitions.get_color_rgb_float(definitions.PINK))
            if self.value > 42 and self.value < 83:
                show_title(ctx, x, y, self.name, color=definitions.get_color_rgb_float(definitions.GREEN))
                show_value(ctx, x, y + 10, self.value, color=definitions.get_color_rgb_float(definitions.GREEN))
            if self.value > 82:
                show_title(ctx, x, y, self.name, color=definitions.get_color_rgb_float(definitions.PURPLE))
                show_value(ctx, x, y + 10, self.value, color=definitions.get_color_rgb_float(definitions.PURPLE))
        elif self.name == 'FILTER':
            show_title(ctx, x, y, self.name, color=definitions.get_color_rgb_float(definitions.ORANGE))
            show_value(ctx, x, y + 10, self.value, color=definitions.get_color_rgb_float(definitions.ORANGE))
        elif self.name == 'FX':
            show_title(ctx, x, y, self.name, color=definitions.get_color_rgb_float(definitions.PURPLE))
            show_value(ctx, x, y + 10, self.value, color=definitions.get_color_rgb_float(definitions.PURPLE))
        elif self.name == 'SMILE':
            show_title(ctx, x, y, self.name, color=definitions.get_color_rgb_float(definitions.YELLOW))
            show_value(ctx, x, y + 10, self.value, color=definitions.get_color_rgb_float(definitions.YELLOW))
        elif self.name == 'DELAY':
            show_title(ctx, x, y, self.name, color=definitions.get_color_rgb_float(definitions.GREEN))
            show_value(ctx, x, y + 10, self.value, color=definitions.get_color_rgb_float(definitions.GREEN))
        elif self.name == 'REVERB':
            show_title(ctx, x, y, self.name, color=definitions.get_color_rgb_float(definitions.CYAN))
            show_value(ctx, x, y + 10, self.value, color=definitions.get_color_rgb_float(definitions.CYAN))
        elif self.name == 'TAPE':
            show_title(ctx, x, y, self.name, color=definitions.get_color_rgb_float(definitions.RED))
            show_value(ctx, x, y + 10, self.value, color=definitions.get_color_rgb_float(definitions.RED))
        else:
            show_value(ctx, x, y+10, self.value, color=definitions.get_color_rgb_float(definitions.GRAY_LIGHT))

        radius = 22
        start_rad = 90 * (math.pi / 180)
        end_rad = 360# * (math.pi / 180)
        xc = x + radius + 32
        yc = y - 64

        def get_rad_for_value(value):
            total_degrees = 360
            # TODO: include vmin here to make it more generic
            return start_rad + total_degrees * (value/self.vmax)  * (math.pi / 180)

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
                #     definitions.LAYOUT_INSTRUMENT = 'lmelodic'


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
        else:
            ctx.set_source_rgb(*definitions.get_color_rgb_float(definitions.GRAY_DARK))
        ctx.set_line_width(43)
        ctx.stroke()

# Outer circle
        ctx.arc(xc, yc, radius, start_rad, get_rad_for_value(self.value))
        if self.name == '':
            ctx.set_source_rgb(0, 0, 0)
        elif self.name == 'INSTRUMENT':
            pass
        elif self.name == 'FILTER':
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
        else:
            ctx.set_source_rgb(*definitions.get_color_rgb_float(definitions.GRAY_LIGHT))

        ctx.set_line_width(44)
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




# TODO: ##########################################################################################################
# TODO: ##########################################################################################################
# TODO: ##########################################################################################################


class PyramidiMode(PyshaMode):

    tracks_info = []
    # pyramid_track_names = [
    #     track_name_1,
    #     track_name_2,
    #     track_name_3,
    #     track_name_4,
    #     track_name_5,
    #     track_name_6,
    #     track_name_7,
    #     track_name_8
    # ]
    # pyramid_track_button_names_a = [
    #     push2_python.constants.BUTTON_LOWER_ROW_1,
    #     push2_python.constants.BUTTON_LOWER_ROW_2,
    #     push2_python.constants.BUTTON_LOWER_ROW_3,
    #     push2_python.constants.BUTTON_LOWER_ROW_4,
    #     push2_python.constants.BUTTON_LOWER_ROW_5,
    #     push2_python.constants.BUTTON_LOWER_ROW_6,
    #     push2_python.constants.BUTTON_LOWER_ROW_7,
    #     push2_python.constants.BUTTON_LOWER_ROW_8
    # ]
    # pyramid_track_button_names_b = [
    #     push2_python.constants.BUTTON_1_32T,
    #     push2_python.constants.BUTTON_1_32,
    #     push2_python.constants.BUTTON_1_16T,
    #     push2_python.constants.BUTTON_1_16,
    #     push2_python.constants.BUTTON_1_8T,
    #     push2_python.constants.BUTTON_1_8,
    #     push2_python.constants.BUTTON_1_4T,
    #     push2_python.constants.BUTTON_1_4
    # ]
    # pyramid_track_selection_button_a = False
    # pyramid_track_selection_button_a_pressing_time = 0
    selected_pyramid_track = 0
    # pyramid_track_selection_quick_press_time = 0.100
    pyramidi_channel = PYRAMIDI_CHANNEL

    synth_midi_control_ccs = {}
    active_midi_control_ccs = []

    def initialize(self, settings=None):
        # TODO: tracks info could be loaed from some json file, including extra stuff like main MIDI CCs, etc
        # for i in range(0, 64):
        for i in range(0, 1):
            data = {
                'instrument_short_name': 'MASTER',
                'color': definitions.ROOT_KEY,
                'default_layout': definitions.LAYOUT_INSTRUMENT,
            }
            self.tracks_info.append(data)


        for synth_name, data in synth_midi_control_cc_data.items():
            self.synth_midi_control_ccs[synth_name] = []
            for section in data:
                section_name = section['section']
                for name, cc_number in section['controls']:
                    # control = MIDICCControl(cc_number, name, section_name, self.get_current_track_color_rgb, self.app.send_midi)
                    control = MIDICCControl(cc_number, name, self.get_current_track_color_rgb, self.app.send_midi)
                    self.synth_midi_control_ccs[synth_name].append(control)

        self.select_pyramid_track(self.selected_pyramid_track)


    def get_current_track_instrument_short_name(self):
        return self.tracks_info[self.selected_pyramid_track]['instrument_short_name']

    def get_current_track_color(self):
        # return self.tracks_info[self.selected_pyramid_track]['color']
        return definitions.ROOT_KEY

    def get_current_track_color_rgb(self):
        return definitions.get_color_rgb_float(self.get_current_track_color())

    def load_current_default_layout(self):
        if self.tracks_info[self.selected_pyramid_track]['default_layout'] == LAYOUT_MELODIC:
            self.app.set_melodic_mode()
        elif self.tracks_info[self.selected_pyramid_track]['default_layout'] == LAYOUT_RHYTHMIC:
            self.app.set_rhythmic_mode()

    def clean_currently_notes_being_played(self):
        if self.app.is_mode_active(self.app.melodic_mode):
            self.app.melodic_mode.remove_all_notes_being_played()
        elif self.app.is_mode_active(self.app.rhyhtmic_mode):
            self.app.rhyhtmic_mode.remove_all_notes_being_played()

    def send_select_track_to_pyramid(self, track_idx):
        # Follows pyramidi specification (Pyramid configured to receive on ch 16)
        msg = mido.Message('control_change', control=0, value=track_idx + 1)
        self.app.send_midi(msg, force_channel=self.pyramidi_channel)

    def select_pyramid_track(self, track_idx):
        self.selected_pyramid_track = track_idx
        self.send_select_track_to_pyramid(self.selected_pyramid_track)
        self.load_current_default_layout()
        self.clean_currently_notes_being_played()
        self.active_midi_control_ccs = self.synth_midi_control_ccs.get(self.get_current_track_instrument_short_name(), [])

    def activate(self):
        self.update_buttons()

    def deactivate(self):
        # for button_name in self.pyramid_track_button_names_a + self.pyramid_track_button_names_b:
        for button_name in self.pyramid_track_button_names_a:
            self.push.buttons.set_button_color(button_name, 'black')

    # def update_buttons(self):
    #     for count, name in enumerate(self.pyramid_track_button_names_a):
    #         color = self.tracks_info[count]['color']
    #         self.push.buttons.set_button_color(name, color)

        # # for count, name in enumerate(self.pyramid_track_button_names_b):
        #     if self.pyramid_track_selection_button_a:
        #         equivalent_track_num = self.pyramid_track_button_names_a.index(self.pyramid_track_selection_button_a) + count * 8
        #         if self.selected_pyramid_track == equivalent_track_num:
        #             self.push.buttons.set_button_color(name, 'green', animation='pulsing')
        #         else:
        #             color = self.tracks_info[self.pyramid_track_button_names_a.index(self.pyramid_track_selection_button_a)]['color']
        #             self.push.buttons.set_button_color(name, color)
        #     else:
        #         self.push.buttons.set_button_color(name, 'black')

    def update_display(self, ctx, w, h):

        # Divide display in 8 parts to show different settings
        part_w = w // 8
        part_h = h

        if self.active_midi_control_ccs:
            # Draw midi contorl ccs
            for i in range(0, min(len(self.active_midi_control_ccs), 8)):
                part_x = i * part_w
                self.active_midi_control_ccs[i].draw(ctx, part_x, part_h)
        else:
            pass
            # # Draw track info
            # font_color = [1, 1, 1]
            # rectangle_color = [0, 0, 0]
            # rectangle_height_width = (h - 20 - 20)/1.5
            # ctx.set_source_rgb(*rectangle_color)
            # x = 0
            # y = (h - rectangle_height_width)/2 - 10
            # font_size = 30
            # #ctx.rectangle(x, y, rectangle_height_width, rectangle_height_width)
            # #ctx.fill()
            # # draw_text_at(ctx, x + 3, y + 50, '{1} {0}'.format(self.tracks_info[self.selected_pyramid_track]['instrument_name'],
            # #                                                     self.tracks_info[self.selected_pyramid_track]['track_name']), font_size=font_size, color=font_color)
            # draw_text_at(ctx, x + 3, y + 50, (self.tracks_info[self.selected_pyramid_track]['instrument_name']), font_size=font_size, color=font_color)

        # # Draw track selector labels
        # for i in range(0, 8):
        #     part_x = i * part_w
        #     if self.selected_pyramid_track % 8 == i:
        #         rectangle_color = definitions.get_color_rgb_float(self.tracks_info[i]['color'])
        #         font_color = [1, 1, 1]
        #     else:
        #         rectangle_color = [0, 0, 0]
        #         font_color = definitions.get_color_rgb_float(self.tracks_info[i]['color'])
        #     rectangle_height = 20
        #     ctx.set_source_rgb(*rectangle_color)
        #     ctx.rectangle(part_x, part_h - rectangle_height, w, part_h)
        #     ctx.fill()
        #     instrument_short_name = self.tracks_info[i]['instrument_short_name']
        #     draw_text_at(ctx, part_x + 3, part_h - 4, instrument_short_name, font_size=15, color=font_color)
        font_size = 12

        part_x = 1
        draw_text_at(ctx, part_x + 40, part_h - 4, 'CUE', font_size, color=[1, 1, 1])

        part_x = 2
        draw_text_at(ctx, part_x + 160, part_h - 4, 'CUE', font_size, color=[1, 1, 1])

        part_x = 3
        draw_text_at(ctx, part_x + 280, part_h - 4, 'BAR', font_size, color=[1, 1, 0])

        part_x = 4
        draw_text_at(ctx, part_x + 400, part_h - 4, 'BAR', font_size, color=[1, 1, 0])

        part_x = 5
        draw_text_at(ctx, part_x + 515, part_h - 4, 'BEAT', font_size, color=[1, 0.4, 0])

        part_x = 6
        draw_text_at(ctx, part_x + 635, part_h - 4, 'BEAT', font_size, color=[1, 0.4, 0])

        part_x = 7
        draw_text_at(ctx, part_x + 745, part_h - 4, 'NUDGE', font_size, color=[1, 0.4, 0.6])

        part_x = 8
        draw_text_at(ctx, part_x + 865, part_h - 4, 'NUDGE', font_size, color=[1, 0.4, 0.6])

##################################################################################
############################ SWITCH INSTRUMENTS!!! ###############################
##################################################################################
    def on_button_pressed(self, button_name):
        if button_name == push2_python.constants.BUTTON_UPPER_ROW_1:
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_1, definitions.WHITE)
            if definitions.ROOT_KEY == definitions.PINK:
                definitions.LAYOUT_INSTRUMENT = 'lmelodic'
                self.app.set_melodic_mode()
                # self.app.buttons_need_update = True
                self.app.pads_need_update = True
                self.update_pads()
                # msg = mido.Message('control_change', control=21, value=64)
                # self.app.send_midi(msg)
                # self.update_buttons()

            if definitions.ROOT_KEY == definitions.GREEN:
                definitions.LAYOUT_INSTRUMENT = 'lmelodic'
                self.app.set_melodic_mode()
                # self.app.buttons_need_update = True
                self.app.pads_need_update = True
                self.update_pads()
                # self.update_buttons()

            if definitions.ROOT_KEY == definitions.PURPLE:
                definitions.LAYOUT_INSTRUMENT = 'lrhytmic'
                self.app.set_rhythmic_mode()
                # self.app.buttons_need_update = True
                self.app.pads_need_update = True
                self.update_pads()
                # self.update_buttons()

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

        # if button_name == push2_python.constants.BUTTON_RECORD:
        #     self.push.buttons.set_button_color(push2_python.constants.BUTTON_UPPER_ROW_1, definitions.WHITE)
        #     msg = mido.Message('control_change', control=110, value=127)
        #     self.app.send_midi(msg)


    def on_button_released(self, button_name):

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
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_LOWER_ROW_7, definitions.PINK)

        if button_name == push2_python.constants.BUTTON_PLAY:
            msg = mido.Message('control_change', control=109, value=0)
            self.app.send_midi(msg)
            self.push.buttons.set_button_color(push2_python.constants.BUTTON_PLAY, definitions.PINK)






        # if button_name == push2_python.constants.BUTTON_PLAY:
        #     msg = mido.Message('control_change', control=109, value=0)
        #     self.app.send_midi(msg)

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
