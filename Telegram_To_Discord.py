import time
import requests
import json
import re


# Telegram settings
# Replace 'your_telegram_bot_token' with your actual Telegram bot token
telegram_bot_token = "your_telegram_bot_token"
# The URL for the Telegram API to get updates from the Telegram bot
telegram_url = f"https://api.telegram.org/bot{telegram_bot_token}/getUpdates"
# Initialize the Telegram offset to 0 (this is used to avoid processing the same update multiple times)
telegram_offset = 0
# Replace 'your_telegram_channel_id' with the actual ID of the Telegram channel you want to monitor
telegram_channel_id = "your_telegram_channel_id"  

# Discord settings
# Replace 'your_discord_bot_token' with your actual Discord bot token
discord_bot_token = "your_discord_bot_token"
# Replace 'your_discord_channel_id' with the actual ID of the Discord channel you want to send messages to
discord_channel_id = "your_discord_channel_id"
# The URL for the Discord API to send messages to a channel
discord_url = f"https://discord.com/api/channels/{discord_channel_id}/messages"
# The headers required for the Discord API
discord_headers = {"Authorization": f"Bot {discord_bot_token}", "Content-Type": "application/json"}

# Regex pattern to find image URLs in a string
# This pattern matches any URL that ends with .jpg, .gif, or .png
image_url_pattern = re.compile(r"(http(s?):)([/|.|\w|\s|-])*\.(?:jpg|gif|png)")

# The main loop of the program runs indefinitely
while True:
    try:
        # Get new updates from the Telegram bot
        response = requests.get(telegram_url, params={"offset": telegram_offset})
        updates = response.json()

        # Process each update
        for update in updates["result"]:
            # Check if the update is a message from the Telegram channel we're monitoring
            if "message" in update and "chat" in update["message"] and str(update["message"]["chat"]["id"]) == telegram_channel_id:
                # Check if the message has text (it might not have text if it's a photo, sticker, etc.)
                if "text" in update["message"]:
                    # Extract the text from the message
                    message_text = update["message"]["text"]

                    # Use the regex pattern to check if the message text contains an image URL
                    match = image_url_pattern.search(message_text)
                    if match:
                        # The message contains an image URL, so we create a payload with an embed to show the image in Discord
                        payload = {
                            "embeds": [
                                {
                                    "description": message_text,
                                    "image": {"url": match.group()},
                                }
                            ]
                        }
                    else:
                        # The message does not contain an image URL, so we create a payload with just the text
                        payload = {"content": message_text}

                    # Send the payload to the Discord API to send the message to the Discord channel
                    response = requests.post(discord_url, headers=discord_headers, data=json.dumps(payload))

                # Update the Telegram offset so we don't process the same update again next time
                telegram_offset = update["update_id"] + 1

        # Wait for a second before getting updates again
        time.sleep(1)

    except Exception as e:
        # If an error occurred, print it and wait for 5 seconds before trying again
        print(f"An error occurred: {e}")
        time.sleep(5)
