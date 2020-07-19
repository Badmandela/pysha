# Instrument volume
        pos1 = 3.14 / 2 + 360 * ((controls['instr_vol'] - 5) / 127) * (3.14 / 180)
        pos2 = 3.14 / 2 + 360 * ((controls['instr_vol'] + 5) / 127) * (3.14 / 180)
        center_x = 300

        # Instrument_volume title
        if controls['instr'] <= piano_max:
            ctx.set_source_rgb(*color_piano)
        if synth_min <= controls['instr'] <= synth_max:
            ctx.set_source_rgb(*color_synth)
        if controls['instr'] >= sampler_min:
            ctx.set_source_rgb(*color_sampler)
        s = "INSTR. LVL:"
        ctx.move_to(300 - (ctx.text_extents(s)[2] / 2), 15)
        ctx.show_text(s)

        ctx.stroke()

        # Instrument_volume value 1 (inverted canvas)
        if controls['instr_vol'] >= 100:
            ctx.set_source_rgb(*color_piano_light)
        else:
            ctx.set_source_rgb(*screen_dark)
        ctx.arc(300, 70, 42, 2 * 3.14, 3.14 / 2 + 360 * (controls['instr_vol'] / 127) * (3.14 / 180))
        ctx.line_to(300, 70)
        ctx.fill()
        ctx.stroke()

        # Instrument_volume value 2 (inverted canvas)
        if controls['instr_vol'] <= 90:
            ctx.set_source_rgb(*color_piano_dark)
        if controls['instr_vol'] >= 100:
            ctx.set_source_rgb(*color_piano_dark)
        ctx.arc(300, 70, 42, 3.14 / 2 + 360 * (controls['instr_vol'] / 127) * (3.14 / 180), 2 * 3.14)
        ctx.line_to(300, 70)
        ctx.fill()
        ctx.stroke()

        # ## Instrument_volume frame
        ctx.arc(300, 70, 40, 0.5 * 3.14, 2 * 3.14)
        if controls['instr_vol'] <= 90:
            if controls['instr'] <= piano_max:
                ctx.set_source_rgb(*color_piano)
            if synth_min <= controls['instr'] <= synth_max:
                ctx.set_source_rgb(*color_synth)
            if controls['instr'] >= sampler_min:
                ctx.set_source_rgb(*color_sampler)
        elif controls['instr_vol'] >= 100:
            ctx.set_source_rgb(*screen_dark)
            if controls['instr'] <= piano_max:
                ctx.set_source_rgb(*color_piano_light)
            if synth_min <= controls['instr'] <= synth_max:
                ctx.set_source_rgb(*color_synth_light)
            if controls['instr'] >= sampler_min:
                ctx.set_source_rgb(*color_sampler_light)
        else:
            ctx.set_source_rgb(*screen_dark)

        ctx.set_line_width(10)
        ctx.stroke()

        # Instrument_volume frame 2 !!!
        ctx.arc(300, 70, 40, 0 * 3.14, 0.5 * 3.14)
        if controls['instr_vol'] <= 90:
            if controls['instr'] <= piano_max:
                ctx.set_source_rgb(*color_piano_dark)
            if synth_min <= controls['instr'] <= synth_max:
                ctx.set_source_rgb(*color_synth_dark)
            if controls['instr'] >= sampler_min:
                ctx.set_source_rgb(*color_sampler_dark)
        elif controls['instr_vol'] >= 100:
            ctx.set_source_rgb(*screen_dark)
            if controls['instr'] <= piano_max:
                ctx.set_source_rgb(*color_piano_light)
            if synth_min <= controls['instr'] <= synth_max:
                ctx.set_source_rgb(*color_synth_light)
            if controls['instr'] >= sampler_min:
                ctx.set_source_rgb(*color_sampler_light)
        else:
            ctx.set_source_rgb(*screen_dark)

        ctx.set_line_width(10)
        ctx.stroke()

        # Instrument indicator frame
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        if controls['instr_vol'] <= 90:
            if controls['instr'] <= piano_max:
                ctx.set_source_rgb(*color_piano_light)
            if synth_min <= controls['instr'] <= synth_max:
                ctx.set_source_rgb(*color_synth_light)
            if controls['instr'] >= sampler_min:
                ctx.set_source_rgb(*color_sampler_light)
        elif controls['instr_vol'] >= 100:
            if controls['instr'] <= piano_max:
                ctx.set_source_rgb(*color_piano)
            if synth_min <= controls['instr'] <= synth_max:
                ctx.set_source_rgb(*color_synth)
            if controls['instr'] >= sampler_min:
                ctx.set_source_rgb(*color_sampler)
        else:
            ctx.set_source_rgb(*screen_dark)
        ctx.move_to(center_x, 70)
        ctx.arc(center_x, 70, 46, pos1, pos2)
        ctx.line_to(center_x, 70)
        ctx.set_line_width(3)
        ctx.stroke()
        ctx.set_line_cap(cairo.LINE_CAP_BUTT)

        # Instrument_volume indicator inner
        if controls['instr_vol'] <= 90:
            if controls['instr'] <= piano_max:
                ctx.set_source_rgb(*color_piano)
            if synth_min <= controls['instr'] <= synth_max:
                ctx.set_source_rgb(*color_synth)
            if controls['instr'] >= sampler_min:
                ctx.set_source_rgb(*color_sampler)
        elif controls['instr_vol'] >= 100:
            ctx.set_source_rgb(*screen_dark)
            if controls['instr'] <= piano_max:
                ctx.set_source_rgb(*color_piano_light)
            if synth_min <= controls['instr'] <= synth_max:
                ctx.set_source_rgb(*color_synth_light)
            if controls['instr'] >= sampler_min:
                ctx.set_source_rgb(*color_sampler_light)
        else:
            ctx.set_source_rgb(*screen_dark)

        ctx.arc(300, 70, 42, pos1, pos2)
        ctx.line_to(300, 70)
        ctx.fill()

        # Instrument_volume indicator outer
        if controls['instr_vol'] <= 90:
            if controls['instr'] <= piano_max:
                ctx.set_source_rgb(*color_piano_light)
            if synth_min <= controls['instr'] <= synth_max:
                ctx.set_source_rgb(*color_synth_light)
            if controls['instr'] >= sampler_min:
                ctx.set_source_rgb(*color_sampler_light)
        elif controls['instr_vol'] >= 100:
            if controls['instr'] <= piano_max:
                ctx.set_source_rgb(*color_piano)
            if synth_min <= controls['instr'] <= synth_max:
                ctx.set_source_rgb(*color_synth)
            if controls['instr'] >= sampler_min:
                ctx.set_source_rgb(*color_sampler)
        else:
            ctx.set_source_rgb(*screen_dark)

        ctx.arc(300, 70, 40, pos1, pos2)
        ctx.set_line_width(12)
        ctx.stroke()