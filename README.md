# Telegram-to-Discord-Bot

This is a really basic and simple Python script that retrieves messages from a Telegram channel and then sends them to a Discord channel. It allows for connection and communication between Telegram and Discord.

## Setup

1. You need valid API tokens for Telegram and Discord to access their respective APIs. Replace the placeholders "your_telegram_bot_token", "your_telegram_channel_id", "your_discord_bot_token", and "your_discord_channel_id" with your own tokens and IDs.

2. Make sure you have the required dependencies installed. This script uses the `requests` and `json` libraries to make HTTP requests and process JSON data. You can install them using `pip`:

   ```bash
   pip install requests

## Usage

Run the script, and it will continuously look for new updates in the Telegram channel. Once a new message is found, it will be sent to the Discord channel.

To run the script, open a command prompt or terminal window and navigate to the directory where the script is located. Execute the following command:

<pre><code>python Telegram_To_Discord.py
</code></pre>


The script will run in the background, waiting for new messages. You can stop it by pressing Ctrl+C in the command prompt.
Notes

    The script uses the time.sleep(1) function to wait for one second before checking for more updates. You can adjust the waiting time by modifying the parameter of sleep.
    The script only handles text messages. Other types of messages, such as images or documents, will be ignored.
    The script only sends messages to Discord. There is no back-transmission of messages from Discord to Telegram.

## License

This script is licensed under the MIT License. For more information, please see the LICENSE file.


## Author

Created by eClipZe88.
