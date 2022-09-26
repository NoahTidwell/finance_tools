buyPrice = float(input("At what price did you buy? >"))
sellPrice = float(input("At what price did you sell? >"))

pnl = sellPrice - buyPrice

if pnl > 0:
    decimalGain = (pnl / buyPrice)
    f_gain = format(decimalGain, ".2%")
    print("Congrats! You were","\033[32m" ,"profitable.", "\033[0m", "You gained", "\033[32m",f_gain, "\033[0m")
elif pnl == 0:
    decimalGain = (pnl / buyPrice)
    b_e = decimalGain * 100
    f_be = format(b_e, ".2%")
    print("You were", "\033[33m","breakeven", "\033[0m","on your trade", "\033[33m", f_be, "\033[0m")
elif pnl < 0:
    pnl = buyPrice - sellPrice
    decimalLoss = (pnl / buyPrice)
    f_userLoss = format(decimalLoss, ".2%")

    gainNeeded = (1 / (1 - decimalLoss)) - 1
    f_gainNeeded = format(gainNeeded, ".2%")

    print("You", "\033[31m" "lost", f_userLoss, "\033[0m", "in your trade.")
    print("You need to gain", "\033[32m", f_gainNeeded, "\033[0m", "to recapture your losses.")