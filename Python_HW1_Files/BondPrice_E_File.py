
def getBondPrice_E(face, couponRate, m, yc):
    bondPrice = 0
    for t, yield_rate in enumerate(yc, start=1):
        discount_factor = 1 / (1 + yield_rate)**t
        coupon_payment = face * couponRate
        if t < m:
            bondPrice += coupon_payment * discount_factor
        else:
            bondPrice += (coupon_payment + face) * discount_factor
    
    return (bondPrice)