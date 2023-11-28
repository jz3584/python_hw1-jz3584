
def getBondPrice_Z(face, couponRate, times, yc):
    bondPrice = 0
    for t, y in zip(times, yc):
        discount_factor = 1 / (1 + y)**t
        bondPrice += face * couponRate * discount_factor
    bondPrice += face / (1 + yc[-1])**times[-1] 
    return (bondPrice)