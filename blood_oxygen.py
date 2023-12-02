
def blood_oxygen(carrying_capacity, hemoglobin_concentration, saturation, blood_volume, side):
    if side == 'arterial':
        side = 0.25
    elif side == 'venous':
        side == 0.75
    return carrying_capacity * hemoglobin_concentration * saturation * blood_volume * side