import mido


def update_encoder(encoder, cc, increment):

    max_encoder_value = 254
    updated_value = int(encoder + increment)

    if updated_value < 0:
        encoder = 0
    elif updated_value > max_encoder_value:
        encoder = max_encoder_value
    else:
        encoder = updated_value

    msg = mido.Message('control_change', control=cc, value=int(round(encoder / 2)))

    return msg, encoder
