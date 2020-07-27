def update_encoder(encoder, cc, increment):
    # print("I update: ", encoder)

    max_encoder_value = 254
    updated_value = int(encoder + increment)

    if updated_value < 0:
        encoder = 0
    elif updated_value > max_encoder_value:
        encoder = max_encoder_value
    else:
        encoder = updated_value

    # print("Efter updated: ", encoder)

    # msg = mido.Message('control_change', control=cc, value=int(round(encoder / 2)))

    # return msg
    # self.app.send_midi(msg)


# def update_encoder_value(increment):
#     updated_filter_value = int(controls['master_lpf'] + increment)
#
#     if updated_filter_value < 0:
#         controls['master_lpf'] = 0
#     elif updated_filter_value > max_encoder_value:
#         controls['master_lpf'] = max_encoder_value
#     else:
#         controls['master_lpf'] = updated_filter_value
#
#     print("Increment", increment)
#     print("LPF", int(round(controls['master_lpf'] / 2)))
#     print("UPDATED", int(round(updated_filter_value)))
#
#
# update_encoder_value(increment)
#
# msg = mido.Message('control_change', control=24, value=int(round(controls['master_lpf'] / 2)))
# self.app.send_midi(msg)
