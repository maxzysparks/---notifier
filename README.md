# ---notifier
Here is a simple outline of a code that can notify you when a token increases or decreases in price:
This code assumes that you have defined a function called get_current_price() that takes a token as input and returns its current price, 
and a function called send_notification() that takes a message as input and sends a notification to you.

You can use this code by calling the check_price() function and passing in the token you want to track 
and the threshold price at which you want to be notified.
The function will query the current price of the token and compare it to the threshold,
and if the price is above or below the threshold, it will send a notification to you.

For example, if you want to be notified when the price of BTC (Bitcoin) decreases below $50,000, you can call the check_price() function like this:

check_price('BTC', 50000)

This code is just a simple outline, so you may need to add additional logic and error-handling to make it more robust and efficient.
Additionally, you will need to implement the get_current_price() and send_notification() functions in order to make this code work.
