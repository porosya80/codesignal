def depositProfit(deposit, rate, threshold):
    counter = 0
    while deposit < threshold:
        counter += 1
        deposit += (deposit/100*rate)
    return counter






deposit = 100
rate = 20 
threshold = 170
print(depositProfit(deposit, rate, threshold))
