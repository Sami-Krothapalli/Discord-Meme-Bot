# Discord Meme Bot

This is a simple Discord bot built with Python and the `discord.py` library that can respond to user messages with various functionalities such as greeting users and fetching random memes from a public meme API. The bot leverages the Discord API and the Meme API to interact with users and fetch entertaining content for them.

## Features

1. **$hello**: The bot responds with a greeting message when a user types `$hello` in the chat.
2. **$meme**: The bot fetches a random meme from the Meme API and shares it in the channel when a user types `$meme`.
3. **$eman**: The bot sends a humorous message about Eman and their skill at Valorant when the user types `$eman`.

## Prerequisites

To run this bot, you need the following:

- Python 3.x
- `discord.py` library (`pip install discord.py`)
- `requests` library (`pip install requests`)
- `python-dotenv` library (`pip install python-dotenv`)
- A Discord Bot Token (see instructions below)

## Getting Started

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/your-username/discord-meme-bot.git
cd discord-meme-bot
```

### 2. Install Dependencies

Install the required dependencies using `pip`:

```bash
pip install discord.py requests python-dotenv
```

### 3. Set Up Environment Variables

You need to create a `.env` file in the root directory of the project and add your Discord bot token. This token will be used to authenticate the bot with Discord.

```bash
DISCORD_BOT_TOKEN=your_discord_bot_token
```

Replace `your_discord_bot_token` with your actual token from the [Discord Developer Portal](https://discord.com/developers/applications).

### 4. Running the Bot

To start the bot, simply run the following command:

```bash
python bot.py
```

You should see a message in the console that says `Logged on as your-bot-name!` indicating that the bot is running and connected to Discord.

### 5. Interacting with the Bot

- To greet the bot, type `$hello` in any text channel that the bot has access to.
- To fetch a meme, type `$meme` and the bot will reply with a random meme image.
- For a humorous message, type `$eman`.

### How It Works
- The bot listens for messages in the channels it has access to and responds to specific commands.
- It makes use of the Meme API (https://meme-api.com/gimme) to fetch random memes as a JSON object and extract the meme URL.
- The .env file is used to keep sensitive data (Discord token) private and secure.
### Files
- bot.py: The main file that contains the bot's code.
- .env: The file containing environment variables like the bot token (not included in the repository for security reasons).
- README.md: This file.

### Notes
- Ensure that the bot has the necessary permissions to read and send messages in your server.
- You may want to expand the bot by adding more commands or integrating additional APIs.
---
Feel free to fork this repository and submit pull requests if you would like to improve or add new features to the bot.
