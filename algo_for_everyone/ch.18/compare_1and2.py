import time
import random


def max_profit1(stock):
    n = len(stock)
    max_profit = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            new_profit = stock[j] - stock[i]
            if new_profit > 0 and new_profit >= max_profit:
                max_profit = new_profit

    return max_profit


def max_profit2(stock):
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


def test(n):
    # 테스트 자료 만들기 (5000부터 20000까지의 난수를 추가로 사용)
    a = []
    for i in range(0, n):
        a.append(random.randint(5000, 20000))

    # 느린 O(n*n) 알고리즘 테스트
    start = time.time()
    mps = max_profit1(a)
    end = time.time()
    time_result_1 = end - start

    # 빠른 O(n)알고리즘 테스트
    start = time.time()
    mpf = max_profit2(a)
    end = time.time()
    time_result_2 = end - start

    # 결과 출격: 계산 결과
    print(n, mps, mpf)  # 입력크기,각각 알고리즘이 계산한 최대 수익갑.(같아야함)
    m = 0  # 결과출력: 계산 시간 비교.
    if time_result_2 > 0:  # 컴퓨터 환경에 따라 빠른 알고리즘 시간이 0 으로 측정될수 있음. 그럴때는 0을 출력
        m = time_result_1 / time_result_2

    print("%d %.5f %.5f %.2f" % (n, time_result_1, time_result_2, m))


test(100)
test(10000)
