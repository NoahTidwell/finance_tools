buyPrice = float(input("At what price did you buy? >"))
sellPrice = float(input("At what price did you sell? >"))

loss = buyPrice - sellPrice
decimalLoss = (loss / buyPrice)
f_userLoss = format(decimalLoss, ".2%")

gainNeeded = (1 / (1 - decimalLoss)) - 1
f_gainNeeded = format(gainNeeded, ".2%")


print("You lost", f_userLoss, "in your trade.")
print("You need to gain", f_gainNeeded, "to recapture your losses.")