


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