# Big O will be O(n^2)

def max_profit(stock):
    n = len(stock)
    max_profit = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            new_profit = stock[j] - stock[i]
            if new_profit > 0 and new_profit >= max_profit:
                max_profit = new_profit

    return max_profit


stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))
