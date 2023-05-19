# Telegram-to-Discord-Bot

This is a really basic and simple Python script that retrieves messages from a Telegram channel and then sends them to a Discord channel. It allows for connection and communication between Telegram and Discord.

## Setup

1. You need valid API tokens for Telegram and Discord to access their respective APIs. Replace the placeholders "your_telegram_bot_token", "your_telegram_channel_id", "your_discord_bot_token", and "your_discord_channel_id" with your own tokens and IDs.

2. Make sure you have the required dependencies installed. This script uses the `requests` and `json` libraries to make HTTP requests and process JSON data. You can install them using `pip`:

   ```bash
   pip install requests

## Usage

Run the script, and it will continuously monitor for new updates in the Telegram channel. Once a new message is found, it will be copied and sent to the Discord channel. The script also supports the transmission of images through links found within the Telegram messages.

To run the script, open a command prompt or terminal window and navigate to the directory where the script is located. Execute the following command:

```bash
python Telegram_To_Discord.py
```

The script will run in the background, patiently waiting for new messages. You can stop it by pressing Ctrl+C in the command prompt.
Notes

    The script uses the time.sleep(1) function to pause for one second before checking for more updates. This interval between checks can be adjusted by modifying the parameter of the sleep function.

    The script handles text messages and image links (ending in .jpg, .gif, or .png). Other types of messages, such as documents or non-image media, will not be transmitted to Discord.

    The script only sends messages from Telegram to Discord. It does not support back-transmission of messages from Discord to Telegram.

    The script uses exception handling to manage errors that may occur during execution, such as network issues. In such cases, the script will wait for 5 seconds before retrying.

Remember to provide the necessary permissions for your bots in both Telegram and Discord for smooth operation.

## License
This script is licensed under the [MIT License](LICENSE). For more information, please see the [LICENSE](LICENSE) file.


## Author

Created by eClipZe88.
