#!/usr/bin/python

import argparse

def find_max_profit(prices):
  #Receive a series of prices
  #use test example [1050, 270, 1540, 3800, 2]
  
  #Find largest difference -> Negative indicate a loss
  
  # Math goes like this by iterating through
  # 1050 -> Buy, no profit made
  # 270 -> buy, no profit 270 - 1050 =  -780
  # 1540 subtract with previous numbers -> 1540-270 or 1540-1050 -> profit is made on both, records these
  # 3800 subtract with previous numbers, largest profit so far
  # 2 is last number and isn't profitable
  
  # Use the hints
  
  #Max profit math is subtracting some price by another price that comes before it
  
    current_min_price_so_far = prices[0]#start with first number
    max_profit_so_far = 0 #profit will zero at start
    for i in range(len(prices)):#loop through given prices
        current_price = prices[i]#current price indicator
        if current_price < current_min_price_so_far:#check for lowest price and reassign
            if max_profit_so_far <= 0: #tracks for lowest profit for negative difference
                max_profit_so_far = current_price - current_min_price_so_far
            current_min_price_so_far = current_price #reassign the min price
        elif current_price - current_min_price_so_far > max_profit_so_far: #calculate max profit so far in the loop and compared to previous max profit
            max_profit_so_far = current_price - current_min_price_so_far
    return max_profit_so_far

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  # Execute as 'python stock_prices.py 1050 2740 1540 3800 2' To pass args
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))