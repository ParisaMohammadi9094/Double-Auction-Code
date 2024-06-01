import numpy as np

# Initialize market state
num_sellers = 3
num_buyers = 3

sellers_bids = np.array([2, 14, 3])
sellers_volume = np.array([2, 3, 1])
sellers_volume_initial = sellers_volume.copy()

loads_bids = np.array([20, 15, 33])
loads_volume = np.array([1, 4, 2])
loads_volume_initial = loads_volume.copy()

minpsell = np.min(sellers_bids)
indminpsell = np.argmin(sellers_bids)
maxpbuy = np.max(loads_bids)
indmaxpbuy = np.argmax(loads_bids)

volume_accept_sellers = np.zeros(num_sellers)
price_accept_sellers = np.zeros(num_sellers)
volume_accept_load = np.zeros(num_buyers)
price_accept_load = np.zeros(num_buyers)
i = 0

while (minpsell <= maxpbuy and 
       sellers_bids[indminpsell] < 1000 and 
       loads_bids[indmaxpbuy] > 0 and 
       sellers_bids[indminpsell] != 0):  # sellers_bid won't be equal to zero as we choose it from a known set
    if sellers_volume[indminpsell] < loads_volume[indmaxpbuy]:
        volume_accept_sellers[indminpsell] = sellers_volume[indminpsell]
        volume_accept_load[indmaxpbuy] = sellers_volume[indminpsell]
        loads_volume[indmaxpbuy] -= sellers_volume[indminpsell]
        sellers_volume[indminpsell] = 0
        price_accept_sellers[indminpsell] = (loads_bids[indmaxpbuy] + sellers_bids[indminpsell]) / 2
        price_accept_load[indmaxpbuy] = (loads_bids[indmaxpbuy] + sellers_bids[indminpsell]) / 2
        sellers_bids[indminpsell] = 1000
    elif sellers_volume[indminpsell] == loads_volume[indmaxpbuy]:
        volume_accept_sellers[indminpsell] = sellers_volume[indminpsell]
        volume_accept_load[indmaxpbuy] = sellers_volume[indminpsell]
        loads_volume[indmaxpbuy] = 0
        sellers_volume[indminpsell] = 0
        price_accept_sellers[indminpsell] = (loads_bids[indmaxpbuy] + sellers_bids[indminpsell]) / 2
        price_accept_load[indmaxpbuy] = (loads_bids[indmaxpbuy] + sellers_bids[indminpsell]) / 2
        sellers_bids[indminpsell] = 1000
        loads_bids[indmaxpbuy] = -3
    else:
        volume_accept_sellers[indminpsell] = loads_volume[indmaxpbuy]
        volume_accept_load[indmaxpbuy] = loads_volume[indmaxpbuy]
        sellers_volume[indminpsell] -= loads_volume[indmaxpbuy]
        loads_volume[indmaxpbuy] = 0
        price_accept_sellers[indminpsell] = (loads_bids[indmaxpbuy] + sellers_bids[indminpsell]) / 2
        price_accept_load[indmaxpbuy] = (loads_bids[indmaxpbuy] + sellers_bids[indminpsell]) / 2
        loads_bids[indmaxpbuy] = -3
    
    minpsell = np.min(sellers_bids)
    indminpsell = np.argmin(sellers_bids)
    maxpbuy = np.max(loads_bids)
    indmaxpbuy = np.argmax(loads_bids)
    i += 1

profit_accept_sellers = volume_accept_sellers * price_accept_sellers
profit_sellers_accept_loads = np.sum(profit_accept_sellers)

volume_accept_sellers_total = np.sum(volume_accept_sellers)

profit_accept_loads = volume_accept_load * price_accept_load
profit_loads = np.sum(profit_accept_loads)

volume_accept_load_total = np.sum(volume_accept_load)

p_sell = 26
p_buy = 10

sellers_volume_left = sellers_volume_initial - volume_accept_sellers
profit_sellers_to_maingrid = sellers_volume_left * p_sell

loads_volume_left = loads_volume_initial - volume_accept_load
profit_loads_to_maingrid = loads_volume_left * p_buy

print("Profit Accept Sellers: \n", profit_accept_sellers)
print("Profit Sellers Accept Loads: \n", profit_sellers_accept_loads)
print("Volume Accept Sellers: \n", volume_accept_sellers_total)
print("Profit Accept Loads: \n", profit_accept_loads)
print("Profit Loads: \n", profit_loads)
print("Volume Accept Load: \n", volume_accept_load_total)
print("Sellers Volume Left: \n", sellers_volume_left)
print("Profit Sellers to Main Grid: \n", profit_sellers_to_maingrid)
print("Loads Volume Left: \n", loads_volume_left)
print("Profit Loads to Main Grid: \n", profit_loads_to_maingrid)
