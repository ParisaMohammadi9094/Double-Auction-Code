###Double Auction Simulation in MATLAB
##Overview
#This MATLAB script simulates a double auction market where multiple sellers and buyers interact. The script determines the volumes and prices at which trades occur based on bids from both parties. It calculates the accepted volumes and prices for both sellers and buyers, as well as the resulting profits.

>[!Features]
Initializes the market with a specified number of sellers and buyers.
Accepts bids and volumes from sellers and buyers.
Matches buyers and sellers based on their bids.
Calculates the accepted volumes, prices, and profits for both sellers and buyers.
Computes the remaining volumes for sellers and buyers after the auction.
Evaluates the profits from selling to or buying from the main grid at a fixed price.


>[!Notes]
Ensure that the initial bid prices and volumes are correctly set for both sellers and buyers.
The script currently uses fixed prices for selling to and buying from the main grid (p_sell = 26 and p_buy = 10), which can be adjusted as needed.
