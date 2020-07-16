VERSION = '0.2'

PYRAMIDI_CHANNEL = 15

DELAYED_ACTIONS_APPLY_TIME = 1.0  # Encoder changes won't be applied until this time has passed since last moved

# LAYOUT_MELODIC = 'lmelodic'
# LAYOUT_RHYTHMIC = 'lrhytmic'
# LAYOUT_INSTRUMENT = 'lmelodic'

BLACK_RGB = [0, 0, 0]
GRAY_DARK_RGB = [30, 30, 30]
GRAY_LIGHT_RGB = [180, 180, 180]
WHITE_RGB = [255, 255, 255]
YELLOW_RGB = [255, 241, 0]
ORANGE_RGB = [255, 90, 0]
RED_RGB = [255, 32, 32]
PINK_RGB = [255, 64, 128]
PURPLE_RGB = [104, 33, 122]
CYAN_RGB = [0, 188, 242]
GREEN_RGB = [0, 158, 73]
SURF_RGB = [0, 200, 100]

CRASH_COLOR_RGB = [128, 32, 64]
TOM_1_COLOR_RGB = [64, 32, 32]
TOM_2_COLOR_RGB = [64, 32, 32]
KICK_DRUM_COLOR_RGB = [255, 128, 96]
OPEN_HIHAT_COLOR_RGB = [96, 192, 255]
CLOSED_HIHAT_COLOR_RGB = [40, 120, 200]
STICK_COLOR_RGB = [64, 64, 32]
SNARE_COLOR_RGB = [255, 255, 128]

S1_RGB = [32, 4, 32]
S2_RGB = [64, 8, 64]
S3_RGB = [96, 12, 96]
S4_RGB = [128, 32, 128]
S5_RGB = [160, 40, 160]
S6_RGB = [192, 80, 192]
S7_RGB = [224, 96, 224]
S8_RGB = [255, 128, 255]

BLACK = 'black'
GRAY_DARK = 'gray_dark'
GRAY_LIGHT = 'gray_light'
WHITE = 'white'
YELLOW = 'yellow'
ORANGE = 'orange'
RED = 'red'
PINK = 'pink'
PURPLE = 'purple'
CYAN = 'cyan'
GREEN = 'green'
SURF = 'surf'

CRASH_COLOR = 'crash_color'
TOM_1_COLOR = 'tom_1_color'
TOM_2_COLOR = 'tom_2_color'
KICK_DRUM_COLOR = 'kick_drum_color'
OPEN_HIHAT_COLOR = 'open_hihat_color'
CLOSED_HIHAT_COLOR = 'closed_hihat_color'
STICK_COLOR = 'stick_color'
SNARE_COLOR = 'snare_color'

S1 = 'S1'
S2 = 'S2'
S3 = 'S3'
S4 = 'S4'
S5 = 'S5'
S6 = 'S6'
S7 = 'S7'
S8 = 'S8'

COLORS_NAMES = [BLACK, GRAY_DARK, GRAY_LIGHT, WHITE, YELLOW, ORANGE, RED, PINK, PURPLE, CYAN, GREEN, SURF,
                CRASH_COLOR, TOM_1_COLOR, TOM_2_COLOR, KICK_DRUM_COLOR, OPEN_HIHAT_COLOR, CLOSED_HIHAT_COLOR,
                STICK_COLOR, SNARE_COLOR,
                S1, S2, S3, S4, S5, S6, S7, S8]


def get_color_rgb(color_name):
    return globals().get('{0}_RGB'.format(color_name.upper()), [0, 0, 0])


def get_color_rgb_float(color_name):
    return [x / 255 for x in get_color_rgb(color_name)]


FONT_COLOR_DELAYED_ACTIONS = ORANGE
FONT_COLOR_DISABLED = GRAY_LIGHT
OFF_BTN_COLOR = BLACK
NOTE_ON_COLOR = GREEN
WHITE_KEY = GRAY_DARK
BLACK_KEY = BLACK
ROOT_KEY = PINK


class PyshaMode(object):
    """
    """

    name = ''

    def __init__(self, app, settings=None):
        self.app = app
        self.initialize(settings=settings)

    @property
    def push(self):
        return self.app.push

    # Method run only once when the mode object is created, may receive settings dictionary from main app
    def initialize(self, settings=None):
        pass

    # Method to return a dictionary of properties to store in a settings file, and that will be passed to
    # initialize method when object created
    def get_settings_to_save(self):
        return {}

    # Methods that are run before the mode is activated and when it is deactivated
    def activate(self):
        pass

    def deactivate(self):
        pass

    # Method called every iteration in the main loop to see if any actions need to be done at the end of the iteration
    # This is used to avoid some actions unncessesarily being repeated many times
    def check_for_delayed_actions(self):
        pass

    # Method called when MIDI messages arrive from Pysha MIDI input
    def on_midi_in(self, msg):
        pass

    # Push2 update methods
    def update_pads(self) -> object:
        pass

    def update_buttons(self):
        pass

    def update_display(self, ctx, w, h):
        pass

    # Push2 action callbacks
    def on_encoder_rotated(self, encoder_name, increment):
        pass

    def on_button_pressed(self, button_name):
        pass

    def on_button_released(self, button_name):
        pass

    def on_pad_pressed(self, pad_n, pad_ij, velocity):
        pass

    def on_pad_released(self, pad_n, pad_ij, velocity):
        pass

    def on_pad_aftertouch(self, pad_n, pad_ij, velocity):
        pass

    def on_touchstrip(self, value):
        pass

    def on_sustain_pedal(self, sustain_on):
        pass
