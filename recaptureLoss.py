userLoss = float(input("What percent are you down? > "))

userLossDecimal = userLoss / 100

gainNeeded = (1 / (1 - userLossDecimal)) - 1
f_gainNeeded = format(gainNeeded, ".3%")

print("You need to gain", f_gainNeeded, "to recapture your losses.")