# A list of prices where prices[i] is the price of stock on day i. You want to buy one stock and sell one stock - just one trasactions - to maximize your profit , return the maximum profit you can achieve .If no profit is possible ,return 0.

# you want to :-
# Buy at the lowest price
# Sell at the highest price after that
# So,track the minimum price seen so far ,and calculate the profit if we sell today.
# Keep updating the maximum profit found so far.

# Stock Market Analysis (Greedy pattern example) :-

# Best Time to Buy and sell Stock (Single Transaction only ) :-

def max_Profit(prices):
    if not prices :
        return 0

    for price in prices[1:]:
        if price<min_price:
            min_price=price
        else:
            profit = price - min_price
            max_profit=max(max_profit,profit)
    return max_profit

    print(max_profit([7,1,5,3,6,4]))
