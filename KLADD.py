


@push2_python.on_button_pressed(push2_python.constants.BUTTON_LOWER_ROW_1
    def function(push):
        msg = mido.Message('control_change', control=101, value=127)
        self.send_midi_func(msg)

    @push2_python.on_button_pressed(push2_python.constants.BUTTON_LOWER_ROW_2
    def function(push):
        msg = mido.Message('control_change', control=102, value=127)
        self.send_midi_func(msg)

    @push2_python.on_button_pressed(push2_python.constants.BUTTON_LOWER_ROW_3
    def function(push):
        msg = mido.Message('control_change', control=103, value=127)
        self.send_midi_func(msg)

    @push2_python.on_button_pressed(push2_python.constants.BUTTON_LOWER_ROW_4
    def function(push):
        msg = mido.Message('control_change', control=104, value=127)
        self.send_midi_func(msg)

    @push2_python.on_button_pressed(push2_python.constants.BUTTON_LOWER_ROW_5
    def function(push):
        msg = mido.Message('control_change', control=105, value=127)
        self.send_midi_func(msg)

    @push2_python.on_button_pressed(push2_python.constants.BUTTON_LOWER_ROW_6
    def function(push):
        msg = mido.Message('control_change', control=106, value=127)
        self.send_midi_func(msg)

    @push2_python.on_button_pressed(push2_python.constants.BUTTON_LOWER_ROW_7
    def function(push):
        msg = mido.Message('control_change', control=107, value=127)
        self.send_midi_func(msg)

    @push2_python.on_button_pressed(push2_python.constants.BUTTON_LOWER_ROW_8
    def function(push):
        msg = mido.Message('control_change', control=108, value=127)
        self.send_midi_func(msg)







#############################################################################
#############################################################################
        #
        #           FILTER DRAW TEST 8 Rectangular version...
        #


# Filter "canvas"
        ctx.rectangle(120, 25, 254, 90)
        ctx.set_source_rgb(0.1, 0.05, 0.01)
        ctx.fill()

        # Filter frequency:
        filter_frequency = (controls['instrument_filter'] * 2) + 120

        ctx.move_to(filter_frequency, 25)
        ctx.line_to(filter_frequency, 115)
        ctx.line_to(374, 115)
        ctx.line_to(374, 25)
        ctx.close_path()
        ctx.set_source_rgb(1, 0.5, 0.1)
        ctx.fill()

        # Filter "frame":
        ctx.rectangle(120, 25, 254, 90)
        if controls['instrument_filter'] == 127:
            ctx.set_source_rgb(0.2, 0.1, 0.02)
        else:
            ctx.set_source_rgb(1, 0.5, 0.1)
        ctx.set_line_width(5)
        ctx.stroke()