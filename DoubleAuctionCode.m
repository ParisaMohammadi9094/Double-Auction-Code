clear;
close all;
clc;

% initialize market state
num_sellers = 3;
num_buyers = 3;

sellers_bids = [2; 14;3];
sellers_volume = [2; 3; 1];
sellers_volume_initial=sellers_volume;

loads_bids = [20; 15; 33];
loads_volume = [1; 4; 2];
loads_volume_initial=loads_volume;

[minpsell,indminpsell]=min(sellers_bids);
[maxpbuy,indmaxpbuy]=max(loads_bids);
volume_accept_sellers=zeros(num_sellers,1);
price_accept_sellers=zeros(num_sellers,1);
volume_accept_load=zeros(num_buyers,1);
price_accept_load=zeros(num_buyers,1);
i=1
while minpsell<=maxpbuy && sellers_bids(indminpsell,1)<1000 && loads_bids(indmaxpbuy,1)>0 && sellers_bids(indminpsell,1)~=0 %%% sellers_bid won't be equal to zero as we choose it from a known set
    if sellers_volume(indminpsell,1)<loads_volume(indmaxpbuy,1) 
       volume_accept_sellers(indminpsell,i)= sellers_volume(indminpsell,1);
       volume_accept_load(indmaxpbuy,i)=sellers_volume(indminpsell,1);
       loads_volume(indmaxpbuy,1)=loads_volume(indmaxpbuy,1)-sellers_volume(indminpsell,1);
       sellers_volume(indminpsell,1)=0;
       price_accept_sellers(indminpsell,i)=(loads_bids(indmaxpbuy,1)+sellers_bids(indminpsell,1))/2;
       price_accept_load(indmaxpbuy,i)=(loads_bids(indmaxpbuy,1)+sellers_bids(indminpsell,1))/2;
       sellers_bids(indminpsell,1)=1000;
    elseif  sellers_volume(indminpsell,1)==loads_volume(indmaxpbuy,1)
       volume_accept_sellers(indminpsell,i)= sellers_volume(indminpsell,1);
       volume_accept_load(indmaxpbuy,i)=sellers_volume(indminpsell,1);
       loads_volume(indmaxpbuy,i)=0;
       sellers_volume(indminpsell,1)=0;
       price_accept_sellers(indminpsell,i)=(loads_bids(indmaxpbuy,1)+sellers_bids(indminpsell,1))/2;
       price_accept_load(indmaxpbuy,i)=(loads_bids(indmaxpbuy,1)+sellers_bids(indminpsell,1))/2;
       sellers_bids(indminpsell,1)=1000;
       loads_bids(indmaxpbuy,1)=-3;
    else
        volume_accept_sellers(indminpsell,i)=loads_volume(indmaxpbuy,1);
        volume_accept_load(indmaxpbuy,i)=loads_volume(indmaxpbuy,1);
        sellers_volume(indminpsell,1)=sellers_volume(indminpsell,1)-loads_volume(indmaxpbuy,1);
        loads_volume(indmaxpbuy,1)=0;
        price_accept_sellers(indminpsell,i)=(loads_bids(indmaxpbuy,1)+sellers_bids(indminpsell,1))/2;
        price_accept_load(indmaxpbuy,i)=(loads_bids(indmaxpbuy,1)+sellers_bids(indminpsell,1))/2;
        loads_bids(indmaxpbuy,1)=-3;
    end
        [minpsell,indminpsell]=min(sellers_bids);
        [maxpbuy,indmaxpbuy]=max(loads_bids) ;
        i=i+1;
end

profit_accept_sellers=volume_accept_sellers.*price_accept_sellers
profit_sellers_accpet_loads= sum(profit_accept_sellers,2)

volume_accept_sellers=sum(volume_accept_sellers,2)

profit_accept_loads=volume_accept_load.*price_accept_load
profit_loads= sum(profit_accept_loads,2)

volume_accept_load=sum(volume_accept_load,2)

p_sell=26;
p_buy=10;

sellers_volume_left=sellers_volume_initial-volume_accept_sellers
profit_sellers_tomaingrid=sellers_volume_left*p_sell

loads_volume_left=loads_volume_initial-volume_accept_load
profit_loads_tomaingrid=loads_volume_left*p_buy



