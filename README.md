# botProto1

Rules:

1. Use good programming practices. Read the textbook to know what these are. 
2. Don't commit changes unless they work. 
3. Start a new branch if you're working on something not exactly related to the main goal at the moment. 
4. If you need help using github to its fullest potential, read the book. Promise it's in there. 
5. Best if used with linux 
6. This is a closed project. 

Purpose:
The first purpose is to make a bot that will automatically trade for its user on Binance. The kind of trades it will make are using the triangular arbitrage strategy. This is where sell A for B, B for C, and C for A again. This is only possible when there is a pricing inefficiency in the market between the three coins. The profit it will make is the difference in the prices of the trades, minus the trading fee. 

Strategy:
In order to do this, it must get its own current wallet values first. After this, obtain the exchange rates between the coins intended on trading between. Then see if it can make a profit between three, including fees. Next, see how much of each coin need to be bought given current funds in wallet. Then make trade one, wait till completion, make trade two, wait for completion, then make trade three and wait for completion. Then make another calculation to obtain its wallet balances after the trade. 

Problems:
-Figuring out how much of each coin need to be bought
-Figuring out fees at each stage? 
-Waiting for trade to complete? 
-Doing the three trades consecutively
