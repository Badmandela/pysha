import cairo

screen_black = [0, 0, 0]
screen_dark = [0.05, 0.05, 0.05]


def show_title(ctx, x, h, text, color=[1, 1, 1]):
    text = str(text)
    ctx.set_source_rgb(*color)
    ctx.select_font_face("Verdana", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    font_size = h // 12
    ctx.set_font_size(font_size)
    ctx.move_to(x + 3, 15)
    ctx.show_text(text)


def draw_title(ctx, center_x, text, *color):
    text = str(text)
    ctx.select_font_face("Ableton Sans Bold", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(15)

    # Main Text
    ctx.set_source_rgb(*color)
    ctx.move_to(center_x - (ctx.text_extents(text)[2] / 2), 17)
    ctx.show_text(text)

def draw_list(ctx, center_x, y, text, *color):
    ctx.set_font_size(10)
    # ctx.select_font_face("Unscreen", cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_NORMAL)
    ctx.select_font_face("Ableton Sans Light", cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_NORMAL)
    ctx.move_to(center_x - (ctx.text_extents(text)[2] / 2), y)
    ctx.set_source_rgba(*color)
    ctx.show_text(text)


def show_value(ctx, x, h, text, color=[1, 1, 1]):
    text = str(text)
    ctx.set_source_rgb(*color)
    ctx.select_font_face("Verdana", cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_NORMAL)
    font_size = 12
    ctx.set_font_size(font_size)
    ctx.move_to(x + 3, 45)
    ctx.show_text(text)


def draw_text_at(ctx, x, y, text, font_size=12, color=[1, 1, 1]):
    text = str(text)
    ctx.set_source_rgb(*color)
    ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(font_size)
    ctx.move_to(x, y)
    ctx.show_text(text)


def draw_knob(ctx, center_x, center_y, rad, control, off_value, *color):
    line = 10
    pos1 = 3.14 / 2 + 360 * ((control - 10) / 254) * (3.14 / 180)
    pos2 = 3.14 / 2 + 360 * ((control + 10) / 254) * (3.14 / 180)

    # Canvas
    if off_value == 0:
        ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
        ctx.set_source_rgb(*screen_black)
        ctx.fill()
        ctx.stroke()
    else:
        ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
        ctx.set_source_rgba(*color, 0.5)
        ctx.fill()
        ctx.stroke()

    # Value-canvas
    if off_value == 0:
        ctx.move_to(center_x, center_y)
        ctx.arc(center_x, center_y, rad, 3.14 / 2, 3.14 / 2 + 360 * (control / 254) * (3.14 / 180))
        ctx.close_path()
        ctx.set_source_rgba(*color, 0.5)
        ctx.fill()
        ctx.stroke()
    else:
        ctx.move_to(center_x, center_y)
        ctx.arc(center_x, center_y, rad, 3.14 / 2, 3.14 / 2 + 360 * (control / 254) * (3.14 / 180))
        ctx.close_path()
        ctx.set_source_rgb(*screen_black)
        ctx.fill()
        ctx.stroke()

    # Frame
    if control == off_value:
        ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
        ctx.set_source_rgb(*screen_dark)
        ctx.set_line_width(10)
        ctx.stroke()

    else:
        # Frame Shadow
        ctx.set_source_rgba(*color, 0.25)
        # ctx.arc(center_x - 2.5, center_y + 2.5, rad + 5, 0, 2 * 3.14)
        ctx.arc(center_x, center_y, rad + 5, 0, 2 * 3.14)
        ctx.fill()

        # Main Frame
        if off_value == 0:
            ctx.set_source_rgb(*color)
            ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
            ctx.set_line_width(line)
            ctx.stroke()

            ctx.set_source_rgb(*color)

            ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
            ctx.set_line_width(line)
            ctx.stroke()
        else:
            ctx.set_source_rgb(*color)
            ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
            ctx.set_line_width(line)
            ctx.stroke()

            ctx.set_source_rgb(*color)

            ctx.arc(center_x, center_y, rad, 0, 2 * 3.14)
            ctx.set_line_width(line)
            ctx.stroke()


    # # Indicator
    # Inner (if value is "0")
    if control == off_value:
        ctx.set_source_rgb(*screen_dark)
        # ctx.arc(center_x, center_y, rad + 6, pos1, pos2)
        ctx.arc(center_x, center_y, rad, pos1, pos2)
        ctx.line_to(center_x, center_y)
        ctx.fill()
    else:
        # Main
        ctx.set_source_rgb(*color)
        # ctx.arc(center_x, center_y, rad + 6, pos1, pos2)
        ctx.arc(center_x, center_y, rad, pos1, pos2)
        ctx.line_to(center_x, center_y)
        ctx.fill()

        # # Outer Indicator "marker"
        # ctx.set_source_rgba(1, 1, 1, 0.64)
        # ctx.arc(center_x, center_y, rad, pos1, pos2)
        # ctx.set_line_width(12)
        # ctx.stroke()

def fill_button(ctx, x, y_min, *color):
    # Fill "Button"
    ctx.rectangle(x - 60, y_min, 120, 30)
    ctx.set_source_rgb(*color)
    ctx.fill()


def draw_cue(ctx, x, midi_value):
    y_min = 130
    y = y_min
    color = [0.75, 0.75, 0.75]

    def flag():
        ctx.move_to(x - 8, y + 7)
        ctx.curve_to(x - 2, y + 2, x - 2, y + 12, x + 8, y + 7)
        ctx.line_to(x + 8, y + 17)
        ctx.curve_to(x, y + 22, x, y + 12, x - 8, y + 17)
        ctx.line_to(x - 8, y + 26)
        ctx.line_to(x - 10, y + 26)
        ctx.line_to(x - 10, y + 7)
        ctx.close_path()

    if midi_value == 0:
        # # Cue (Shadow)
        # x = x - 2
        # y = y_min + 2
        # flag()
        # ctx.set_source_rgba(*color, 0.25)
        # ctx.fill()

        # Cue (Fill)
        # x = x + 2
        y = y_min
        flag()

        # pat = cairo.LinearGradient(x, y_min + 10, x, y_min + 25)
        # pat.add_color_stop_rgba(0, *color, 1)
        # pat.add_color_stop_rgba(1, *color, 0.5)
        # ctx.set_source(pat)

        ctx.set_source_rgb(*color)

        ctx.fill_preserve()

        # Cue (Stroke color)
        ctx.set_source_rgb(*color)
        ctx.set_line_width(0)
        ctx.stroke()

    else:
        fill_button(ctx, x, y_min, *color)
        # Paint Shape Black
        flag()
        ctx.set_source_rgb(0, 0, 0)
        ctx.fill()


def draw_bar(ctx, x, midi_value):
    color = [1, 1, 0.3]
    y_min = 130
    y = y_min

    def bar():
        # Bar (More Wine Shape)
        # Bar (Left)
        ctx.move_to(x - 5, y + 25)
        ctx.line_to(x - 2, y + 22)
        ctx.curve_to(x - 12, y + 21, x - 8, y + 13, x - 7, y + 11)
        ctx.curve_to(x - 7, y + 15, x - 8, y + 9, x - 9, y + 9)

        # Bar (Top)
        ctx.line_to(x + 9, y + 9)

        # Bar (Right)
        ctx.curve_to(x + 8, y + 9, x + 7, y + 15, x + 7, y + 11)
        ctx.curve_to(x + 8, y + 13, x + 12, y + 21, x + 2, y + 22)
        ctx.line_to(x + 5, y + 25)

        # Bar (Drinkpinne)
        ctx.move_to(x + 3, y + 8)
        ctx.line_to(x + 5, y + 4)
        ctx.line_to(x + 6, y + 5)
        ctx.line_to(x + 4, y + 8)

        # Bar (Paraply)
        ctx.move_to(x - 5, y + 5)
        ctx.line_to(x - 13, y + 10)
        ctx.curve_to(x - 11, y + 2, x - 4, y + 5, x - 4, y + 5)

    if midi_value == 0:
        bar()

        ctx.set_source_rgb(*color)

        ctx.fill_preserve()

        # Bar (Stroke color)
        ctx.set_source_rgb(*color)
        ctx.set_line_width(0.5)
        ctx.set_line_cap(cairo.LINE_CAP_BUTT)
        ctx.stroke()

    else:
        fill_button(ctx, x, y_min, *color)
        # Paint Shape Black
        bar()
        ctx.set_source_rgb(0, 0, 0)
        ctx.fill()


def draw_beat(ctx, x, midi_value):
    color = [1, 0.4, 0.15]
    y_min = 130
    y = y_min + 2

    def beat():
        # Beat (Shape)
        ctx.move_to(x, y + 12)
        ctx.curve_to(x, y + 2, x + 15, y + 2, x + 10, y + 14)
        ctx.curve_to(x + 10, y + 15, x + 2, y + 22, x + 0, y + 24)
        ctx.curve_to(x - 2, y + 22, x - 10, y + 15, x - 10, y + 14)
        ctx.curve_to(x - 15, y + 2, x + 0, y + 2, x + 0, y + 12)
        ctx.close_path()
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)

    if midi_value == 0:

        beat()

        ctx.set_source_rgb(*color)
        ctx.fill_preserve()

        # Beat (Stroke)
        ctx.set_source_rgb(*color)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        ctx.set_line_width(0)
        ctx.stroke()

    else:
        fill_button(ctx, x, y_min, *color)
        # Paint Shape Black
        beat()
        ctx.set_source_rgb(0, 0, 0)
        ctx.fill()


def draw_nudge_1(ctx, x, midi_value):
    color = [1, 0.4, 0.6]
    y_min = 130
    y_max = y_min + 30
    ctx.set_line_width(2.5)

    def nudge_1():
        # Nudge 1 (Shape)
        ctx.set_line_cap(cairo.LINE_CAP_SQUARE)
        ctx.move_to(x - 12, y_min + 9.3)
        ctx.line_to(x - 12, y_min + 21.7)
        ctx.set_line_width(5)
        ctx.stroke()

        ctx.move_to(x - 4, y_min + 8.3)
        ctx.line_to(x - 4, y_min + 22.7)
        ctx.set_line_width(3)
        ctx.stroke()

        ctx.move_to(x + 4, y_min + 8.1)
        ctx.line_to(x + 4, y_min + 22.9)
        ctx.set_line_width(2.5)
        ctx.stroke()

        ctx.move_to(x + 12, y_min + 7.75)
        ctx.line_to(x + 12, y_min + 23.2)
        ctx.set_line_width(1.7)
        ctx.stroke()

    if midi_value == 0:
        # # Shadow
        # x = x - 2
        # y_min = 132
        # ctx.set_source_rgba(*color, 0.25)
        # ctx.set_line_cap(cairo.LINE_CAP_SQUARE)
        # nudge_1()

        # Nudge 1 fill color
        # x = x + 2
        y_min = 130
        ctx.set_source_rgb(*color)
        nudge_1()

    else:
        fill_button(ctx, x, y_min, *color)
        # Paint Shape Black
        ctx.set_source_rgb(0, 0, 0)
        nudge_1()


def draw_nudge_2(ctx, x, midi_value):
    color = [1, 0.4, 0.6]
    y_min = 130
    ctx.set_line_width(2.5)

    def nudge_2():
        ctx.move_to(x - 12, y_min + 7.75)
        ctx.line_to(x - 12, y_min + 23.2)
        ctx.set_line_width(1.7)
        ctx.stroke()

        ctx.move_to(x - 4, y_min + 8.1)
        ctx.line_to(x - 4, y_min + 22.9)
        ctx.set_line_width(2.5)
        ctx.stroke()

        ctx.move_to(x + 4, y_min + 8.3)
        ctx.line_to(x + 4, y_min + 22.7)
        ctx.set_line_width(3)
        ctx.stroke()

        ctx.move_to(x + 12, y_min + 9.3)
        ctx.line_to(x + 12, y_min + 21.7)
        ctx.set_line_width(5)
        ctx.stroke()

    if midi_value == 0:
        # Nudge 2 (Fill color)
        ctx.set_source_rgb(*color)
        # ctx.fill()

        # Nudge 2 (Stroke color)
        ctx.set_source_rgb(*color)
        ctx.set_line_cap(cairo.LINE_CAP_SQUARE)
        nudge_2()

    else:
        fill_button(ctx, x, y_min, *color)
        # Paint Shape Black
        ctx.set_source_rgb(0, 0, 0)
        nudge_2()


def draw_mute_button(ctx, x, mute_value, color):
    ctx.select_font_face("Ableton Sans Bold", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(15)

    if mute_value == 0:
        text = "MUTE"
        ctx.set_source_rgb(0.25, 0.25, 0.25)
    else:
        text = "ON"
        ctx.set_source_rgb(*color)

    ctx.move_to(x - (ctx.text_extents(text)[2] / 2), 150)
    ctx.show_text(text)


def draw_potentiometer(ctx, x, control, mute_value, color):
    # Line
    if mute_value == 0:
        ctx.set_source_rgb(0.125, 0.125, 0.125)
    else:
        ctx.set_source_rgba(*color, 0.25)
    ctx.set_line_width(2)
    ctx.move_to(x, 47.5)
    ctx.line_to(x, 118)
    ctx.stroke()

    ctx.select_font_face("Verdana", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    font_size = 9
    ctx.set_font_size(font_size)

    # Markers
    # + 6
    ctx.move_to(x - 7.5, 47.5)
    ctx.line_to(x + 7.5, 47.5)
    ctx.set_source_rgb(*color)
    ctx.stroke()

    ctx.move_to(x - 25, 50)
    ctx.set_source_rgba(*color, 0.25)
    ctx.show_text("10")
    ctx.stroke()

    ctx.arc(x + 25, 47.5, 4, 0, 2 * 3.14)
    ctx.set_line_width(2)
    ctx.set_source_rgba(*color, 0.25)
    ctx.stroke()

    # 0
    ctx.move_to(x - 15, 64.5)
    ctx.line_to(x + 15, 64.5)
    ctx.set_source_rgb(*color)
    ctx.stroke()

    ctx.move_to(x - 25, 68)
    ctx.set_source_rgba(*color, 0.25)
    ctx.show_text("0")
    ctx.stroke()

    ctx.arc(x + 25, 64.5, 4, 0, 2 * 3.14)
    ctx.set_line_width(2)
    ctx.set_source_rgba(*color, 0.25)
    ctx.stroke()

    # Mitten
    ctx.move_to(x - 10, 82.5)
    ctx.line_to(x + 10, 82.5)
    ctx.set_source_rgb(*color)
    ctx.stroke()

    ctx.move_to(x - 25, 86)
    ctx.set_source_rgba(*color, 0.25)
    ctx.show_text("10")
    ctx.stroke()

    ctx.arc(x + 25, 82.5, 4, 0, 2 * 3.14)
    ctx.set_line_width(2)
    ctx.set_source_rgba(*color, 0.25)
    ctx.stroke()

    # - 30
    ctx.move_to(x - 10, 100)
    ctx.line_to(x + 10, 100)
    ctx.set_source_rgb(*color)
    ctx.stroke()

    ctx.move_to(x - 25, 103)
    ctx.set_source_rgba(*color, 0.25)
    ctx.show_text("30")
    ctx.stroke()

    ctx.arc(x + 25, 100, 4, 0, 2 * 3.14)
    ctx.set_line_width(2)
    ctx.set_source_rgba(*color, 0.25)
    ctx.stroke()

    # - 60
    ctx.move_to(x - 7.5, 118)
    ctx.line_to(x + 7.5, 118)
    ctx.set_source_rgb(*color)
    ctx.stroke()

    ctx.move_to(x - 25, 120)
    ctx.set_source_rgba(*color, 0.25)
    ctx.show_text(" ∞")
    ctx.stroke()

    ctx.arc(x + 25, 117.5, 4, 0, 2 * 3.14)
    ctx.set_line_width(2)
    ctx.set_source_rgba(*color, 0.25)
    ctx.stroke()

    # Pot
    # Pot (Color)
    if mute_value == 0:
        ctx.set_source_rgb(0.25, 0.25, 0.25)

    else:
        pat = cairo.LinearGradient(x, 110 - (70 * (control / 127)), x, 125 - (70 * (control / 127)))
        pat.add_color_stop_rgb(0, 0.75, 0.75, 0.75)
        pat.add_color_stop_rgb(0.5, 0.5, 0.5, 0.5)
        pat.add_color_stop_rgb(1, 0.75, 0.75, 0.75)
        ctx.set_source(pat)

    # Pot (Main)
    ctx.rectangle(x - 5, 110 - (70 * (control / 127)), 10, 15)
    ctx.fill_preserve()
    ctx.set_source_rgba(*color, 0.25)
    ctx.stroke()

    # Pot (Outlines)
    ctx.move_to(x - 5, 110 - (70 * (control / 127)) + 7.5)
    ctx.line_to(x + 5, 110 - (70 * (control / 127)) + 7.5)
    ctx.set_source_rgba(*color, 0.5)
    ctx.stroke()
