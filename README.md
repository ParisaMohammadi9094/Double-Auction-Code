**Double Auction in Energy Markets**  
A double auction is a type of auction in which multiple buyers (loads) and multiple sellers (producers) submit bids simultaneously. The market aims to clear by matching these bids to determine the price and volume of trades, ensuring efficient market operations. This mechanism is particularly relevant in energy markets where both energy producers and consumers participate to buy and sell electricity.

**How Double Auction Works**

**Bids Submission:**    
Sellers (Producers): Each seller submits a bid indicating the price at which they are willing to sell a certain volume of energy. For example, a producer might offer to sell 3 units of energy at $14 per unit.
Buyers (Loads): Each buyer submits a bid indicating the price they are willing to pay for a certain volume of energy. For example, a consumer might offer to buy 4 units of energy at $15 per unit.  

**Bid Comparison:**  
The auctioneer compares the bids from sellers and buyers to find potential matches.
The key objective is to find the minimum price a seller is willing to accept and the maximum price a buyer is willing to pay.

**Matching Process:**
Sellers' bids are sorted in ascending order based on the price.
Buyers' bids are sorted in descending order based on the price.
The auctioneer starts by matching the lowest seller bid with the highest buyer bid. If the seller's price is less than or equal to the buyer's price, a trade occurs.
The volume of energy traded is the minimum of the seller's offered volume and the buyer's requested volume.

**Market Clearing Price:**
The price at which the trade occurs is typically the average of the seller's bid price and the buyer's bid price.
This process continues iteratively until no more matches can be made (i.e., the lowest seller's price is higher than the highest buyer's price).  

**Unmatched Bids:**
Sellers and buyers whose bids are not matched either revise their bids in the next round or withdraw from the market.
The remaining volumes can be sold or bought at a default market price if the market allows for such a mechanism.

**Example Scenario**
Consider a simple market with three sellers and three buyers:

**Sellers' Bids:**
Seller 1: 2 units at $2/unit  
Seller 2: 3 units at $14/unit  
Seller 3: 1 unit at $3/unit  

**Buyers' Bids:**
Buyer 1: 1 unit at $20/unit  
Buyer 2: 4 units at $15/unit  
Buyer 3: 2 units at $33/unit  

**Matching Process:**
Match Seller 1 (2 units at $2) with Buyer 3 (2 units at $33). The trade occurs at the average price of $17.50/unit.
Match Seller 3 (1 unit at $3) with Buyer 1 (1 unit at $20). The trade occurs at the average price of $11.50/unit.
Match Seller 2 (3 units at $14) with Buyer 2 (3 units at $15, note Buyer 2 originally wanted 4 units but only 3 units are left to match). The trade occurs at the average price of $14.50/unit.
After matching, any remaining volumes would be unmatched bids or traded at a default price if applicable.

**Benefits of Double Auction**
**Efficiency:** Double auctions tend to result in efficient market outcomes by finding the price that balances supply and demand.  
**Market Clearing:** It ensures that the market clears, meaning all possible trades at mutually agreeable prices are executed.  
**Price Discovery:** It helps in discovering the true market price for energy, reflecting the willingness to pay and accept among participants.  

**Applications in Microgrids** 
In the context of microgrids, where energy is managed locally with a mix of renewable sources and storage, double auctions can optimize energy distribution. By using algorithms to automate the matching process, microgrids can efficiently balance supply and demand, minimize costs, and maximize the use of renewable energy sources.

Overall, double auctions provide a robust framework for dynamic pricing and efficient market operations in energy systems.

**Double Auction Simulation in MATLAB**  
**Overview**  
This MATLAB script simulates a double auction market where multiple sellers and buyers interact. The script determines the volumes and prices at which trades occur based on bids from both parties. It calculates the accepted volumes and prices for both sellers and buyers, as well as the resulting profits.

**Features**
Initializes the market with a specified number of sellers and buyers.  
Accepts bids and volumes from sellers and buyers.  
Matches buyers and sellers based on their bids.  
Calculates the accepted volumes, prices, and profits for both sellers and buyers.  
Computes the remaining volumes for sellers and buyers after the auction.  
Evaluates the profits from selling to or buying from the main grid at a fixed price.  


**Notes**
Ensure that the initial bid prices and volumes are correctly set for both sellers and buyers.
The script currently uses fixed prices for selling to and buying from the main grid (p_sell = 26 and p_buy = 10), which can be adjusted as needed.
