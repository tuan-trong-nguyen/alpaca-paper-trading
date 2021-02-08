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
# api = tradeapi.REST()
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
 
 
symbol = 'AAPL'
symbol_bars = api.get_barset(symbol, 'minute', 1).df.iloc[0]
symbol_price = symbol_bars[symbol]['close']

# We could buy a position and add a stop-loss and a take-profit of 5 %
api.submit_order(
    symbol=symbol,
    qty=1,
    side='buy',
    type='market',
    time_in_force='gtc',
    order_class='bracket',
    stop_loss={'stop_price': symbol_price * 0.95,
               'limit_price':  symbol_price * 0.94},
    take_profit={'limit_price': symbol_price * 1.05}
)


