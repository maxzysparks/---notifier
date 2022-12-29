import requests

def get_current_price(token: str) -> float:
  """
  Retrieves the current price of the given token.
  """
  # Replace with API call to retrieve current price
  return requests.get(f'https://api.example.com/price?token={token}').json()['price']

def send_notification(message: str):
  """
  Sends a notification with the given message.
  """
  # Replace with code to send notification
  print(message)

def check_price(token: str, threshold: float):
  """
  Checks the current price of the given token and sends a notification if it is above or below the given threshold.
  """
  # Query current price of token
  current_price = get_current_price(token)
  
  # Check if current price is above or below threshold
  if current_price > threshold:
    
    # Send notification that price has increased
    send_notification(f'{token} price has increased!')
  elif current_price < threshold:
    
    # Send notification that price has decreased
    send_notification(f'{token} price has decreased!')
  else:
    
    # Send notification that price has not changed
    send_notification(f'{token} price has not changed.')
