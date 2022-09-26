buyPrice = float(input("At what price did you buy? >"))
sellPrice = float(input("At what price did you sell? >"))

pnl = sellPrice - buyPrice

if pnl > 0:
    decimalGain = (pnl / buyPrice)
    f_gain = format(decimalGain, ".2%")
    print("Congrats! You were profitable. You gained", f_gain)
elif pnl == 0:
    decimalGain = (pnl / buyPrice)
    b_e = decimalGain * 100
    f_be = format(b_e, ".2%")
    print("You were breakeven on your trade", f_be)
elif pnl < 0:
    pnl = buyPrice - sellPrice
    decimalLoss = (pnl / buyPrice)
    f_userLoss = format(decimalLoss, ".2%")

    gainNeeded = (1 / (1 - decimalLoss)) - 1
    f_gainNeeded = format(gainNeeded, ".2%")

    print("You lost", f_userLoss, "in your trade.")
    print("You need to gain", f_gainNeeded, "to recapture your losses.")