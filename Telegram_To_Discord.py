import time
import requests
import json

# Telegram Settings
telegram_bot_token = "your_telegram_bot_token"
telegram_url = f"https://api.telegram.org/bot{telegram_bot_token}/getUpdates"
telegram_offset = 0
telegram_channel_id = "your_telegram_channel_id"  # Replace with your channel ID

# Discord Settings
discord_bot_token = "your_discord_bot_token"
discord_channel_id = "your_discord_channel_id"
discord_url = f"https://discord.com/api/channels/{discord_channel_id}/messages"
discord_headers = {"Authorization": f"Bot {discord_bot_token}", "Content-Type": "application/json"}

# Process runs indefinitely
while True:
    # Get new updates from Telegram
    response = requests.get(telegram_url, params={"offset": telegram_offset})
    updates = response.json()

    for update in updates["result"]:
        # Process each message
        if "message" in update and "chat" in update["message"] and str(update["message"]["chat"]["id"]) == telegram_channel_id:
            message_text = update["message"]["text"]

            # Send the message to Discord
            payload = {"content": message_text}
            response = requests.post(discord_url, headers=discord_headers, data=json.dumps(payload))

            # Update the offset for the next time
            telegram_offset = update["update_id"] + 1

    # Wait for a while before checking for more updates
    time.sleep(1)
