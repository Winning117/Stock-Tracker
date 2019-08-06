# Stock-and-Crypto-Tracker
Shows you how much money you've gained per stock, per cryptocurrency, or both!  

# Before you run this:
Open up a terminal and copy/paste the following commands:  
</br>
<b>MacOS:</b>  
Install Homebrew: `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`  
Install python3: `brew install python3`  
`pip3 install yfinance`  
`pip3 install coinmarketcap`  
</br>
<b>Linux:</b>  
Install python3: `sudo apt-get install python3`  
Install pip3: `sudo apt-get install python3-pip`  
`pip3 install yfinance`  
`pip3 install coinmarketcap` 

# How to configure this tool:
If you wish to track stocks, edit my_stocks.txt  
If you wish to track cryptocurrency, edit my_crypto.txt  
Both will be configured into your total gains/losses if you have values in both files  
If you bought the same stock at multiple price points, you can add the price points on different lines like so:  
AAPL, 100, 25  
AAPL, 200, 5  

# How to run this tool:
Open up a terminal and type `python3 track.py` and that's it!
