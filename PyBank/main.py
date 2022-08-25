import csv

with open('Resources/budget_data.csv', 'r') as csvfile:
    budgetReader = csv.reader(csvfile, delimiter=',')
    header = next(budgetReader)

    months = 0
    total = 0
    increaseMonthYear = ''
    decreaseMonthYear = ''
    increaseChange = 0
    decreaseChange = 0
    previousAmount = 0
    changeTotal = 0
    for row in budgetReader:
        months += 1
        currentAmount = int(row[1])
        total += currentAmount
        change = (currentAmount - previousAmount)
        previousAmount = currentAmount
        if (change == currentAmount):
            continue

        changeTotal += change

        if (change > increaseChange):
            increase = row[0]
            increaseChange = change
    
        if (change < decreaseChange):
            decrease = row[0]
            decreaseChange = change

    outputs = [
    "Financial Analysis",
    "----------------------------",
    "Total Months: %d"%(months),
    "Total: $%d"%(total),
    "Average Change: $%.2f"%(changeTotal/(months-1)),
    "Greatest Increase in Profits: %s ($%s)"%(increaseMonthYear, increaseChange),
    "Greatest Decrease in Profits: %s ($%s)"%(decreaseMonthYear, decreaseChange)
    ]
    with open('analysis/budget_results.txt', 'w') as textFile:
        for output in outputs:
            print(output)
            print(output, file=textFile)
            