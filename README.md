# Token Price Checker
This is a simple Python script that checks the current price of a given token and sends a notification if it is above or below a given threshold.

Prerequisites
Python 3.x
Requests library (install with pip install requests)
## Usage

  

To use the script, call the check_price() function with the following arguments:  
  


check_price(token: str, threshold: float)
- **token** is the name of the token to check the price of.
- **threshold** is the price threshold. If the current price of the token is above or below this threshold, a notification will be sent.
