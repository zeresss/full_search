def get_spn(envelope):
    lower, upper = envelope["lowerCorner"].split(), envelope["upperCorner"].split()
    return f'{float(upper[0]) - float(lower[0])},{float(upper[1]) - float(lower[1])}'
