import definitions
import mido
import push2_python
import time
import math

from definitions import PyshaMode, OFF_BTN_COLOR, LAYOUT_MELODIC, LAYOUT_RHYTHMIC, PYRAMIDI_CHANNEL
from display_utils import draw_text_at, show_title, show_value


# TODO: this shoud be loaded from some definition file(s)
synth_midi_control_cc_data = {
    'Rhodes': [
        {
            'section': 'INSTRUMENT',
            'controls': [('Selection:', 1),
        },{
            'section': 'FILTER',
            'controls': [('Frequency', 127),
        },{
            'section': ' - ',
            'controls': [(' - ', 0),
                            (' - ', 0),
                            (' - ', 0)],
        },{
            'section': 'FX',
            'controls': [('Smile', 0),
                            ('Reverb', 0),
                            ('Tapestop', 127)],
        }
    ]
}

class MIDICCControl(object):

    color = definitions.GRAY_LIGHT
    color_rgb = None
    name = 'Unknown'
    section = 'unknown'
    cc_number = 10
    value = 64
    vmin = 0
    vmax = 127
    get_color_func = None
    send_midi_func = None

    def __init__(self, cc_number, name, section_name, get_color_func, send_midi_func):
        self.cc_number = cc_number
        self.name = name
        self.section = section_name
        self.get_color_func = get_color_func
        self.send_midi_func = send_midi_func

    def draw(self, ctx, x, y):
        color = self.get_color_func()
        show_title(ctx, x, y, '{0} - {1}'.format(self.name, self.section), color=definitions.get_color_rgb_float(definitions.WHITE))
        show_value(ctx, x, y+30, self.value, color=color)

        radius = 25
        start_rad = 130 * (math.pi / 180)
        end_rad = 50 * (math.pi / 180)
        xc = x + radius + 3
        yc = y - 70

        def get_rad_for_value(value):
            total_degrees = 280
            # TODO: include vmin here to make it more generic
            return start_rad + total_degrees * (value/self.vmax)  * (math.pi / 180)

        # This is needed to prevent showing line from previous position
        ctx.set_source_rgb(0, 0, 0)
        ctx.stroke()

        # Inner circle
        ctx.arc(xc, yc, radius, start_rad, end_rad)
        ctx.set_source_rgb(*definitions.get_color_rgb_float(definitions.GRAY_LIGHT))
        ctx.set_line_width(1)
        ctx.stroke()

        # Outer circle
        ctx.arc(xc, yc, radius, start_rad, get_rad_for_value(self.value))
        ctx.set_source_rgb(*color)
        ctx.set_line_width(3)
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


class PyramidiMode(PyshaMode):

    tracks_info = []
    pyramid_track_button_names_a = [
        push2_python.constants.BUTTON_LOWER_ROW_1,
        push2_python.constants.BUTTON_LOWER_ROW_2,
        push2_python.constants.BUTTON_LOWER_ROW_3,
        push2_python.constants.BUTTON_LOWER_ROW_4,
        push2_python.constants.BUTTON_LOWER_ROW_5,
        push2_python.constants.BUTTON_LOWER_ROW_6,
        push2_python.constants.BUTTON_LOWER_ROW_7,
        push2_python.constants.BUTTON_LOWER_ROW_8
    ]
    pyramid_track_selection_button_a = False
    selected_pyramid_track = 0

    def initialize(self, settings=None):
        # TODO: tracks info could be loaed from some json file, including extra stuff like main MIDI CCs, etc
        for i in range(0, 64):
            data = {
                'track_name': '{0}{1}'.format((i % 16) + 1, ['A', 'B', 'C', 'D'][i//16]),
                'instrument_name': '-',
                'instrument_short_name': '-',
                'color': 'my_dark_gray',
                'color_rgb': [26/255, 26/255, 26/255],
            }
            if i % 8 == 0:
                data['instrument_name'] = 'Rhodes'
                data['instrument_short_name'] = 'Rhodes'
                data['color'] = 'pink'
                data['color_rgb'] = [255/255, 64/255, 64/255]
            elif i % 8 == 1:
                data['instrument_name'] = 'Synth'
                data['instrument_short_name'] = 'Synth'
                data['color'] = 'turquoise'
                data['color_rgb'] = [0/255, 255/255, 255/255]
            elif i % 8 == 2:
                data['instrument_name'] = 'Sampler'
                data['instrument_short_name'] = 'Sampler'
                data['color'] = 'purple'
                data['color_rgb'] = [255/255, 0/255, 255/255]
            self.tracks_info.append(data)

    def get_current_track_color(self):
        return self.tracks_info[self.selected_pyramid_track]['color']

    def get_current_track_color_rgb(self):
        return self.tracks_info[self.selected_pyramid_track]['color_rgb']

    def activate(self):
        self.update_buttons()

    def deactivate(self):
        for button_name in self.pyramid_track_button_names_a:
            self.push.buttons.set_button_color(button_name, 'black')

    def update_buttons(self):
        for count, name in enumerate(self.pyramid_track_button_names_a):
            color = self.tracks_info[count]['color']
            self.push.buttons.set_button_color(name, color)

    def update_display(self, ctx, w, h):

        # Divide display in 8 parts to show different settings
        part_w = w // 8
        part_h = h

        # Draw track selector labels
        for i in range(0, 8):
            part_x = i * part_w
            if self.selected_pyramid_track % 8 == i:
                rectangle_color = self.tracks_info[i]['color_rgb']
                font_color = [1, 1, 1]
            else:
                rectangle_color = [0, 0, 0]
                font_color = self.tracks_info[i]['color_rgb']
            rectangle_height = 20
            ctx.set_source_rgb(*rectangle_color)
            ctx.rectangle(part_x, part_h - rectangle_height, w, part_h)
            ctx.fill()
            instrument_short_name = self.tracks_info[i]['instrument_short_name']
            draw_text_at(ctx, part_x + 3, part_h - 4, instrument_short_name, font_size=15, color=font_color)

        # Draw main track info
        font_color = self.get_current_track_color_rgb()
        rectangle_color = [0, 0, 0]
        rectangle_height_width = (h - 20 - 20)/1.5
        ctx.set_source_rgb(*rectangle_color)
        x = 0
        y = (h - rectangle_height_width)/2 - 10
        font_size = 30
        #ctx.rectangle(x, y, rectangle_height_width, rectangle_height_width)
        #ctx.fill()
        draw_text_at(ctx, x + 3, y + 50, '{0}'.format(self.tracks_info[self.selected_pyramid_track]['instrument_name']), font_size=font_size, color=font_color)


    def on_button_pressed(self, button_name):
        if button_name in self.pyramid_track_button_names_a:
            self.selected_pyramid_track = self.pyramid_track_button_names_a.index(button_name)
            self.pyramid_track_selection_button_a = False
            self.app.buttons_need_update = True
            self.app.pads_need_update = True
