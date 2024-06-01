Double Auction Simulation in MATLAB
Overview
This MATLAB script simulates a double auction market where multiple sellers and buyers interact. The script determines the volumes and prices at which trades occur based on bids from both parties. It calculates the accepted volumes and prices for both sellers and buyers, as well as the resulting profits.

Features
Initializes the market with a specified number of sellers and buyers.
Accepts bids and volumes from sellers and buyers.
Matches buyers and sellers based on their bids.
Calculates the accepted volumes, prices, and profits for both sellers and buyers.
Computes the remaining volumes for sellers and buyers after the auction.
Evaluates the profits from selling to or buying from the main grid at a fixed price.
Usage
Initialize Market State:

Define the number of sellers and buyers.
Input the bid prices and volumes for sellers.
Input the bid prices and volumes for buyers.
Run the Auction:

The script matches sellers and buyers based on their bids.
It iteratively finds the minimum seller bid and maximum buyer bid.
It determines the accepted volumes and prices until no more matching is possible.
Calculate Results:

The script computes the profit for each seller and buyer based on the accepted trades.
It also calculates the remaining volumes and potential profits if the remaining volumes are sold or bought from the main grid.
Example
The script initializes the market with the following data:

matlab
Copy code
num_sellers = 3;
num_buyers = 3;

sellers_bids = [2; 14; 3];
sellers_volume = [2; 3; 1];

loads_bids = [20; 15; 33];
loads_volume = [1; 4; 2];
It runs the auction, matches trades, and outputs the results:

matlab
Copy code
profit_accept_sellers = % profits from accepted trades for sellers
profit_sellers_accpet_loads = % total profits for each seller
volume_accept_sellers = % total accepted volumes for each seller

profit_accept_loads = % profits from accepted trades for buyers
profit_loads = % total profits for each buyer
volume_accept_load = % total accepted volumes for each buyer

sellers_volume_left = % remaining volumes for each seller
profit_sellers_tomaingrid = % profits if remaining volumes are sold to the main grid

loads_volume_left = % remaining volumes for each buyer
profit_loads_tomaingrid = % profits if remaining volumes are bought from the main grid
Requirements
MATLAB (any recent version)
Instructions
Copy the script into a new MATLAB script file (double_auction.m).
Modify the initial market state parameters as needed.
Run the script in MATLAB to simulate the double auction and view the results.
Notes
Ensure that the initial bid prices and volumes are correctly set for both sellers and buyers.
The script currently uses fixed prices for selling to and buying from the main grid (p_sell = 26 and p_buy = 10), which can be adjusted as needed.
Contact
For any questions or suggestions, please contact [Your Name] at [your email address].
