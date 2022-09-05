def maxi(a,b):
    if a > b:
        return a
    else:
        return b
def maxiProfit(prices):
    profit = 0
    least = prices[0]
    for current in prices:
        if current < least:
            least = current
        profit = maxi(profit, current - least)
    return profit
    
prices = list(map(int,input().split()))
print(maxiProfit(prices))