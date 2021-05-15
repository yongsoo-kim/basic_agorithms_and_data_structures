def max_profit(stock):
    n = len(stock)
    max_profit = 0
    lowest_price = stock[0]

    for i in range(n):
        profit = stock[i] - lowest_price
        if profit >= max_profit:  # 이수익이 지금까지 최대수익보다 크면 값을 고침. !!!!!!주의. 이부분이 11행보다 아래로 가면 안된다. 이미 보유한 최소값의 주식과(어제까지) 오늘의 값을 비교해야하기 때문이다!!!!!!!!!!
            max_profit = profit

        if stock[i] <= lowest_price:  # i날 주가가 초솟값보다 작으면 값을 고침
            lowest_price = stock[i]

    return max_profit



stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))
