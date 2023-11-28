
def getBondDuration(y, face, couponRate, m, ppy = 1):
    pvcfsum = 0
    wtsum = 0
    cf = face * couponRate
  
    for t in range(1, m + 1):
        pv = (1+y)**-t
        pvcf = pv * cf
        wt = pvcf * t
        pvcfsum = pvcfsum + pvcf
        wtsum = wtsum + wt
  

    pvcfsum = pvcfsum+face*(1+y)**-m
    wtsum = wtsum + (face*(1+y)**-m)*t
    bondDuration = wtsum / pvcfsum
    return(bondDuration)
