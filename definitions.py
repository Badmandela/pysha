VERSION = '0.2'

PYRAMIDI_CHANNEL = 15

DELAYED_ACTIONS_APPLY_TIME = 1.0  # Encoder changes won't be applied until this time has passed since last moved

LAYOUT_MELODIC = 'lmelodic'
LAYOUT_RHYTHMIC = 'lrhytmic'
LAYOUT_INSTRUMENT = 'lmelodic'

BLACK_RGB = [0, 0, 0]
GRAY_DARK_RGB = [30, 30, 30]
GRAY_LIGHT_RGB = [180, 180, 180]
WHITE_RGB = [255, 255, 255]
YELLOW_LIGHT_RGB = [255, 255, 128]
YELLOW_RGB = [255, 241, 0]
YELLOW_DARK_RGB = [16, 16, 0]
ORANGE_RGB = [255, 90, 0]
ORANGE_DARK_RGB = [16, 8, 1]
RED_RGB = [255, 32, 32]
RED_DARK_RGB = [17, 0, 0]
PINK_RGB = [255, 64, 128]
PINK_DARK_RGB = [16, 0, 8]
PURPLE_RGB = [104, 33, 122]
PURPLE_DARK_RGB = [8, 0, 16]
BLUE_RGB = [0, 24, 143]
CYAN_RGB = [0, 188, 242]
CYAN_DARK_RGB = [0, 8, 8]
TURQUOISE_LIGHT_RGB = [96, 230, 255]
TURQUOISE_RGB = [0, 178, 148]
TURQUOISE_DARK_RGB = [0, 8, 8]
GREEN_RGB = [0, 158, 73]
SURF_RGB = [0, 200, 100]
SURF_DARK_RGB = [0, 16, 4]
LIME_RGB = [186, 216, 10]

CRASH_COLOR_RGB = [128, 32, 64]
TOM_1_COLOR_RGB = [64, 32, 32]
TOM_2_COLOR_RGB = [64, 32, 32]
KICK_DRUM_COLOR_RGB = [255, 128, 96]
OPEN_HIHAT_COLOR_RGB = [96, 192, 255]
CLOSED_HIHAT_COLOR_RGB = [40, 120, 200]
STICK_COLOR_RGB = [64, 64, 32]
SNARE_COLOR_RGB = [255, 255, 128]

SPARKLE_1_COLOR_RGB = [32, 4, 32]
SPARKLE_2_COLOR_RGB = [64, 8, 64]
SPARKLE_3_COLOR_RGB = [96, 12, 96]
SPARKLE_4_COLOR_RGB = [128, 32, 128]
SPARKLE_5_COLOR_RGB = [160, 40, 160]
SPARKLE_6_COLOR_RGB = [192, 80, 192]
SPARKLE_7_COLOR_RGB = [224, 96, 224]
SPARKLE_8_COLOR_RGB = [255, 128, 255]

BLACK = 'black'
GRAY_DARK = 'gray_dark'
GRAY_LIGHT = 'gray_light'
WHITE = 'white'
YELLOW_LIGHT = 'yellow_light'
YELLOW = 'yellow'
YELLOW_DARK = 'yellow_dark'
ORANGE = 'orange'
ORANGE_DARK = 'orange_dark'
RED = 'red'
RED_DARK = 'red_dark'
PINK = 'pink'
PINK_DARK = 'pink_dark'
PURPLE = 'purple'
PURPLE_DARK = 'purple_dark'
BLUE = 'blue'
CYAN = 'cyan'
CYAN_DARK = 'cyan_dark'
TURQUOISE_LIGHT = 'turquoise_light'
TURQUOISE = 'turquoise'
TURQUOISE_DARK = 'turquoise_dark'
GREEN = 'green'
SURF = 'surf'
SURF_DARK = 'surf_dark'
LIME = 'lime'

CRASH_COLOR = 'crash_color'
TOM_1_COLOR = 'tom_1_color'
TOM_2_COLOR = 'tom_2_color'
KICK_DRUM_COLOR = 'kick_drum_color'
OPEN_HIHAT_COLOR = 'open_hihat_color'
CLOSED_HIHAT_COLOR = 'closed_hihat_color'
STICK_COLOR = 'stick_color'
SNARE_COLOR = 'snare_color'

SPARKLE_1_COLOR = 'sparkle_1_color'
SPARKLE_2_COLOR = 'sparkle_2_color'
SPARKLE_3_COLOR = 'sparkle_3_color'
SPARKLE_4_COLOR = 'sparkle_4_color'
SPARKLE_5_COLOR = 'sparkle_5_color'
SPARKLE_6_COLOR = 'sparkle_6_color'
SPARKLE_7_COLOR = 'sparkle_7_color'
SPARKLE_8_COLOR = 'sparkle_8_color'

COLORS_NAMES = [BLACK, GRAY_DARK, GRAY_LIGHT, WHITE, YELLOW_LIGHT, YELLOW, YELLOW_DARK, ORANGE, ORANGE_DARK, RED, RED_DARK, PINK, PINK_DARK, PURPLE, PURPLE_DARK, BLUE, CYAN, CYAN_DARK, TURQUOISE_LIGHT, TURQUOISE, TURQUOISE_DARK, GREEN, SURF, SURF_DARK, LIME, CRASH_COLOR, TOM_1_COLOR, TOM_2_COLOR, KICK_DRUM_COLOR, OPEN_HIHAT_COLOR, CLOSED_HIHAT_COLOR, STICK_COLOR, SNARE_COLOR, SPARKLE_1_COLOR, SPARKLE_2_COLOR, SPARKLE_3_COLOR, SPARKLE_4_COLOR, SPARKLE_5_COLOR, SPARKLE_6_COLOR, SPARKLE_7_COLOR, SPARKLE_8_COLOR]

def get_color_rgb(color_name):
    return globals().get('{0}_RGB'.format(color_name.upper()), [0, 0, 0])

def get_color_rgb_float(color_name):
    return [x/255 for x in get_color_rgb(color_name)]

FONT_COLOR_DELAYED_ACTIONS = ORANGE
FONT_COLOR_DISABLED = GRAY_LIGHT
OFF_BTN_COLOR = GRAY_DARK
NOTE_ON_COLOR = TURQUOISE
BLACK_KEY = GRAY_DARK
ROOT_KEY = CYAN




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

    # Method called at every iteration in the main loop to see if any actions need to be performed at the end of the iteration
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
