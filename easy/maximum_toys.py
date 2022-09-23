def maximumToys(prices, k):
    # Write your code here
    prices.sort()

    total_price = 0
    number_of_items = 0
    counter = 0

    condition = 0
    while condition < k:
        total_price += prices[counter]
        number_of_items += 1
        counter += 1
        condition = total_price + prices[counter]
    
    return number_of_items

print(maximumToys([1, 12, 5, 111, 200, 1000, 10], 50))