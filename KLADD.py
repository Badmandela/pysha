def on_button_pressed(self, button_name):
    if button_name in self.pyramid_track_button_names_a:
        self.select_pyramid_track(self.pyramid_track_button_names_a.index(button_name))
        self.pyramid_track_selection_button_a = False
        self.app.buttons_need_update = True
        self.app.pads_need_update = True