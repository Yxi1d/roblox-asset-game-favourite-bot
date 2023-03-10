import requests

# Enter your Roblox account information here
username = "your_username"
password = "your_password"

# Enter the game or asset ID that you want to favorite
asset_id = "youridheredoesntmatterifassetorgame"

# Define the endpoint URLs
login_url = "https://auth.roblox.com/v2/login"
favorite_url = f"https://www.roblox.com/v1/assets/{asset_id}/favorites"

# Create a session and log in to the Roblox account
session = requests.Session()
session.post(login_url, json={"username": username, "password": password})

# Favorite the specified asset
session.post(favorite_url)

# Close the session
session.close()
