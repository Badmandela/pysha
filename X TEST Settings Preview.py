import cairo
import push2_python

from display_utils import show_title, show_value, draw_title

# class SettingsMode(definitions.PyshaMode):
current_page = 0
n_pages = 1
encoders_state = {}
is_running_sw_update = False

w, h = push2_python.constants.DISPLAY_LINE_PIXELS, push2_python.constants.DISPLAY_N_LINES
surface = cairo.ImageSurface(cairo.FORMAT_RGB16_565, w, h)
ctx = cairo.Context(surface)

part_w = w // 8
part_h = h

for i in range(0, 8):
    part_x = i * part_w
    part_y = 0

ctx.set_source_rgb(0, 0, 0)  # Draw black background


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 1
title = "ROOT NOTE:"
center_x = 60
color = [1, 0.25, 0.5]
draw_title(ctx, center_x, title, *color)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 2
title = "OCTAVE:"
center_x = 180
color = [1, 0.25, 0.5]
draw_title(ctx, center_x, title, *color)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 3
center_x = 300


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 4
center_x = 420
title = "MIDI OUT:"
color = [1, 0.1, 1]
draw_title(ctx, center_x, title, *color)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 5
center_x = 540

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 6
center_x = 660
title = "RESET MIDI:"
color = [1, 1, 1]
draw_title(ctx, center_x, title, *color)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 7
center_x = 780
title = "REBOOT:"
color = [1, 0.1, 0.1]
draw_title(ctx, center_x, title, *color)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 8
center_x = 900
title = "SAVE:"
color = [0.1, 1, 0.1]
draw_title(ctx, center_x, title, *color)



if current_page == 0:  # Performance settings

    if i == 0:  # Root note
        if not self.app.is_mode_active(self.app.melodic_mode):
            color = definitions.get_color_rgb_float(definitions.FONT_COLOR_DISABLED)
        # show_title(ctx, part_x, h, 'ROOT NOTE')
        show_title(ctx, part_x, h, "ROOT NOTE")
        show_value(ctx, part_x, h, "{0} ({1})".format(self.app.melodic_mode.note_number_to_name(
            self.app.melodic_mode.root_midi_note), self.app.melodic_mode.root_midi_note), color)

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

        # if 'iConnectAUDIO2+ USB1' in name:
        #     name = 'iCA2 USB1'
        #     color = definitions.get_color_rgb_float(definitions.GREEN)
        #
        # if 'iConnectAUDIO2+ DIN' in name:
        #     name = 'iCA2 DIN'
        #     color = definitions.get_color_rgb_float(definitions.RED)

        show_title(ctx, part_x, h, 'OUT DEVICE')
        show_value(ctx, part_x, h, name, color)

    elif i == 5:  # MIDI out channel
        if self.app.midi_out is None:
            color = definitions.get_color_rgb_float(definitions.FONT_COLOR_DISABLED)
        show_title(ctx, part_x, h, 'OUT CH')
        show_value(ctx, part_x, h, self.app.midi_out_channel + 1, color)

    elif i == 6:  # Re-send MIDI connection established (to push, not MIDI in/out device)
        show_title(ctx, part_x, h, 'RESET MIDI')


    # elif i == 7:  # definitions.VERSION info
    #     show_title(ctx, part_x, h, 'SAVE')
    #     #show_value(ctx, part_x, h, 'Niklas Pysha ' + definitions.VERSION, color)

# End of drawing code

surface.write_to_png('settings.png')