def getBondPrice(y, face, couponRate, m, ppy=1):
    n = m * ppy  
    r = y / ppy  
    c = face * couponRate / ppy  

    bondPrice = 0

    for t in range(1, n + 1):
        bondPrice += c / (1 + r) ** t

    bondPrice += face / (1 + r) ** n

    return (bondPrice)