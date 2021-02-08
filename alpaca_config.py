# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 22:09:59 2021

@author: tuann
"""

import alpaca_trade_api as tradeapi

"""
With the Alpaca API, you can check on your daily profit or loss by
comparing your current balance to yesterday's balance.
"""

# First, open the API connection
api = tradeapi.REST(
    'PKQYKLCSI9ZKRMXDZNMM',
    'Uu2caxZ3FZf1aaE8n5Ly0KFjOM50RvzcucxKiHy8',
    'https://paper-api.alpaca.markets'
)

# Get account info
account = api.get_account()

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we can use to open new positions.
print('${} is available as buying power.'.format(account.buying_power))

# Check our current balance vs. our balance at the last market close
balance_change = float(account.equity) - float(account.last_equity)
print(f'Today\'s portfolio balance change: ${balance_change}')
    
# Check if AAPL is tradable on the Alpaca platform.
aapl_asset = api.get_asset('AAPL')
if aapl_asset.tradable:
    print('We can trade AAPL.')

# Check if the market is open now.
clock = api.get_clock()
print('The market is {}'.format('open.' if clock.is_open else 'closed.'))

# Check when the market was open on Dec. 1, 2018
date = '2021-02-08'
calendar = api.get_calendar(start=date, end=date)[0]
print('The market opened at {} and closed at {} on {}.'.format(
    calendar.open,
    calendar.close,
    date
))    
    
# Get daily price data for AAPL over the last 5 trading days.
barset = api.get_barset('AAPL', '1Min', limit=10)
aapl_bars = barset['AAPL']

# See how much AAPL moved in that timeframe.
week_open = aapl_bars[0].o
week_close = aapl_bars[-1].c
percent_change = (week_close - week_open) / week_open * 100
print('AAPL moved {}% over the last 5 days'.format(percent_change))  


  