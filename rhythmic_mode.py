import push2_python.constants

import definitions
from melodic_mode import MelodicMode


class RhythmicMode(MelodicMode):

    rhythmic_notes_matrix = [
        [64, 65, 66, 67, 96, 97, 98, 99],
        [60, 61, 62, 63, 92, 93, 94, 95],
        [56, 57, 58, 59, 88, 89, 90, 91],
        [52, 53, 54, 55, 84, 85, 86, 87],
        [48, 49, 50, 51, 80, 81, 82, 83],
        [44, 45, 46, 47, 76, 77, 78, 79],
        [40, 41, 42, 43, 72, 73, 74, 75],
        [36, 37, 38, 39, 68, 69, 70, 71]
    ]

    def get_settings_to_save(self):
        return {}

    def pad_ij_to_midi_note(self, pad_ij):
        return self.rhythmic_notes_matrix[pad_ij[0]][pad_ij[1]]

    def deactivate(self):
        self.push.buttons.set_button_color(push2_python.constants.BUTTON_ACCENT, definitions.BLACK)

    def update_buttons(self):
        self.update_accent_button()

    def update_pads(self):
        color_matrix = []
        for i in range(0, 8):
            row_colors = []
            for j in range(0, 8):
                corresponding_midi_note = self.pad_ij_to_midi_note([i, j])
                cell_color = definitions.ROOT_KEY

                # 1/4 (Upper-left 4x4)
                if i <= 4 and j < 4:
                    cell_color = definitions.BLACK

                # SPARKLE (Bottom-left 4x4)
                # ROW 1
                elif i == 4 and j == 0:
                    cell_color = definitions.BLACK
                elif i == 4 and j == 1:
                    cell_color = definitions.BLACK
                elif i == 4 and j == 2:
                    cell_color = definitions.BLACK
                elif i == 4 and j == 3:
                    cell_color = definitions.BLACK

                # ROW 2
                elif i == 5 and j == 0:
                    cell_color = definitions.S5
                elif i == 5 and j == 1:
                    cell_color = definitions.S6
                elif i == 5 and j == 2:
                    cell_color = definitions.S7
                elif i == 5 and j == 3:
                    cell_color = definitions.S8

                # ROW 3
                elif i == 6 and j == 0:
                    cell_color = definitions.S2
                elif i == 6 and j == 1:
                    cell_color = definitions.S3
                elif i == 6 and j == 2:
                    cell_color = definitions.S4
                elif i == 6 and j == 3:
                    cell_color = definitions.S5

                # ROW 4
                elif i == 7 and j == 0:
                    cell_color = definitions.S1
                elif i == 7 and j == 1:
                    cell_color = definitions.S1
                elif i == 7 and j == 2:
                    cell_color = definitions.BLACK
                elif i == 7 and j == 3:
                    cell_color = definitions.S6

                # DRUM (Upper-right 4x4)
                # ROW 1
                elif i == 0 and j == 4:
                    cell_color = definitions.CRASH_COLOR
                elif i == 0 and j == 5:
                    cell_color = definitions.TOM_1_COLOR
                elif i == 0 and j == 6:
                    cell_color = definitions.TOM_1_COLOR
                elif i == 0 and j == 7:
                    cell_color = definitions.CRASH_COLOR

                # ROW 2
                elif i == 1 and j == 4:
                    cell_color = definitions.TOM_2_COLOR
                elif i == 1 and j == 5:
                    cell_color = definitions.KICK_DRUM_COLOR
                elif i == 1 and j == 6:
                    cell_color = definitions.KICK_DRUM_COLOR
                elif i == 1 and j == 7:
                    cell_color = definitions.TOM_2_COLOR

                # ROW 3
                elif i == 2 and j == 4:
                    cell_color = definitions.OPEN_HIHAT_COLOR
                elif i == 2 and j == 5:
                    cell_color = definitions.CLOSED_HIHAT_COLOR
                elif i == 2 and j == 6:
                    cell_color = definitions.CLOSED_HIHAT_COLOR
                elif i == 2 and j == 7:
                    cell_color = definitions.OPEN_HIHAT_COLOR

                # ROW 4
                elif i == 3 and j == 4:
                    cell_color = definitions.STICK_COLOR
                elif i == 3 and j == 5:
                    cell_color = definitions.SNARE_COLOR
                elif i == 3 and j == 6:
                    cell_color = definitions.SNARE_COLOR
                elif i == 3 and j == 7:
                    cell_color = definitions.STICK_COLOR

                # 4/4 (Bottom-right 4x4)
                elif i >= 4 and j >= 4:
                    cell_color = definitions.BLACK

                if self.is_midi_note_being_played(corresponding_midi_note):
                    cell_color = definitions.NOTE_ON_COLOR

                else:
                    pass

                row_colors.append(cell_color)
            color_matrix.append(row_colors)

        self.push.pads.set_pads_color(color_matrix)

    def on_button_pressed(self, button_name):
        if button_name == push2_python.constants.BUTTON_ACCENT:
            self.fixed_velocity_mode = not self.fixed_velocity_mode
            self.app.buttons_need_update = True
            self.app.pads_need_update = True
